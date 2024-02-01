# Resume_And_JD_Matcher
This script matches the Resume/CV against the Job Description. 

This is helpful for the candidates, recruiters to evaulate the resume/cv matching score against the job description.


## Notes
- Rename the resume/cv to resume.docx
- Save the job description in .docx format
- Place the resume in the /resume folder 
- Place the jd in the /jd folder


## Usage

### 1. Create virtual environment 
```cmd
python -m venv env
. env/bin/activate
```

### 2. Install the dependencies
```cmd
pip install -r requirements.txt
```

### 3. Add the Resume and JD to the respective folders
resume/resume.docx
jd/jd.docx


### 4. Run the app2.py script
```python
python3 app2.py 
```

Output :
Match Percentage: 47.32%




