import re

def generic_Parser(filepath, valid_skills):
    """
    Upgraded Parser using Regex: Matches whole words only to avoid 
    false positives like 'r' matching inside 'react'.
    """
    found_skills = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().lower()

        for skill in valid_skills:
            clean_skill = skill.strip().lower()
            if not clean_skill:
                continue

            pattern = r'\b' + re.escape(clean_skill) + r'\b'
            
            if re.search(pattern, content):
                found_skills.append(clean_skill)

        return list(set(found_skills))

    except FileNotFoundError:
        print(f"Error: Resume file not found at {filepath}")
        return []
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return []