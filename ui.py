import streamlit as st

from parser import extract_text_from_pdf
from utils import clean_text
from skills import load_skills, extract_skills
from ats import calculate_ats_score
from recommendation import generate_recommendations
from report import generate_pdf_report
from ai import (analyze_resume_with_ai, improve_resume_with_ai,generate_cover_letter, generate_interview_questions)

def initialize_session():

    defaults = {
        "analysis_done": False,
        "resume_text": "",
        "job_description": "",
        "detected_skills": [],
        "matched_skills": [],
        "missing_skills": [],
        "recommendations": [],
        "ats_score": 0,
        "ai_feedback": "",
        "improved_resume": "",
        "cover_letter": "",
        "interview_questions": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def analyze_resume(uploaded_file, job_description):

    extracted_text = extract_text_from_pdf(uploaded_file)

    cleaned_resume = clean_text(extracted_text)
    cleaned_jd = clean_text(job_description)

    skills = load_skills()

    detected_skills = extract_skills(cleaned_resume, skills)
    jd_skills = extract_skills(cleaned_jd, skills)

    matched_skills, missing_skills, ats_score = calculate_ats_score(
        detected_skills,
        jd_skills
    )

    recommendations = generate_recommendations(
        missing_skills
    )

    return (
        extracted_text,
        detected_skills,
        matched_skills,
        missing_skills,
        ats_score,
        recommendations
    )
def show_ui():

    initialize_session()

    st.title("📄 Smart Resume Analyzer")
    st.write("Welcome to your AI-powered Resume Analyzer!")
    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        uploaded_file = st.file_uploader(
            "Upload your Resume (PDF)",
            type=["pdf"]
        )

    with col2:
        st.subheader("Job Description")

        job_description = st.text_area(
            "Paste the job description here",
            height=250
        )

    analyze = st.button(
        "Analyze Resume",
        type="primary"
    )

    if uploaded_file and analyze:

        (
            extracted_text,
            detected_skills,
            matched_skills,
            missing_skills,
            ats_score,
            recommendations
        ) = analyze_resume(
            uploaded_file,
            job_description
        )

        st.session_state.analysis_done = True
        st.session_state.resume_text = extracted_text
        st.session_state.job_description = job_description
        st.session_state.detected_skills = detected_skills
        st.session_state.matched_skills = matched_skills
        st.session_state.missing_skills = missing_skills
        st.session_state.recommendations = recommendations
        st.session_state.ats_score = ats_score

        with st.spinner("AI is analyzing your resume..."):

            ai_feedback = analyze_resume_with_ai(
                extracted_text,
                job_description
            )

        st.session_state.ai_feedback = ai_feedback
    if st.session_state.analysis_done:

        st.divider()

        st.subheader("ATS Score")
        st.metric(
            "Overall ATS Score",
            f"{st.session_state.ats_score}%"
        )

        st.progress(int(st.session_state.ats_score))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            for skill in st.session_state.matched_skills:
                st.success(skill)

        with col2:
            st.subheader("❌ Missing Skills")
            for skill in st.session_state.missing_skills:
                st.error(skill)

        st.subheader("💡 Recommendations")
        for recommendation in st.session_state.recommendations:
            st.info(recommendation)

        tab1, tab2, tab3, tab4 = st.tabs([
                        "🤖 Resume Review",
                        "✨ Resume Improvement",
                        "📄 Cover Letter",
                        "🎤 Interview Questions"
                    ])
        with tab1: 
            st.subheader("🤖 AI Resume Review")
            st.markdown(st.session_state.ai_feedback)

        st.divider()

        with tab2: 
            if st.button("✨ Improve Resume"):

                with st.spinner("Improving your resume..."):

                    improved_resume = improve_resume_with_ai(
                        st.session_state.resume_text,
                        st.session_state.job_description
                    )

                st.session_state.improved_resume = improved_resume

            if st.session_state.improved_resume:

                st.subheader("✨ Improved Resume")

                st.markdown(
                    st.session_state.improved_resume
                )
        with tab3: 
            if st.button("📄 Generate Cover Letter"):

                with st.spinner("Generating Cover Letter..."):

                    cover_letter = generate_cover_letter(
                        st.session_state.resume_text,
                        st.session_state.job_description
                    )
                st.session_state.cover_letter = cover_letter

            if st.session_state.cover_letter:
                st.subheader("📄 AI Cover Letter")
                st.markdown(st.session_state.cover_letter)

        with tab4: 
            if st.button("🎤 Generate Interview Questions"):

                with st.spinner("Generating Interview Questions..."):

                    interview_questions = generate_interview_questions(
                        st.session_state.resume_text,
                        st.session_state.job_description
                    )

                st.session_state.interview_questions = interview_questions

            if st.session_state.interview_questions:
                st.subheader("🎤 AI Interview Questions")
                st.markdown(st.session_state.interview_questions)

        generate_pdf_report(
            st.session_state.ats_score,
            st.session_state.matched_skills,
            st.session_state.missing_skills,
            st.session_state.recommendations
        )

        with open("ATS_Report.pdf", "rb") as pdf_file:

            st.download_button(
                "📄 Download ATS Report",
                pdf_file,
                "ATS_Report.pdf",
                "application/pdf"
            )

        st.subheader("📊 Resume Summary")

        st.write(
            "Skills Detected:",
            len(st.session_state.detected_skills)
        )

        st.write(
            "ATS Score:",
            f"{st.session_state.ats_score}%"
        )