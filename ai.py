import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume_with_ai(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume and provide:

1. Overall Resume Feedback
2. Strengths
3. Weaknesses
4. Missing Skills
5. ATS Improvement Tips

Keep the response professional and well formatted.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content