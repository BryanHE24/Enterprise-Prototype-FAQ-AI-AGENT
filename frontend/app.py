import streamlit as st
import requests
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Enterprise FAQ AI Agent",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        
        .main {
            background-color: #121621;
            color: #ffffff;
            padding: 0;
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }
        
        h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput {
            color: #ffffff;
        }
        
        .stTextInput > div > div > input {
            background-color: #1a1f2f;
            border: 1px solid #2d3649;
            border-radius: 6px;
            padding: 1rem;
            color: #ffffff;
            font-size: 1rem;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #8891a7;
        }
        
        .stButton > button {
            background-color: #1e4285;
            color: white;
            font-weight: 600;
            padding: 0.65rem 1.5rem;
            border-radius: 6px;
            border: none;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            background-color: #2756a9;
        }
        
        .title {
            color: #3b82f6;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: #8891a7;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        
        .info-box {
            background-color: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 6px;
            padding: 1rem;
            color: #8891a7;
            margin: 1.5rem 0;
        }
        
        .info-icon {
            color: #3b82f6;
            margin-right: 0.5rem;
        }
        
        .footer {
            color: #8891a7;
            font-size: 0.85rem;
            text-align: center;
            padding: 2rem 0 1rem 0;
        }
        
        .nav-tabs {
            display: flex;
            border-bottom: 1px solid #2d3649;
            margin-bottom: 1.5rem;
            padding-bottom: 0;
        }
        
        .nav-tab {
            color: #8891a7;
            padding: 0.75rem 1.25rem;
            text-decoration: none;
            margin-right: 0.5rem;
            border-bottom: 2px solid transparent;
            font-size: 0.95rem;
            transition: all 0.15s ease;
        }
        
        .nav-tab.active {
            color: #3b82f6;
            border-bottom: 2px solid #3b82f6;
        }
        
        .question-pill {
            background-color: #1a1f2f;
            border: 1px solid #2d3649;
            color: #ffffff;
            padding: 0.5rem 1rem;
            border-radius: 100px;
            font-size: 0.85rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            display: inline-block;
            cursor: pointer;
        }
        
        .question-pill:hover {
            background-color: #2d3649;
        }
        
        .response-container {
            background-color: #1a1f2f;
            border-radius: 6px;
            padding: 1.5rem;
            margin-top: 1.5rem;
            border-left: 3px solid #3b82f6;
        }
        
        .response-header {
            color: #ffffff;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .response-content {
            color: #e2e8f0;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        .meta-info {
            display: flex;
            justify-content: space-between;
            color: #8891a7;
            font-size: 0.8rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #2d3649;
        }
        
        .divider {
            height: 1px;
            background-color: #2d3649;
            margin: 2rem 0;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Adjust header spacing */
        .stHeadingContainer {
            padding-bottom: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App container
st.markdown('<div class="title">Enterprise FAQ AI Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get instant answers to your most common questions</div>', unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Navigation tabs
st.markdown("""
    <div class="nav-tabs">
        <a href="#" class="nav-tab active">General</a>
    </div>
""", unsafe_allow_html=True)

# Info box
st.markdown("""
    <div class="info-box">
        <span class="info-icon">ℹ️</span>
        Our AI agent is trained on our complete knowledge base to provide you with accurate answers instantly. 
        Ask any question about our products, services, or support issues.
    </div>
""", unsafe_allow_html=True)

# Question input section
st.subheader("Ask a Question")
question = st.text_input("", placeholder="e.g. How do I reset my password?")

# Quick questions
st.markdown("""
    <div style="margin-top: 1rem;">
        <div class="question-pill">How do I reset my password?</div>
        <div class="question-pill">What is your return policy?</div>
        <div class="question-pill">How long does shipping take?</div>
    </div>
""", unsafe_allow_html=True)

# Button
col1, col2, col3 = st.columns([3, 3, 2])
with col3:
    submit = st.button("Get Answer")

# Response section
if submit and question:
    with st.spinner("Finding answer..."):
        try:
            # Simulating API request
            response = requests.post(
                "http://localhost:5000/ask", 
                json={"question": question}
            )
            
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer provided")
                confidence = response.json().get("confidence", 1)
                category = response.json().get("category", "General")
                
                # Display response
                st.markdown(f"""
                    <div class="response-container">
                        <div class="response-header">Answer</div>
                        <div class="response-content">{answer}</div>
                        <div class="meta-info">
                            <div>Confidence: {int(confidence * 100)}%</div>
                            <div>Category: {category}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Display related questions
                st.markdown('<p style="margin-top:1.5rem; font-weight:500; color:#ffffff;">Related Questions</p>', unsafe_allow_html=True)
                st.markdown("""
                    <div>
                        <div class="question-pill">How do I change my email address?</div>
                        <div class="question-pill">What security measures protect my account?</div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Unable to process your request. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
current_year = datetime.now().year
st.markdown(f"""
    <div class="footer">
        Enterprise FAQ AI Agent Prototype • {current_year}<br>
        
    </div>
""", unsafe_allow_html=True)