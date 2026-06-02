from skills import extract_skills

sample_text = """
I have experience in Python, SQL, Pandas, NumPy,
Machine Learning, TensorFlow and NLP.
"""

skills = extract_skills(sample_text)

print(skills)