def Report_writer(file_path, matched, missing, percentage, level, recommendation, jd_skills):
    """
    Generates a professional text report of the skill gap analysis.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("==========================================\n")
            f.write("        SKILL GAP ANALYSIS REPORT          \n")
            f.write("==========================================\n\n")
            
            f.write(f"OVERALL MATCH: {percentage}%\n")
            f.write(f"CANDIDATE LEVEL: {level}\n")
            f.write(f"ADVICE: {recommendation}\n\n")
            
            f.write("--- ANALYSIS BREAKDOWN ---\n")
            
            # Matched Section
            if matched:
                f.write(f"✅ MATCHED SKILLS: {', '.join(matched)}\n")
            else:
                f.write("✅ MATCHED SKILLS: None\n")
                
            # Missing Section
            if missing:
                f.write(f"❌ MISSING SKILLS: {', '.join(missing)}\n")
            else:
                f.write("❌ MISSING SKILLS: None (All requirements met!)\n")
            
            f.write("\n--- JOB SPECIFIC SKILLS ---\n")
            # First 3 skills are consider as primary skills
            primary = jd_skills[:3]
            f.write(f"⭐ PRIMARY REQUIREMENTS: {', '.join(primary)}\n")

            f.write("\n------------------------------------------\n")
            f.write("PROFESSIONAL NOTES:\n")
            f.write("- Weighted matching used: Primary skills carry more weight.\n")
            f.write("- Ensure matched keywords appear in your project context.\n")
            f.write("==========================================\n")
            
    except Exception as e:
        print(f"Error writing report: {e}")