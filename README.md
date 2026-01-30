# Pardeep Tiwari - AI-Powered Portfolio

An interactive Streamlit-based portfolio application featuring an AI chatbot (PardeepBot) that can answer questions about professional experience, skills, and projects in real-time.

## 🌟 Features

- **🤖 AI Assistant (PardeepBot)**: Interactive chatbot powered by Google's Gemini AI
- **📱 Responsive Design**: Clean, modern UI that adapts to all devices
- **💼 Professional Sections**: About Me, Technical Experience, Resume, Contact
- **🎨 Custom Styling**: Theme-aware design with beautiful gradients
- **⚡ Real-time Responses**: Context-aware answers using RAG (Retrieval-Augmented Generation)
- **📊 Smart Content**: Curated Q&A pairs for instant responses to common questions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key**
   
   Edit `.streamlit/secrets.toml` and add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your-actual-api-key-here"
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
pardeep_portfolio/
│
├── app.py                      # Main application entry point
├── stored_questions.py         # Curated Q&A pairs
├── requirements.txt            # Python dependencies
│
├── .streamlit/
│   └── secrets.toml           # API configuration (DO NOT COMMIT!)
│
├── assets/
│   └── bio.txt                # Professional bio for AI context
│
├── ui/                        # User interface components
│   ├── chat.py                # AI chat interface with memory
│   ├── experience.py          # Work experience timeline
│   ├── resume.py              # Skills and education
│   ├── contact.py             # Contact information
│   └── side_panel.py          # Profile sidebar
│
├── logic/                     # Business logic
│   ├── llm.py                 # Gemini AI integration
│   ├── rag.py                 # Context retrieval
│   └── similarity.py          # Question matching
│
└── data/                      # Data management
    └── curated.py             # Blocked content & filters
```

## 💡 Using the Chat Feature

PardeepBot can answer questions like:
- "What's your experience with machine learning?"
- "Tell me about your current role at General Mills"
- "What technologies and tools do you use?"
- "What are your biggest achievements?"
- "What's your educational background?"
- "How can I contact you?"

## 🎨 Customization

### Update Your Information

1. **Professional Bio** (`assets/bio.txt`)
   - Contains your complete professional background
   - Used by AI to answer questions accurately

2. **Curated Q&A** (`stored_questions.py`)
   - Pre-defined answers for common questions
   - Provides instant responses without AI calls

3. **Experience** (`ui/experience.py`)
   - Work history and achievements
   - Project descriptions

4. **Skills** (`ui/resume.py`)
   - Technical skills and tools
   - Education and certifications

5. **Contact** (`ui/contact.py`)
   - Contact information
   - Location and availability

### Customize Styling

- Edit CSS in `app.py` to change colors and themes
- Modify gradient colors (#667eea, #764ba2)
- Adjust card styles and spacing

## 🔑 Getting Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Copy the key and paste it in `.streamlit/secrets.toml`

**Note**: The app works without the API key using fallback responses, but the AI chat is much smarter with Gemini.

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push your code to GitHub (don't commit `secrets.toml`!)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `GEMINI_API_KEY` in Streamlit Cloud secrets
5. Deploy!

Your portfolio will be live at: `your-app-name.streamlit.app`

## 🛠️ Troubleshooting

### AI not responding?
- Check if your API key is correct in `.streamlit/secrets.toml`
- Verify internet connection
- The app will use fallback responses if Gemini is unavailable

### App not starting?
- Install all dependencies: `pip install -r requirements.txt`
- Check Python version (needs 3.8+): `python --version`
- Look for error messages in the terminal

### Import errors?
- Make sure you're in the `pardeep_portfolio` directory
- Create `__init__.py` files if missing in ui/logic/data folders

## 📝 Technical Details

### AI Chat System

The chatbot uses a multi-layer approach:
1. **Content Filtering**: Blocks inappropriate questions
2. **Question Classification**: Identifies portfolio-relevant queries
3. **Curated Responses**: Instant answers for common questions
4. **AI Generation**: RAG-powered responses using Gemini for complex questions
5. **Conversation Memory**: Maintains context across chat history

### Technologies Used

- **Streamlit**: Web application framework
- **Google Gemini AI**: Large language model
- **RAG (Retrieval-Augmented Generation)**: Context-aware responses
- **TF-IDF**: Text similarity matching
- **scikit-learn**: Machine learning utilities

## 📄 License

This project is open source and available for personal use.

## 🙏 Acknowledgments

Based on modern AI-powered portfolio concepts with Streamlit framework and inspired by the open-source community.

## 📞 Contact

**Pardeep Tiwari**
- Email: pardeep.tiwari@live.com
- Phone: +91-8527661324
- LinkedIn: [linkedin.com/in/pardeeptiwari](https://www.linkedin.com/in/pardeeptiwari/)
- Location: Mumbai, India

---

**⭐ If this portfolio inspired you, please star it and share with others!**

Made with ❤️ using Streamlit and Google Gemini AI
