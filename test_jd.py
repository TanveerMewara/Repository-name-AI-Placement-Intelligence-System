from jd_matcher import match_skills

resume_skills = [
    "python",
    "sql",
    "tensorflow",
    "numpy"
]

jd_skills = [
    "python",
    "sql",
    "docker",
    "aws"
]

score, matched, missing = match_skills(
    resume_skills,
    jd_skills
)

print(f"\nMatch Score: {score:.2f}%")

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)