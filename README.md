
# 🧠 AI Career Coach 

A smart AI-powered web app built with Streamlit to help students and professionals:

- 📘 Learn about different tech domains  
- 🗺️ Get curated roadmap images  
- 💬 Chat with a domain-specific AI mentor  
- 📂 Analyze their resume and get ATS-based feedback

---

## 🚀 Features

### 🔍 Career Domain Selector
- Choose from multiple domains like:
  `Data Science`, `Backend`, `Frontend`, `Cybersecurity`, etc.

### 🗺️ Roadmap Viewer
- Visual roadmap images auto-loaded for each domain  
- Extracted text used for chatbot context

### 💬 AI Career Chatbot
- Ask domain-specific career questions  
- Powered by **Gemini Pro** using LangChain integration  
- Context-aware replies based on roadmap content only

### 📂 Resume Analyzer (ATS)
- Upload your PDF resume  
- Get:
  - **ATS Score (0–100)**
  - ✅ Strengths in your resume
  - ⚠️ Improvement Suggestions
- Auto-detects best-matching domain based on resume content

---

## 📁 Folder Structure

```
AI_Career_Coach/
├── assets/                  # Roadmap images (named like backend.png, data_science.png)
├── chatbot.py              # Gemini-based chatbot logic
├── resume_analyzer.py      # ATS resume scoring engine
├── roadmap_reader.py       # OCR-based roadmap image reader
├── main.py                 # Streamlit frontend app
└── README.md
```

---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-career-coach.git
cd ai-career-coach
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pymupdf google-generativeai langchain langchain-community
```

### 3. Add Roadmap Images

Place roadmap PNGs in the `assets/` folder with these names:

- `frontend.png`
- `backend.png`
- `data_science.png`
- `cybersecurity.png`
- etc.

### 4. Add your Gemini API Key

Create a `.env` file or configure your key in `chatbot.py` like:

```python
import os
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📸 Screenshots

| Feature            | Preview                    |
|--------------------|----------------------------|
| Domain Selector    | ✅ Dropdown                |
| Roadmap Viewer     | 🗺️ Image with OCR text     |
| Resume Analyzer    | 📊 ATS score + tips        |
| AI Chatbot         | 💬 Text chat based on roadmap |

---

## 🧠 Tech Stack

- **Streamlit** – UI & frontend
- **LangChain + Gemini** – AI chat interface
- **PyMuPDF** – Resume text extraction
- **Tesseract (optional)** – OCR if you want to use image-to-text
- **Python** – Backend logic

---

## 🙌 Credits

- Roadmaps from [roadmap.sh](https://roadmap.sh/)
- Gemini by Google
- OCR via PyMuPDF

---

## 📃 License

MIT License – free to use, improve, and share ✨

---

## 🔮 Future Plans

- Resume-to-JD Matching
- Internship Suggestion API
- Auto-Generated Personalized Roadmap