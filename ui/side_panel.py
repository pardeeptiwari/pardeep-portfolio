import streamlit as st
from pathlib import Path


def side_page(base_dir: Path):
    """Display Pardeep's profile information in the sidebar"""
    
    # Profile photo or initials
    img_path = base_dir / "assets" / "images" / "pardeep.jpeg"
    if img_path.exists():
        st.image(str(img_path), width=150)
    else:
        # Fallback initials
        st.markdown(
            """
            <div style="
                width: 150px;
                height: 150px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 60px;
                font-weight: bold;
                margin: 0 auto 20px;
            ">
                PT
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Contact information
    st.markdown("""
    <div style="text-align: center; margin-top: 10px;">
        <h2 style="color: var(--text-color);">Pardeep Tiwari</h2>
        <p style="font-size: 1.1em; color: #667eea; font-weight: 600;">Senior Data Scientist</p>
        <p style="color: #718096;">15+ Years Experience</p>
        <hr style="margin: 20px 0; opacity: 0.3;">
        <div style="text-align: left; max-width: 300px; margin: 0 auto;">
            <p style="margin: 10px 0;">📧 <a href="mailto:pardeep.tiwari@live.com" style="color: #4A90E2; text-decoration: none;">pardeep.tiwari@live.com</a></p>
            <p style="margin: 10px 0;">📞 <a href="tel:+918527661324" style="color: #4A90E2; text-decoration: none;">+91-8527661324</a></p>
            <p style="margin: 10px 0;">💼 <a href="https://www.linkedin.com/in/pardeeptiwari/" target="_blank" style="color: #4A90E2; text-decoration: none;">LinkedIn Profile</a></p>
            <p style="margin: 10px 0;">📍 Mumbai, India</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
