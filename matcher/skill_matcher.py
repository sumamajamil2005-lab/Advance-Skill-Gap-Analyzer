from matcher.ai_matcher import is_semantic_match ,  get_embeddings

# Dict mappings :
# 1:
_SKILL_NORMALIZATION = {
    "python": "python",
    "py": "python",
    "javascript": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "ts": "typescript",
    "java": "java",
    "c++": "c++",
    "c#": "c#",
    "kotlin": "kotlin",
    "swift": "swift",
    "php": "php",
    "r": "r",

    "django": "django",
    "flask": "flask",
    "fastapi": "fastapi",
    "drf": "django rest framework",
    "django rest framework": "django rest framework",
    "spring boot": "spring boot",
    "nodejs": "node.js",
    "node.js": "node.js",
    "node": "node.js",

    "react": "react",
    "reactjs": "react",
    "react.js": "react",
    "angular": "angular",
    "vue.js": "vue.js",
    "html": "html",
    "css": "css",
    "sass": "sass",
    "less": "less",

    "aws": "aws",
    "amazon web services": "aws",
    "amazon platform": "aws",
    "gcp" : "google cloud platform",
    "google cloud platform": "gcp",
    "azure": "azure",
    "microsoft azure": "azure",
    "microsoft cloud": "azure",

    "docker": "docker",
    "dockerization": "docker",
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "container orchestration": "kubernetes",
    "helm charts": "kubernetes",
    "jenkins": "jenkins",
    "ci/cd": "ci/cd",
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",
    "automated deployment": "ci/cd",
    "automated deployment processes": "ci/cd",
    "git": "git",
    "github": "git",
    "version control": "git",
    "terraform": "terraform",
    "infrastructure as code": "terraform",
    "iac": "terraform",
    "ansible": "ansible",

    # --- Databases (Specific vs Generic) ---
    "sql": "sql",
    "structured query language": "sql",
    "rdbms": "sql",
    "relational databases": "sql",
    "mysql": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "mongo": "mongodb",
    "nosql": "nosql",
    "redis": "redis",
    "dynamodb": "dynamodb",
    "cassandra": "cassandra",

    "machine learning": "ml",
    "ml": "ml",
    "artificial intelligence": "ai",
    "ai": "ai",
    "deep learning": "dl",
    "dl": "dl",
    "nlp": "nlp",
    "natural language processing": "nlp",
    "computer vision": "cv",
    "cv": "cv",
    "genai": "genai",
    "generative ai": "genai",
    "pandas": "pandas",
    "numpy": "numpy",
    "scikit-learn": "scikit-learn",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",

    "microservices": "microservices",
    "independent services": "microservices",
    "small independent services": "microservices",
    "rest api": "rest api",
    "restapi": "rest api",
    "restapis": "rest api",
    "restful api": "rest api",
    "restful apis": "rest api",
    "graphql": "graphql",
    "apache kafka": "kafka",
    "data streaming": "kafka",
    "linux": "linux",
    "ubuntu": "linux"
}

# 2:

_IMPLIED_SKILLS = {
    "django": ["python", "sql", "rest api"],
    "flask": ["python", "rest api"],
    "fastapi": ["python", "rest api"],
    "react": ["javascript", "html", "css"],
    "kubernetes": ["docker", "linux"],
    "postgresql": ["sql", "postgresql"],
    "mongodb": ["nosql"]
}






# 3:

SKILL_FAMILIES = {
    "python_web": ["django", "flask", "fastapi", "pyramid"],
    "frontend_js": ["react", "vue", "angular", "svelte"],
    "sql_db": ["postgresql", "mysql", "sqlite", "oracle"],
    "nosql_db": ["mongodb", "cassandra", "redis", "couchdb"],
    "communication": [
        "communication", "team player", "collaboration", 
        "soft skills", "interpersonal", "presentation", 
        "verbal", "written", "problem-solving"
    ]
}





def _normalize(skill):
    skill = skill.strip().lower()
    return _SKILL_NORMALIZATION.get(skill , skill)





def expand_skills(extracted_skills):
    expanded = []
    for s in extracted_skills:
        if s not in expanded:
            expanded.append(s)
            
    for skill in extracted_skills:
        skill_lower = skill.lower()
        if skill_lower in _IMPLIED_SKILLS:
            for implied in _IMPLIED_SKILLS[skill_lower]:
                if implied not in expanded:
                    expanded.append(implied)
                    
    return expanded





def get_partial_match_score(jd_skill, resume_skills):
    jd_skill = jd_skill.lower()
    for family, members in SKILL_FAMILIES.items():
        if jd_skill in members:
            for member in members:
                if member in resume_skills:
                    return float(0.5) 
    return float(0)





def skill_cleaner(skills_list , compare_list):
    if not skills_list:
        return None
    
    unique_skills = []
    if skills_list:
            for skill in skills_list:
                cleaned_skill = _SKILL_NORMALIZATION.get(skill.lower() , skill.lower())
                if skill not in unique_skills and _SKILL_NORMALIZATION.get(skill.lower()) not in unique_skills:
                    unique_skills.append(cleaned_skill)
                    continue
                else:
                    continue

    final_skills = [s for s in unique_skills if s not in compare_list]
    return final_skills











def skill_matcher(jd_skills , resume_skills):
    if not jd_skills or not resume_skills:
        print("\nInvalid input! ")
        return []
    
    missing_skills = []
    matched_skill = []
    earned_points = 0
    total_points = 0
    
    normalized_resume = [_normalize(s) for s in resume_skills]
    normalized_jd = [_normalize(j) for j in jd_skills]
    exp_res = expand_skills(normalized_resume)

    res_emb= get_embeddings(exp_res)
    jd_emb = get_embeddings(normalized_jd)

    lower_resume = [s.lower() for s in resume_skills]

    
    for index , skill in enumerate(jd_skills):
        is_required = True if index < 4 else False
        weight = 10 if is_required else 5
        total_points += weight


        if skill.lower() in lower_resume or normalized_jd[index] in exp_res:
            matched_skill.append({"name": skill, "type": "Full"})
            earned_points += weight
            continue


        partial_score = get_partial_match_score(skill, exp_res)
        if partial_score > 0:
            earned_points += (weight * partial_score)
            matched_skill.append({"name": skill, "type": "Partial"})
            continue
        
        if is_semantic_match(jd_emb[index] , res_emb):
            matched_skill.append({"name": skill, "type": "Semantic"})
            earned_points += (weight * 0.7)
            continue
        else:
            missing_skills.append(skill)

        
    if missing_skills:
        matched_names = [s['name'] for s in matched_skill]
        missing_skills = skill_cleaner(missing_skills , matched_names)

            
    match_percentage = float((earned_points / total_points) * 100) if total_points > 0 else 0
    return matched_skill , missing_skills , match_percentage