def match_skills(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = list(resume_set.intersection(jd_set))

    missing = list(jd_set - resume_set)

    score = (len(matched) / len(jd_set)) * 100

    return score, matched, missing