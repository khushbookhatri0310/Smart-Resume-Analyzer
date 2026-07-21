def generate_recommendations(missing_skills):
    recommendations = []
    suggestion_map = {
        "React": "Learn React and build at least one frontend project.",
        "Docker": "Learn Docker to understand containerization and deployment.",
        "AWS": "Learn AWS fundamentals and deploy a small application.",
        "Git": "Practice Git branching and upload projects on GitHub.",
        "SQL": "Practice SQL joins, indexing and database design.",
        "Python": "Improve Python by solving DSA and automation problems.",
        "Machine Learning": "Build one end-to-end Machine Learning project."
    }
    for skill in missing_skills:
        if skill in suggestion_map:
            recommendations.append(suggestion_map[skill])
        else:
            recommendations.append(f"Learn {skill}")
    return recommendations