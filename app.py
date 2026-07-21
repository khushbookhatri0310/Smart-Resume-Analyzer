import streamlit as st
from parser import extract_text_from_pdf
from utils import clean_text
from skills import load_skills, extract_skills
from ats import calculate_ats_score
from recommendation import generate_recommendations
from report import generate_pdf_report
# Page configuration
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
# Title
st.title("📄 Smart Resume Analyzer")
# Welcome message
st.write("Welcome to your AI-powered Resume Analyzer!")
# Divider
st.divider()
# Upload section
col1, col2 = st.columns([1, 2])
with col1:
    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )
with col2:
    st.subheader("Job Description")
    job_description = st.text_area("Paste the job description here",
                                height=250
    )
analyze=st.button("Analyze Resume")
if uploaded_file and analyze:
    st.success("✅ Resume uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    extracted_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(extracted_text)
    cleaned_job_description = clean_text(job_description)
    skills=load_skills()
    detected_skills=extract_skills(cleaned_text,skills)
    job_detected_skills=extract_skills(cleaned_job_description,skills)
    matched_skills, missing_skills, ats_score = calculate_ats_score(detected_skills, job_detected_skills)
    st.write("Resume Skills:",detected_skills)
    st.write("Job Skills:",job_detected_skills)
    st.subheader("ATS Score")
    st.metric(label="Overall ATS Score",
               value=f"{ats_score}%")
    st.progress(int(ats_score))
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Matched Skills")
        for skill in matched_skills:
            st.success(skill)
    with col2:
        st.subheader("Missing Skills")
        for skill in missing_skills:
            st.error(skill)
    st.subheader("Matched Skills")
    st.write(matched_skills)
    st.subheader("Missing Skills")
    st.write(missing_skills)
    recommendations = generate_recommendations(missing_skills)
    st.subheader("Recommendations")
    for recommendation in recommendations:
        st.info(recommendation)
    generate_pdf_report(ats_score,
                        matched_skills,
                        missing_skills,
                        recommendations)
    with open("ATS_Report.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download ATS Report",
            data=pdf_file,
            file_name="ATS_Report.pdf",
            mime="application/pdf"
        )
    with st.container():
        st.subheader("Resume Summary")
        st.write(" File Name:", uploaded_file.name)
        st.write(" Skills Detected:", len(detected_skills))
        st.write(" ATS Score:", f"{ats_score}%")