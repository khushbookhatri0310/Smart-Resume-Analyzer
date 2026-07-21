import pandas as pd
import re
def load_skills():
    df=pd.read_csv("data/skills.csv")
    skills=df["skill"].tolist()
    return skills
def extract_skills(text,skills):
    detected_skills=[]
    for skill in skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text.lower()):
            detected_skills.append(skill.strip())
    return detected_skills