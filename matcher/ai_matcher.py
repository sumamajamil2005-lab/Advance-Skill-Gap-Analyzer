from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-miniLM-L6-v2" , device= "cpu")

def get_embeddings(text_list):
    if not text_list:
        return None
    return model.encode(text_list , convert_to_tensor= True)

def is_semantic_match(jd_emb , res_emb , threshold= 0.5):
    if jd_emb is None or res_emb is None:
        return False
    
    cosine_similarity = util.cos_sim(jd_emb , res_emb)[0]
    return any(cosine_score >= threshold for cosine_score in cosine_similarity)