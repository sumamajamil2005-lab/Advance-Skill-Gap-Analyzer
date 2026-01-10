def get_skill_level(match_percentage):
    """Categorizes the candidate's readiness level."""
    if match_percentage >= 80:
        return "Advanced / Job-Ready"
    elif match_percentage >= 50:
        return "Intermediate / Competitive"
    else:
        return "Beginner / Developing"