def get_recommendation(match_percentage, missing_skills):
    """Provides a tailored recommendation based on match quality."""
    if not missing_skills:
        return "Perfect match! Your profile aligns exceptionally well with this role."
    elif match_percentage >= 70:
        return "Strong candidate. Targeted upskilling in missing areas will make you a top pick."
    elif match_percentage >= 40:
        return "Good potential. Consider completing a project involving the missing skills."
    else:
        return "Significant gap identified. Focus on foundational skills before applying."