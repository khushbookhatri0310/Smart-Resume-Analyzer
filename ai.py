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
def improve_resume_with_ai(resume_text, job_description):

    prompt = f"""
You are an expert Resume Writer and ATS Expert.

Resume:
{resume_text}

Job Description:
{job_description}

Rewrite and improve the resume by:

1. Improving grammar.
2. Making bullet points more professional.
3. Adding ATS-friendly wording.
4. Keeping all information truthful.
5. Do NOT invent projects or skills.
6. Format the output section-wise.

Return only the improved resume.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are a professional career coach.

Using the resume and job description below, write a professional cover letter.

Resume:
{resume_text}

Job Description:
{job_description}

Instructions:
- Keep it within 300-400 words.
- Be professional.
- Highlight relevant skills.
- Do not invent experience or projects.
- End with a professional closing.

Return only the cover letter.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content