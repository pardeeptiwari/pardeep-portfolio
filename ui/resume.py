import streamlit as st
from pathlib import Path


def render_resume(base_dir: Path):
    """Render Pardeep's resume/skills section"""
    
    st.title("📄 Resume & Technical Skills")
    st.markdown("---")
    
    # Technical Skills Section
    st.header("💻 Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Languages & Tools")
        st.markdown("""
        - **Programming**: Python, PySpark, SQL, SAS
        - **Visualization**: Tableau, Looker
        - **Analytics**: Adobe Omniture (Site Catalyst)
        - **Big Data**: Hadoop, PySpark
        - **MS Office**: Excel (VBA macros)
        """)
        
        st.subheader("ML/AI Expertise")
        st.markdown("""
        - **Machine Learning**: Supervised & Unsupervised
        - **Deep Learning**: Neural Networks
        - **NLP**: Natural Language Processing
        - **Time-Series**: Forecasting Models
        - **Techniques**: Clustering, Classification, Regression
        - **Models**: XGBoost, Random Forest, LightGBM
        """)
        
        st.subheader("Advanced AI")
        st.markdown("""
        - **Transformers**: Modern architectures
        - **LLMs**: Large Language Models
        - **Generative AI**: GPT-based applications
        - **Agentic AI**: Autonomous systems
        """)
    
    with col2:
        st.subheader("Cloud & Platforms")
        st.markdown("""
        - **Google Cloud Platform (GCP)**
        - **Vertex AI**: ML model training & deployment
        - **BigQuery ML (BQML)**: Large-scale analytics
        """)
        
        st.subheader("MLOps & Deployment")
        st.markdown("""
        - **Containerization**: Docker
        - **Orchestration**: Kubernetes
        - **Model Packaging**: Production deployment
        - **CI/CD**: Continuous integration for ML
        - **Monitoring**: Model performance tracking
        - **Governance**: ML frameworks & policies
        """)
        
        st.subheader("Frameworks & Libraries")
        st.markdown("""
        - **LangChain**: LLM application development
        - **LangGraph**: Graph-based LLM workflows
        - **RAG**: Retrieval-Augmented Generation
        - **scikit-learn**: ML modeling
        - **pandas**: Data manipulation
        - **NumPy**: Numerical computing
        """)
    
    st.markdown("---")
    
    # Education Section
    st.header("🎓 Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **M.Tech**  
        Artificial Intelligence and Machine Learning  
        **Indian Institute of Technology (IIT), Jammu**  
        June 2023 – June 2025  
        **CGPA: 8.89/10** ⭐
        """)
    
    with col2:
        st.info("""
        **B.Tech**  
        Electronics & Communication Engineering  
        **Lovely Professional University**  
        July 2007 – June 2010  
        **CGPA: 7.42/10**
        """)
    
    st.markdown("---")
    
    # Key Achievements
    st.header("🏆 Key Achievements")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Revenue Impact",
            value="$15M+",
            delta="Across all AI/ML solutions"
        )
    
    with col2:
        st.metric(
            label="Forecast Volatility",
            value="15-20%",
            delta="Reduction",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            label="Efficiency Gain",
            value="30%",
            delta="Planner productivity"
        )
    
    with col4:
        st.metric(
            label="Mentored",
            value="6-8",
            delta="Data Scientists"
        )
    
    st.markdown("---")
    
    # Business Skills
    st.header("💼 Business & Domain Expertise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - **Project Management**: Leading cross-functional teams
        - **Customer Insights**: Segmentation & behavior analysis
        - **Campaign Analysis**: A/B testing & optimization
        - **Clickstream Data Analysis**: User journey tracking
        - **Dashboarding**: Executive reporting & visualization
        """)
    
    with col2:
        st.markdown("""
        - **Pricing Optimization**: Elasticity modeling
        - **Demand Forecasting**: Supply chain planning
        - **Prescriptive Analytics**: Decision optimization
        - **Predictive Analytics**: Future trend analysis
        - **Stakeholder Communication**: Executive presentations
        """)
    
    st.markdown("---")
    
    # Additional certifications or achievements section
    st.header("📜 Notable Accomplishments")
    
    accomplishments = [
        "🎯 Generated $15M+ in total revenue impact through AI/ML solutions",
        "📊 Reduced forecast volatility by 15-20% in supply chain planning",
        "⚡ Improved operational efficiency by 30% through AI automation",
        "🎓 Achieved 8.89/10 CGPA in M.Tech from prestigious IIT Jammu",
        "👥 Successfully mentored 6-8 data scientists, building strong analytics teams",
        "🏆 Delivered 8-12% MAPE improvement over baseline forecasting methods",
        "💰 Contributed to $5M+ annual revenue impact at Dunnhumby",
        "📈 Improved campaign targeting effectiveness by 10-15%"
    ]
    
    for accomplishment in accomplishments:
        st.success(accomplishment)
