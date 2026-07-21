def calculate_ats_score(resume_skills, job_skills):
    matched_skills = []
    missing_skills = []
    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_skills)) * 100
    return matched_skills, missing_skills, round(score, 2)