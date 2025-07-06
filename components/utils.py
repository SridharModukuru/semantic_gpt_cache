import math

def cosine_similarity(vector1, vector2):
    dot_product = sum(a * b for a,b in zip(vector1, vector2))

    mag1 = math.sqrt(sum(a * a for a in vector1))  #magnitude = sqrt(a1square + a2 sq + a3 sq ---)
    mag2 = math.sqrt(sum(b * b for b in vector2))
    
    #  similarity = (ABcosx / |A|*|B|)
    similarity_index =  dot_product / (mag1 * mag2)

    return similarity_index
