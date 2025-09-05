import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a model instance
model = genai.GenerativeModel("gemini-2.5-pro")

# Start a persistent chat session
chat_session = model.start_chat(history=[])

def get_tutor_response(question: str) -> str:
    """
    Interactive AI Tutor with memory.
    Maintains conversation like a teacher guiding step by step.
    """
    prompt = f"""
    You are an AI tutor for school kids.
    The student asked: {question}

    ✅ Your job:
    - Guide the student step by step like a kind teacher.
    - Use simple and encouraging language.
    - Do NOT directly give the final answer.
    - Ask follow-up hints to keep it interactive.
    - Keep your response under 5 lines and 500 characters.
    - Use bullet points and short paragraphs.
    - Format any code using Markdown triple backticks.
    - If the student asks for code, show only the code and a brief explanation (max 2 lines).

    Example style:
    "Okay, let’s start! What do you notice first? 
     Can you try breaking it down into smaller steps?"
    """
    try:
        response = chat_session.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Oops, something went wrong: {e}"