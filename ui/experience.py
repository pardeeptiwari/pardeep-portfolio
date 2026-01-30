import streamlit as st
from pathlib import Path


def render_experience(base_dir: Path):
    """Render Pardeep's professional experience"""
    
    st.title("💼 Professional Experience")
    st.markdown("---")
    
    # Experience 1: General Mills
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <h2 style="color: #667eea;">Senior Data Scientist</h2>
        <h3 style="color: #4a5568;">General Mills India Pvt Ltd</h3>
        <p style="color: #718096; font-style: italic;">July 2022 – Present | Mumbai, India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Achievements:**
    - 🚀 Architected and deployed AI-driven forecast exception management framework on GCP, reducing forecast volatility by **15–20%** and improving planner efficiency by **30%** across global markets
    - 📈 Developed production time-series forecasting models achieving **8–12% MAPE improvement** over statistical baselines, impacting **$10M+ annual revenue**
    - 💡 Built interpretable ML scorecards and insight layers for C-suite, driving data-informed decisions on range optimization and promotional strategies
    - ⚙️ Established MLOps practices including model monitoring, retraining pipelines, and governance frameworks
    - 👥 Mentored **6–8 data scientists**, accelerating onboarding by **25%** and standardizing delivery practices
    """)
    
    st.markdown("---")
    
    # Experience 2: Dunnhumby
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <h2 style="color: #667eea;">Lead Applied Data Scientist</h2>
        <h3 style="color: #4a5568;">Dunnhumby IT Services Pvt Ltd</h3>
        <p style="color: #718096; font-style: italic;">May 2015 – July 2022 | Gurugram, India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Achievements:**
    - 🏢 Led development of advanced ML solutions for **Fortune 500 retail clients**, including customer analytics, demand forecasting, and pricing elasticity models
    - 💰 Delivered pricing, assortment, and demand optimization solutions contributing to **2–4% margin uplift** and **$5M+ annual revenue impact**
    - 🎯 Improved campaign targeting effectiveness by **10–15%** over rule-based approaches through predictive modeling
    - 🤝 Collaborated with global stakeholders to translate business requirements into scalable analytics solutions
    
    **Notable Projects:**
    - **Customer Optimal Entry Point Targeting**: Led team of 4 using XGBoost and Random Forest to identify optimal customer targeting moments
    - **Front of Store Basket Missions**: Applied K-Means clustering and NMF to optimize customer experience
    - **Propensity Modeling**: Built models increasing redemption rates by **7%** post-implementation
    - **Customer Journey Tracking**: Analyzed clickstream data using Hive and Adobe Omniture for taxonomy optimization
    """)
    
    st.markdown("---")
    
    # Experience 3: Inductis
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <h2 style="color: #667eea;">Senior Business Analyst</h2>
        <h3 style="color: #4a5568;">Inductis (India) Pvt Ltd</h3>
        <p style="color: #718096; font-style: italic;">June 2012 – May 2015 | Gurugram, India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Achievements:**
    - 📊 Delivered data-driven retail and supply chain solutions, enabling **3–5% cost reductions** through improved demand planning
    - 🔬 Applied statistical modeling and ML techniques to solve complex business problems
    - 📈 Supported client engagements through analysis and executive presentations
    - 💼 Improved collection process efficiency by **3x** through customer segmentation
    - 📧 Reduced email volumes by **~20%** through trend analysis and recommendations
    """)
    
    st.markdown("---")
    
    # Experience 4: TCS
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <h2 style="color: #667eea;">Assistant System Engineer</h2>
        <h3 style="color: #4a5568;">Tata Consultancy Services Pvt Ltd</h3>
        <p style="color: #718096; font-style: italic;">September 2010 – June 2012 | Gurugram, India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Key Achievements:**
    - ⚡ Optimized data management and reporting processes, reducing manual effort by **40%**
    - 📊 Improved data availability for operational teams
    - 🔧 Streamlined workflows and automated routine tasks
    """)
