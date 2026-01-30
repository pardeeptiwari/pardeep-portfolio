import streamlit as st
from pathlib import Path


def render_contact(base_dir: Path):
    """Render Pardeep's contact information"""
    
    st.title("📞 Contact Information")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Get in Touch")
        st.markdown("")
        
        # Email
        st.markdown("### 📧 Email")
        st.markdown("[pardeep.tiwari@live.com](mailto:pardeep.tiwari@live.com)")
        st.markdown("")
        
        # Phone
        st.markdown("### 📱 Phone")
        st.markdown("[+91-8527661324](tel:+918527661324)")
        st.markdown("")
        
        # LinkedIn
        st.markdown("### 💼 LinkedIn")
        st.markdown("[linkedin.com/in/pardeeptiwari](https://www.linkedin.com/in/pardeeptiwari/)")
        st.markdown("")
        
        # Location
        st.markdown("### 📍 Location")
        st.write("Gurugram, India")
        st.markdown("")
        
        # Current Company
        st.markdown("### 🏢 Current Company")
        st.write("General Mills India Pvt Ltd")
    
    with col2:
        st.subheader("Professional Summary")
        st.markdown("")
        
        st.write("""
        I am a Senior Data Scientist with **15+ years of experience** building 
        production-grade AI/ML systems across **Retail and CPG industries**.
        """)
        
        st.write("""
        I specialize in the end-to-end ML lifecycle, from problem formulation to deployment 
        on **GCP (Vertex AI, BQML)**, with expertise in:
        """)
        
        st.markdown("""
        - **Forecasting & Optimization**: Time-series models, demand planning
        - **Generative AI & LLMs**: LangChain, RAG, Agentic AI
        - **MLOps & Cloud**: Docker, Kubernetes, CI/CD
        - **Team Leadership**: Mentoring data scientists, establishing best practices
        """)
        
        st.write("""
        I have delivered solutions generating **$15M+ revenue impact**, reduced 
        forecast volatility by **15-20%**, and improved operational efficiency 
        by **30%**.
        """)
        
        st.markdown("")
        st.info("💡 Feel free to reach out for opportunities, collaborations, or to discuss data science and AI/ML topics!")
    
    st.markdown("---")
    
    # Quick Stats
    st.subheader("📊 Quick Stats")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Experience", "15+ Years")
    
    with col2:
        st.metric("Revenue Impact", "$15M+")
    
    with col3:
        st.metric("Companies", "4")
    
    with col4:
        st.metric("Mentored", "6-8")
    
    with col5:
        st.metric("Location", "Mumbai")
    
    st.markdown("---")
    
    # Additional contact options
    st.subheader("📬 Preferred Contact Methods")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Best for:** General inquiries, opportunities  \n**Method:** Email  \n**Response:** Within 24-48 hours")
    
    with col2:
        st.info("**Best for:** Quick questions, urgent matters  \n**Method:** Phone/WhatsApp  \n**Response:** Same day")
    
    with col3:
        st.info("**Best for:** Professional networking  \n**Method:** LinkedIn  \n**Response:** Within 2-3 days")
