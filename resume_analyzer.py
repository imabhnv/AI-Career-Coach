import re

def analyze_resume(text: str) -> dict:
    """
    Simple ATS-like analysis of resume text.
    Returns:
      {
        'ats_score': int (0-100),
        'strengths': list of strings,
        'improvements': list of strings
      }
    """

    text = text.lower()

    # Basic scoring parameters
    keywords = [
        'python', 'java', 'c++', 'machine learning', 'data science', 'sql', 'docker', 'kubernetes',
        'react', 'node', 'aws', 'tensorflow', 'django', 'flask', 'git', 'linux', 'html', 'css', 'javascript'
    ]

    sections = ['education', 'experience', 'projects', 'skills', 'certifications', 'achievements']

    ats_score = 0
    strengths = []
    improvements = []

    # 1. Keyword density (max 40 points)
    found_keywords = [kw for kw in keywords if kw in text]
    keyword_score = min(len(found_keywords)*4, 40)
    ats_score += keyword_score
    if found_keywords:
        strengths.append(f"Strong skill keywords detected: {', '.join(found_keywords)}")
    else:
        improvements.append("Add relevant technical skills keywords to your resume.")

    # 2. Sections present (max 30 points)
    found_sections = [sec for sec in sections if sec in text]
    section_score = min(len(found_sections)*5, 30)
    ats_score += section_score
    missing_sections = [sec for sec in sections if sec not in found_sections]
    if missing_sections:
        improvements.append(f"Missing important sections: {', '.join(missing_sections)}")
    else:
        strengths.append("All key sections (Education, Experience, Projects, Skills, Certifications, Achievements) found.")

    # 3. Contact info presence (max 10 points)
    if re.search(r"\b(email|@|phone|contact)\b", text):
        ats_score += 10
        strengths.append("Contact information is present.")
    else:
        improvements.append("Add your contact details clearly.")

    # 4. Length check (max 10 points)
    word_count = len(text.split())
    if 300 <= word_count <= 1000:
        ats_score += 10
        strengths.append(f"Resume length looks good ({word_count} words).")
    elif word_count < 300:
        improvements.append("Resume is too short; add more details.")
    else:
        improvements.append("Resume is too long; keep it concise.")

    # 5. Formatting hints (max 10 points)
    # Simple heuristic: presence of bullet points or dashes
    if re.search(r"(\n\s*[-•*])", text):
        ats_score += 10
        strengths.append("Good use of bullet points for readability.")
    else:
        improvements.append("Use bullet points for better formatting and readability.")

    # Cap ATS score to 100 max
    ats_score = min(ats_score, 100)

    return {
        "ats_score": ats_score,
        "strengths": strengths,
        "improvements": improvements,
    }