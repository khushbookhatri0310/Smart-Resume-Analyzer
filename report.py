from reportlab.lib.pagesizes import letter
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
def generate_pdf_report(ats_score,
                        matched_skills,
                        missing_skills,
                        recommendations):
    doc = SimpleDocTemplate("ATS_Report.pdf")
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("SMART RESUME ANALYZER", styles["Title"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph(f"ATS Score: {ats_score}%", styles["Heading2"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Matched Skills", styles["Heading2"]))
    if matched_skills:
        for skill in matched_skills:
            story.append(Paragraph(f"• {skill}", styles["Normal"]))
    else:
        story.append(Paragraph("No matched skills found.", styles["Normal"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Missing Skills", styles["Heading2"]))
    if missing_skills:
        for skill in missing_skills:
            story.append(Paragraph(f"• {skill}", styles["Normal"]))
    else:
        story.append(Paragraph("No missing skills found.", styles["Normal"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Recommendations", styles["Heading2"]))
    if recommendations:
        for recommendation in recommendations:
            story.append(Paragraph(f"• {recommendation}", styles["Normal"]))
    else:
        story.append(Paragraph("No recommendations found.", styles["Normal"]))
    doc.build(story)