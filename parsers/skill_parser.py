from pathlib import Path
import re

def generic_parser(filepath , validskill):
    """
    Upgraded Parser using Regex: Matches whole words only to avoid 
    false positives like 'r' matching inside 'react'.
    """
    my_path = Path(filepath)
    if not my_path.exists() or not my_path.is_file():
        print("\nInvalid File! ")
        return []
    
    found_skills = []
    try:
        with open(my_path , mode="r" , encoding="utf-8") as f:
            skill_file = f.read().lower()
            for skill in validskill:
                clean_skill = skill.strip().lower()
                if not clean_skill:
                    continue

                pattern = r"\b" + re.escape(clean_skill) + r"\b"
                if re.search(pattern , skill_file):
                    found_skills.append(clean_skill)

                
            return list(dict.fromkeys(found_skills))
    except Exception as e:
        print(f"\nError : {e}")
        return []

