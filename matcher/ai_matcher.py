from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2" , device="cpu")

def get_embeddings(text_list):
    if not text_list:
        return None
    return model.encode(text_list, convert_to_tensor=True)

def is_semantic_match(jd_skill_emb, resume_embs, threshold=0.5):
    if jd_skill_emb is None or resume_embs is None:
        return False
    
    cosine_scores = util.cos_sim(jd_skill_emb, resume_embs)[0]
    return any(score >= threshold for score in cosine_scores)