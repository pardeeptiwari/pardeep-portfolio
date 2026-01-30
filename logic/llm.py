from typing import Generator, List, Dict
import time
import streamlit as st


def ask_bot_stream(input_text: str, bio_context: str, chat_history: List[Dict[str, str]] = None) -> Generator[str, None, None]:
    """
    Streams text chunks back to the caller with conversation memory support.
    
    Args:
        input_text: Current user question
        bio_context: RAG-retrieved context + conversation summary 
        chat_history: Complete conversation history for additional context
    """
    # Rate-limit quick repeats
    now = time.time()
    last = st.session_state.get("last_llm_ts", 0)
    if now - last < 2.5:
        yield "I'm answering too quickly. Please wait a moment."
        return
    st.session_state["last_llm_ts"] = now

    # Enhanced system instruction with memory awareness
    system_instruction = (
        "You are AnkBot, an AI assistant representing Ankur Shukla, a Senior Data Scientist with 6+ years of experience.\n"
        "CONTEXT USAGE:\n"
        "- Use the provided context as your primary source of information\n"
        "- Pay attention to previous conversation context to maintain continuity\n"
        "- If information isn't in the context, politely direct users to contact Ankur directly\n"
        "- Never invent or assume information not provided\n\n"
        "CONVERSATION MEMORY:\n"
        "- Remember what was discussed earlier in this conversation\n"
        "- Build upon previous answers when asked follow-up questions\n"
        "- Reference specific details mentioned earlier when relevant (e.g., 'the chatbot project I mentioned')\n"
        "- If user asks about 'that project' or 'those skills', refer back to what was recently discussed\n"
        "- Maintain conversation flow and provide contextual responses\n\n"
        "FOLLOW-UP QUESTION HANDLING:\n"
        "- If user asks 'which one?', 'tell me more', 'what about that?', etc., reference previous discussion\n"
        "- When user mentions 'you said' or 'you mentioned', acknowledge and build on that\n"
        "- For vague references like 'it', 'that', 'those', infer from recent context\n\n"
        "RESPONSE STYLE:\n"
        "- Professional yet conversational tone\n"
        "- Use plain text (no markdown)\n"
        "- Use hyphens (-) for bullet points\n"
        "- Keep responses focused and relevant\n"
        "- Include specific metrics and results when available in context\n\n"
        "CONTACT INFO:\n"
        "For detailed discussions or opportunities, direct users to: ankurshukla19961@gmail.com"
    )

    # The bio_context now includes conversation summary from chat.py
    # So we just need to structure the prompt clearly
    full_prompt = (
        f"CONTEXT:\n{bio_context}\n\n"
        f"CURRENT USER QUESTION: {input_text}\n\n"
        "Based on the context above (which includes both bio information and recent conversation), "
        "provide a helpful response. If this appears to be a follow-up question, make sure to "
        "reference relevant information from our previous discussion. "
        "If you need to clarify what the user is referring to, ask politely."
    )

    api_key = st.secrets.get("GEMINI_API_KEY", None)
    if not api_key:
        yield "API configuration missing. Please contact the administrator."
        return

    # Try new library: `google-genai`
    try:
        from google import genai  # type: ignore

        client = genai.Client(api_key=api_key)
        stream = client.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=full_prompt,
            config={
                "system_instruction": system_instruction,
                "temperature": 0.3,  # Slightly higher for more natural conversation
                "max_output_tokens": 1000,
                "top_p": 0.8,
                "top_k": 40,
            },
        )
        for chunk in stream:
            txt = getattr(chunk, "text", "") or ""
            if txt:
                yield txt
        return
    except Exception:
        pass

    # Fallback to older `google-generativeai`
    try:
        import google.generativeai as genai  # type: ignore

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite",
            system_instruction=system_instruction,
        )
        response = model.generate_content(
            full_prompt,
            stream=True,
            generation_config={
                "temperature": 0.3,  # Slightly higher for conversational flow
                "max_output_tokens": 1000,
                "top_p": 0.8,
            },
        )
        for chunk in response:
            txt = getattr(chunk, "text", "") or ""
            if txt:
                yield txt
        return
    except Exception as e:
        msg = str(e).lower()
        if "model not found" in msg:
            yield "The AI model is temporarily unavailable. Please try again in a moment."
        elif "quota" in msg or "limit" in msg:
            yield "I'm getting a lot of questions right now! Please try again in a minute."
        elif "api key" in msg or "permission" in msg:
            yield "There's an authentication issue. Please contact the administrator."
        else:
            yield "I'm having a brief connection issue. Please try your question again."
            