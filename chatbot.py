from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="AIzaSyBz830luF6uDWgqht5ngyw34l-KWNxUXr0",
    temperature=0.4
)

prompt = PromptTemplate(
    input_variables=["domain", "query", "roadmap_text"],
    template="""
You are a professional AI career advisor.

Below is a roadmap for the domain: {domain}
Roadmap Content:
--------------------
{roadmap_text}
--------------------

Your task is to answer student queries in detail long

✅ If the user asks you to "explain the domain" — give a **explanation of the domain (eg.Android Development, Data Science etc.) upon which the roadmap is based on in detail **, general theory.
otherwise use your knowledge to help student
✅ If user asks for steps, tools, path — derive it from the roadmap content and add detail.

❌ Do NOT guess or add anything not visible in the roadmap.
❌ If you can't find the answer in the roadmap, politely say so.

Question: {query}
"""
)

chain = prompt | llm

def get_bot_response(domain, query, roadmap_text):
    try:
        result = chain.invoke({
            "domain": domain,
            "query": query,
            "roadmap_text": roadmap_text
        })
        return result.content.strip()
    except Exception as e:
        return f"Gemini Error: {e}"
