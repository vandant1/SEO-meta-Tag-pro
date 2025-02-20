import streamlit as st
from pathlib import Path

def inject_custom_css():
    css_file = Path(__file__).parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def inject_custom_js():
    js_file = Path(__file__).parent / "assets" / "main.js"
    with open(js_file) as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

def generate_meta_tags(title, description, url, keywords):
    meta_tags = f"""<!-- SEO Meta Tags -->
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">"""
    return meta_tags

# App Configuration
st.set_page_config(
    page_title="SEO Meta Tag Generator Pro",
    layout="wide",
    page_icon="🚀",
    initial_sidebar_state="expanded"
)

# Inject custom assets
inject_custom_css()
inject_custom_js()

# Main Content
with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("🚀 SEO Meta Tag Generator Pro")
    st.markdown("Craft perfect SEO meta tags with real-time previews & expert guidance")
    st.markdown('</div>', unsafe_allow_html=True)

# Split layout
col1, col2 = st.columns([3, 2])

with col1:
    # User Inputs
    with st.form("meta_form"):
        title = st.text_input(
            "Page Title *", 
            "My Awesome Website",
            help="Ideal length: 50-60 characters",
            max_chars=60
        )
        
        description = st.text_area(
            "Meta Description *", 
            "This is an example description that will appear in search engines.",
            help="Ideal length: 150-160 characters",
            max_chars=160
        )
        
        url = st.text_input(
            "Page URL *", 
            "https://example.com",
            help="Full canonical URL of the page"
        )
        
        keywords = st.text_input(
            "Keywords (comma-separated)", 
            "SEO, Meta Tags, Web Optimization",
            help="Main keywords for the page content"
        )
        
        submitted = st.form_submit_button("✨ Generate Meta Tags")

# Results Section
if submitted:
    with col1:
        meta_tags = generate_meta_tags(title, description, url, keywords)
        
        # Meta Tags Output
        st.markdown("### 📋 Generated Meta Tags")
        st.markdown(f'<div class="code-block"><button onclick="copyToClipboard(`{meta_tags}`)" class="copy-btn">Copy</button><code>{meta_tags}</code></div>', 
                    unsafe_allow_html=True)
        
        # Live Previews
        st.markdown("### 🔍 Live Previews")
        
        # Google Preview
        with st.expander("Google Search Preview", expanded=True):
            st.markdown(f"""
            <div class="preview-card google-preview">
                <h3 style="color: #1a0dab; margin: 0;">{title[:60]}{'...' if len(title)>60 else ''}</h3>
                <p style="color: #006621; margin: 0.2rem 0;">{url}</p>
                <p style="color: #545454; margin: 0;">{description[:160]}{'...' if len(description)>160 else ''}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Social Media Preview
        with st.expander("Social Media Preview"):
            st.markdown(f"""
            <div class="preview-card social-preview">
                <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem;">
                    <h3 style="margin: 0 0 0.5rem 0;">{title[:60]}{'...' if len(title)>60 else ''}</h3>
                    <p style="margin: 0 0 0.5rem 0; color: #666;">{description[:160]}{'...' if len(description)>160 else ''}</p>
                    <p style="margin: 0; color: #666; font-size: 0.9em;">{url}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Right Column - Features & Upsells
with col2:
    st.markdown("### 📌 Pro Tips")
    st.markdown("""
    - 🔍 Keep titles under 60 characters
    - ✍️ Write compelling, action-oriented descriptions
    - 🎯 Focus on 3-5 primary keywords
    - 🔗 Use absolute URLs for better indexing
    """)
    
    st.markdown("---")
    
    # SEO Analysis
    with st.expander("🔎 SEO Analysis", expanded=True):
        title_len = len(title)
        desc_len = len(description)
        
        st.metric("Title Length", f"{title_len}/60", 
                  "Perfect ✅" if 50 <= title_len <= 60 else 
                  "Too Short ⚠️" if title_len < 50 else "Too Long ⚠️")
        
        st.metric("Description Length", f"{desc_len}/160", 
                  "Perfect ✅" if 150 <= desc_len <= 160 else 
                  "Too Short ⚠️" if desc_len < 150 else "Too Long ⚠️")
    
    # Monetization Section
    st.sidebar.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.sidebar.markdown("## 🚀 Go Premium!")