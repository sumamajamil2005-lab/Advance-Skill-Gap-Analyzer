from parsers.file_loader import File_Loader
from parsers.skill_parser import generic_Parser
from matcher.skill_matcher import skill_matcher
from writer.report_writer import Report_writer

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

def get_skill_level(match_percentage):
    """Categorizes the candidate's readiness level."""
    if match_percentage >= 80:
        return "Advanced / Job-Ready"
    elif match_percentage >= 50:
        return "Intermediate / Competitive"
    else:
        return "Beginner / Developing"

def main():
    # 1. Configuration & Loading
    SKILLS_FILE = "skills/skills_list.txt"
    RESUME_FILE = "data/resume.txt"
    JD_FILE = "data/job_description.txt"
    OUTPUT_FILE = "output/report.txt"

    # Load master skills from file
    valid_skills = File_Loader(SKILLS_FILE)

    # 2. Parsing
    # We pass valid_skills to ensure we only extract relevant keywords
    resume_skills = generic_Parser(RESUME_FILE, valid_skills)
    jd_skills = generic_Parser(JD_FILE, valid_skills)

    # 3. Matching Logic (Weighted)
    matched, missing, percentage = skill_matcher(resume_skills, jd_skills)

    # 4. Analysis
    level = get_skill_level(percentage)
    rec = get_recommendation(percentage, missing)

    # 5. Writing Report
    # Note: We now pass 'jd_skills' so the writer knows which ones are 'Primary'
    Report_writer(
        OUTPUT_FILE, 
        matched, 
        missing, 
        percentage, 
        level, 
        rec, 
        jd_skills
    )

    # 6. Console Output (Clean & Professional)
    print("\n\n\n\n" + "="*40)
    print("      SKILL GAP ANALYSIS COMPLETE")
    print("="*40)
    print(f"Match Score   : {percentage}%")
    print(f"Result        : {level}")
    print(f"Matched ({len(matched)}) : {', '.join(matched) if matched else 'None'}")
    print(f"Missing ({len(missing)}) : {', '.join(missing) if missing else 'None'}")
    print("-" * 40)
    print(f"Recommendation: {rec}")
    print(f"Detailed report saved to: {OUTPUT_FILE}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()