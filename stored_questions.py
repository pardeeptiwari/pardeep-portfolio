# stored_questions.py
# Curated Q&A used by the chatbot before calling the LLM.

var = {
    # === CONTACT / PROFILES ===
    "contact": (
        "You can reach Pardeep at:\n"
        "- Email (preferred): pardeep.tiwari@live.com\n"
        "- Phone: +91-8527661324\n"
        "- LinkedIn: https://www.linkedin.com/in/pardeeptiwari/"
    ),
    "how can i contact you": (
        "You can reach Pardeep at:\n"
        "- Email (preferred): pardeep.tiwari@live.com\n"
        "- Phone: +91-8527661324\n"
        "- LinkedIn: https://www.linkedin.com/in/pardeeptiwari/"
    ),
    
    # === EMAIL VARIATIONS ===
    "email": "Email: pardeep.tiwari@live.com",
    "email address": "Email: pardeep.tiwari@live.com",
    "his email": "Email: pardeep.tiwari@live.com",
    "pardeep email": "Email: pardeep.tiwari@live.com",
    "contact email": "Email: pardeep.tiwari@live.com",
    "reach out": "You can reach Pardeep at pardeep.tiwari@live.com or +91-8527661324",
    
    "phone": "Phone: +91-8527661324",
    "phone number": "Phone: +91-8527661324",
    "contact number": "Phone: +91-8527661324",
    "linkedin": "LinkedIn: https://www.linkedin.com/in/pardeeptiwari/",

    # === SUMMARY / HEADLINE ===
    "summary": (
        "Senior Data Scientist with 15+ years of experience building production-grade AI/ML systems across Retail and CPG.\n"
        "- Expert in end-to-end ML lifecycle on GCP (Vertex AI, BQML)\n"
        "- Led cross-functional teams delivering forecasting, GenAI, and optimization solutions\n"
        "- Generated $15M+ revenue impact through AI/ML solutions\n"
        "- Strong background in LLMs, Agentic AI, time-series modeling, and cloud-native architectures"
    ),
    "about": (
        "Senior Data Scientist with 15+ years of experience in AI/ML systems for Retail and CPG industries. "
        "Expert in GCP, forecasting, GenAI, and optimization with $15M+ revenue impact."
    ),
    "who is pardeep": (
        "Pardeep Tiwari is a Senior Data Scientist with 15+ years of experience. Currently at General Mills India, "
        "he specializes in AI/ML, forecasting, and cloud-native architectures with $15M+ revenue impact."
    ),

    # === CURRENT ROLE ===
    "current role": (
        "Senior Data Scientist at General Mills India (July 2022 – Present, Mumbai).\n"
        "- Architected AI-driven forecast exception management (15-20% volatility reduction, 30% efficiency gain)\n"
        "- Developed time-series forecasting models (8-12% MAPE improvement, $10M+ revenue impact)\n"
        "- Built ML scorecards for C-suite decision-making\n"
        "- Established MLOps practices and governance frameworks\n"
        "- Mentored 6-8 data scientists (25% faster onboarding)"
    ),
    "where do you work now": (
        "Pardeep works as a Senior Data Scientist at General Mills India in Mumbai since July 2022."
    ),
    "current company": "General Mills India Pvt Ltd (July 2022 – Present)",
    "where does he work": "General Mills India in Mumbai",

    # === WORK EXPERIENCE ===
    "work experience": (
        "Work Experience:\n\n"
        "- General Mills India — Senior Data Scientist (July 2022 – Present, Mumbai)\n"
        "  - AI-driven forecast management; 15-20% volatility reduction; $10M+ revenue impact\n"
        "  - MLOps practices; mentored 6-8 data scientists\n\n"
        "- Dunnhumby IT Services — Lead Applied Data Scientist (May 2015 – July 2022, Gurugram)\n"
        "  - ML solutions for Fortune 500 retail clients\n"
        "  - Pricing/optimization solutions; $5M+ revenue impact; 10-15% campaign improvement\n\n"
        "- Inductis — Senior Business Analyst (June 2012 – May 2015, Gurugram)\n"
        "  - Retail & supply chain solutions; 3-5% cost reductions\n\n"
        "- TCS — Assistant System Engineer (Sep 2010 – June 2012, Gurugram)\n"
        "  - Data management optimization; 40% manual effort reduction"
    ),
    "professional experience": (
        "15+ years across General Mills, Dunnhumby, Inductis, and TCS. "
        "Specialized in AI/ML for retail and CPG with $15M+ total impact."
    ),
    "experience": "15+ years in Data Science and ML across Retail and CPG industries",
    "how many years of experience": "15+ years of experience in data science and machine learning",
    "years of experience": "15+ years",

    # === EDUCATION - VERY IMPORTANT ===
    "education": (
        "Education:\n"
        "- M.Tech, Artificial Intelligence and Machine Learning\n"
        "  Indian Institute of Technology (IIT), Jammu\n"
        "  June 2023 – June 2025 | CGPA: 8.89/10\n\n"
        "- B.Tech, Electronics & Communication Engineering\n"
        "  Lovely Professional University\n"
        "  July 2007 – June 2010 | CGPA: 7.42/10"
    ),
    "degree": (
        "Pardeep has two degrees:\n"
        "1. M.Tech in AI & Machine Learning from IIT Jammu (2023-2025, CGPA: 8.89/10)\n"
        "2. B.Tech in Electronics & Communication from Lovely Professional University (2007-2010, CGPA: 7.42/10)"
    ),
    "masters": (
        "M.Tech (Master of Technology) in Artificial Intelligence and Machine Learning from "
        "Indian Institute of Technology (IIT), Jammu. Currently pursuing (June 2023 – June 2025) with CGPA: 8.89/10"
    ),
    "masters degree": (
        "M.Tech in Artificial Intelligence and Machine Learning from IIT Jammu (2023-2025, CGPA: 8.89/10)"
    ),
    "mtech": (
        "M.Tech in Artificial Intelligence and Machine Learning from IIT Jammu (2023-2025, CGPA: 8.89/10)"
    ),
    "iit": "Currently pursuing M.Tech in AI and Machine Learning from IIT Jammu (CGPA: 8.89/10)",
    "iit jammu": "M.Tech in AI and Machine Learning from IIT Jammu (June 2023 – June 2025, CGPA: 8.89/10)",
    "university": (
        "Pardeep's universities:\n"
        "- Indian Institute of Technology (IIT), Jammu - M.Tech in AI/ML (ongoing)\n"
        "- Lovely Professional University - B.Tech in ECE (completed)"
    ),
    "from which university": (
        "Pardeep completed his M.Tech in AI and Machine Learning from Indian Institute of Technology (IIT), Jammu "
        "(2023-2025, CGPA: 8.89/10) and his B.Tech from Lovely Professional University (2007-2010)"
    ),
    "which university": (
        "IIT Jammu for M.Tech in AI/ML and Lovely Professional University for B.Tech in Electronics & Communication"
    ),
    "where did you study": (
        "Pardeep studied at IIT Jammu (M.Tech in AI/ML) and Lovely Professional University (B.Tech in ECE)"
    ),

    # === PROJECTS ===
    "projects": (
        "Notable Projects:\n"
        "- AI-driven Forecast Exception Management (GCP, General Mills)\n"
        "- Production Time-Series Forecasting Models ($10M+ impact)\n"
        "- Customer Optimal Entry Point Targeting (XGBoost, Random Forest)\n"
        "- Front of Store Basket Missions (K-Means, NMF clustering)\n"
        "- Propensity Models (7% redemption improvement)\n"
        "- Customer Journey Tracking (Clickstream analysis, Hive, Adobe Omniture)"
    ),
    "best project": (
        "AI-driven forecast exception management framework at General Mills:\n"
        "- Reduced forecast volatility by 15-20%\n"
        "- Improved planner efficiency by 30%\n"
        "- Deployed on GCP with Vertex AI\n"
        "- Impacted global supply chain planning"
    ),
    "tell me about your projects": (
        "At General Mills, I built an AI-driven forecast exception management system on GCP that reduced volatility by 15-20%. "
        "At Dunnhumby, I led customer targeting and propensity modeling projects using XGBoost and Random Forest, "
        "improving campaign effectiveness by 10-15%."
    ),

    # === SKILLS ===
    "skills": (
        "Core Skills:\n"
        "- Languages: Python, PySpark, SQL, SAS\n"
        "- Cloud: GCP, Vertex AI, BigQuery ML\n"
        "- ML/AI: Supervised/Unsupervised ML, Deep Learning, NLP, Time-Series Forecasting\n"
        "- Advanced AI: Transformers, LLMs, Generative AI, Agentic AI\n"
        "- MLOps: Docker, Kubernetes, CI/CD, Model Monitoring\n"
        "- Frameworks: LangChain, LangGraph, RAG\n"
        "- Analytics: Tableau, Looker, Adobe Omniture"
    ),
    "technical skills": (
        "Python, PySpark, SQL, GCP (Vertex AI, BQML), ML/AI (Deep Learning, NLP, Time-Series), "
        "LLMs, Generative AI, Docker, Kubernetes, LangChain, RAG"
    ),
    "what technologies": "Python, PySpark, SQL, GCP, Vertex AI, ML/AI, LLMs, Docker, Kubernetes, LangChain",
    "programming languages": "Python (primary), PySpark, SQL, SAS",
    "cloud platforms": "Google Cloud Platform (GCP) with expertise in Vertex AI and BigQuery ML",

    # === ACHIEVEMENTS ===
    "achievements": (
        "Key Achievements:\n"
        "- $15M+ total revenue impact across AI/ML solutions\n"
        "- 15-20% reduction in forecast volatility\n"
        "- 30% improvement in planner efficiency\n"
        "- 8-12% MAPE improvement in forecasting models\n"
        "- Mentored 6-8 data scientists successfully\n"
        "- 10-15% campaign targeting improvement\n"
        "- 3-5% supply chain cost reductions"
    ),
    "biggest achievement": (
        "$15M+ revenue impact through AI/ML solutions, including forecast management framework "
        "that reduced volatility by 15-20% and improved efficiency by 30%."
    ),
    "accomplishments": (
        "Generated $15M+ in revenue impact, reduced forecast volatility by 15-20%, "
        "improved efficiency by 30%, and mentored 6-8 data scientists."
    ),

    # === SPECIALIZATIONS ===
    "specialization": (
        "Specializations:\n"
        "- Time-Series Forecasting & Demand Planning\n"
        "- Large Language Models & Generative AI\n"
        "- MLOps & Cloud-Native Architectures\n"
        "- Customer Analytics & Segmentation\n"
        "- Pricing & Promotional Optimization"
    ),
    "expertise": (
        "Expertise in AI/ML, GCP, time-series forecasting, LLMs, GenAI, MLOps, customer analytics, and optimization"
    ),
    
    # === LOCATION ===
    "location": "Mumbai, India",
    "where is pardeep based": "Mumbai, India",
    "where is he located": "Mumbai, India (works at General Mills India)",
    "city": "Mumbai",
}
