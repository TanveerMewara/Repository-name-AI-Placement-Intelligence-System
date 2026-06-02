from resume_parser import extract_text
from skills import extract_skills
from jd_matcher import match_skills

text = extract_text("resume.pdf")

resume_skills = extract_skills(text)

jd_skills = [
    "python",
    "sql",
    "docker",
    "aws",
    "tensorflow"
]

score, matched, missing = match_skills(
    resume_skills,
    jd_skills
)

print("\nResume Skills:")
print(resume_skills)

print(f"\nMatch Score: {score:.2f}%")

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)