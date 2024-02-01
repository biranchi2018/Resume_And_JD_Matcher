from flask import Flask, request, jsonify
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def read_docx(file_path):
    text = docx2txt.process(file_path)
    return text

def vectorize_text(texts):
    vectorizer = CountVectorizer().fit_transform(texts)
    return vectorizer

def match_resume_job(resume_text, job_description_text):
    vectorized_texts = vectorize_text([resume_text, job_description_text])
    similarity_matrix = cosine_similarity(vectorized_texts)

    match_percentage = similarity_matrix[0, 1] * 100
    return match_percentage

@app.route('/match', methods=['POST'])
def match_resume_job_api():
    try:
        resume_file = request.files['resume']
        job_description_file = request.files['job_description']

        resume_text = read_docx(resume_file)
        job_description_text = read_docx(job_description_file)

        match_percentage = match_resume_job(resume_text, job_description_text)

        response = {
            'match_percentage': match_percentage
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
