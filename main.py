import streamlit as st
from chatbot import get_bot_response
from roadmap_reader import extract_text_from_image
import re
import fitz  # PyMuPDF
from resume_analyzer import analyze_resume  

st.set_page_config(page_title="🧠 AI Career Coach", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .chat-bubble {
        background-color: #e1eaff;
        padding: 12px;
        border-radius: 12px;
        margin: 5px 0;
    }
    .chat-bubble.bot {
        background-color: #d1f0d1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>🚀 AI Career Coach</h1>", 
    unsafe_allow_html=True
)


tab1, tab2, tab3 = st.tabs(["📘 Overview", "🗺️ Roadmap", "💬 Chatbot"])

domains = {
    "Android": ["kotlin", "java", "android studio"],
    "Android(Flutter)": ["flutter", "dart"],
    "Android(React Native)": ["react native", "expo"],
    "Backend": ["node", "django", "spring", "express", "api", "php"],
    "Blockchain": ["web3", "solidity", "smart contract", "ethereum"],
    "Cybersecurity": ["nmap", "burp", "vulnerability", "kali", "owasp"],
    "Data Analyst": ["excel", "sql", "tableau", "powerbi", "dashboards"],
    "Data Science": ["python", "pandas", "numpy", "ml", "sklearn", "tensorflow"],
    "DevOps": ["docker", "kubernetes", "ci/cd", "jenkins", "aws", "linux"],
    "Frontend": ["html", "css", "javascript", "react", "tailwind", "nextjs"],
    "Full Stack": ["mern", "mevn", "full stack", "frontend", "backend"],
    "IOS": ["swift", "xcode"],
    "MLOps": ["dvc", "mlflow", "deployment", "pipeline", "cloud"]
}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_domain" not in st.session_state:
    st.session_state.selected_domain = "Frontend"

with tab1:
    st.markdown("### 📂 Upload Resume (PDF)")
    uploaded_file = st.file_uploader("Drop your resume here", type=["pdf"])

    analysis_result = None

    if uploaded_file:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        resume_text = " ".join([page.get_text().lower() for page in doc])

        # Resume analysis
        analysis_result = analyze_resume(resume_text)

        # Domain detection
        match_scores = {}
        for domain, keywords in domains.items():
            score = sum(1 for kw in keywords if kw in resume_text)
            match_scores[domain] = score

        best_match = max(match_scores, key=match_scores.get)
        st.session_state.selected_domain = best_match

        st.success(f"✅ Detected best-matched domain: **{best_match}**")

        # Display ATS Score and feedback
        st.markdown(f"### 📊 ATS Score: **{analysis_result['ats_score']} / 100**")

        if analysis_result['strengths']:
            st.markdown("#### ✅ Strengths:")
            for s in analysis_result['strengths']:
                st.markdown(f"- {s}")

        if analysis_result['improvements']:
            st.markdown("#### ⚠️ Improvements:")
            for imp in analysis_result['improvements']:
                st.markdown(f"- {imp}")

    st.markdown("### 🔍 Or Select Domain Manually")
    st.session_state.selected_domain = st.selectbox(
        "Choose domain:",
        list(domains.keys()),
        index=list(domains.keys()).index(st.session_state.selected_domain)
    )

with tab2:
    domain = st.session_state.selected_domain
    safe_filename = re.sub(r"[()]", "", domain.lower().replace(" ", "_"))
    img_path = f"assets/{safe_filename}.png"

    try:
        st.image(img_path, use_container_width=True, caption=f"{domain} Roadmap (Credit: roadmap.sh😁)")
        roadmap_text = extract_text_from_image(img_path)
        
    except Exception as e:
        st.warning(f"❌ Roadmap image missing or unreadable.\nError: {e}")
        roadmap_text = ""

with tab3:
    st.markdown("### 💬 Ask Anything Based on the Roadmap")

    user_input = st.text_input("Your question:")
    if user_input and roadmap_text:
        response = get_bot_response(st.session_state.selected_domain, user_input, roadmap_text)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("CoachBot", response))

    for sender, msg in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {msg}")
