import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_docx(file_path):
    text = docx2txt.process(file_path)
    return text

def vectorize_text(texts):
    vectorizer = CountVectorizer().fit_transform(texts)
    return vectorizer

def match_resume_job(resume_path, job_description_path):
    resume_text = read_docx(resume_path)
    job_description_text = read_docx(job_description_path)

    vectorized_texts = vectorize_text([resume_text, job_description_text])
    similarity_matrix = cosine_similarity(vectorized_texts)

    match_percentage = similarity_matrix[0, 1] * 100
    return match_percentage

# Example usage
resume_path = 'resume/resume.docx'
job_description_path = 'jd/jd.docx'

match_percentage = match_resume_job(resume_path, job_description_path)
print(f"Match Percentage: {match_percentage:.2f}%")
