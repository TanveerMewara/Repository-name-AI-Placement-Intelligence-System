SKILLS = [
    "python",
    "sql",
    "machine learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "deep learning",
    "docker",
    "aws",
    "fastapi"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found