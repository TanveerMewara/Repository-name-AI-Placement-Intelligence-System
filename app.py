# import streamlit as st

# st.title("AI Placement Intelligence System")

# st.write("Resume Analysis & Placement Prediction")

# from resume_parser import extract_text
# import streamlit as st

# st.title("AI Placement Intelligence System")

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file:

#     st.success("Resume Uploaded Successfully")

# import streamlit as st

# from resume_parser import extract_text

# st.title("AI Placement Intelligence System")

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file:

#     text = extract_text(uploaded_file)

#     st.success("Resume Uploaded Successfully")

#     st.subheader("Resume Text")

#     st.write(text[:1000])


# import streamlit as st

# from resume_parser import extract_text
# from skills import extract_skills

# st.title("AI Placement Intelligence System")

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file:

#     text = extract_text(uploaded_file)

#     st.success("Resume Uploaded Successfully")

#     st.subheader("Resume Text")
#     st.write(text[:1000])

#     skills = extract_skills(text)

#     st.subheader("Skills Found")

#     st.write(skills)

# import streamlit as st
# from jd_matcher import match_skills
# from resume_parser import extract_text
# from skills import extract_skills

# st.title("AI Placement Intelligence System")

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file is not None:

#     try:
#         text = extract_text(uploaded_file)

#         st.success("Resume Uploaded Successfully!")

#         st.subheader("Resume Text")
#         st.write(text[:1000])

#         skills = extract_skills(text)

#         st.subheader("Skills Found")
#         st.write(skills)

#     except Exception as e:
#         st.error(f"Error: {e}")

# import streamlit as st
# from resume_parser import extract_text
# from skills import extract_skills
# from jd_matcher import match_skills
# from predictor import predict_student

# st.set_page_config(
#     page_title="AI Placement Intelligence System",
#     layout="wide"
# )

# st.title("🚀 AI Placement Intelligence System")

# st.write(
#     "Upload your resume and compare it with job requirements."
# )

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file is not None:

#     try:

#         text = extract_text(uploaded_file)

#         st.success("✅ Resume Uploaded Successfully!")
        
#         # st.write("Total Skills Found:", len(skills))

#         st.subheader("📄 Resume Text")
#         st.write(text[:1000])

#         skills = extract_skills(text)

#         st.subheader("🛠 Skills Found")
#         st.write(skills)

#         st.subheader("🎯 Job Description Skills")

#         jd_text = st.text_area(
#             "Enter skills separated by commas",
#             placeholder="python, sql, docker, aws, fastapi"
#         )

#         if st.button("Analyze Match"):

#             jd_skills = [
#                 skill.strip().lower()
#                 for skill in jd_text.split(",")
#                 if skill.strip()
#             ]

#             score, matched, missing = match_skills(
#                 skills,
#                 jd_skills
#             )

#             st.subheader("📊 Match Score")
#             st.success(f"{score:.2f}%")

#             st.subheader("✅ Matched Skills")
#             st.write(matched)

#             st.subheader("❌ Missing Skills")
#             st.write(missing)

#     except Exception as e:

#         st.error(f"Error: {e}")

# import streamlit as st

# from resume_parser import extract_text
# from skills import extract_skills
# from jd_matcher import match_skills
# from predictor import predict_student
# from dashboard import (
#     placement_distribution,
#     cgpa_vs_dsa
# )

# st.set_page_config(
#     page_title="AI Placement Intelligence System",
#     layout="wide"
# )

# st.title("🚀 AI Placement Intelligence System")

# st.write(
#     "Upload your resume, compare it with job requirements and predict placement chances."
# )

# uploaded_file = st.file_uploader(
#     "Upload Resume PDF",
#     type=["pdf"]
# )

# if uploaded_file is not None:

#     try:

#         text = extract_text(uploaded_file)

#         st.success("✅ Resume Uploaded Successfully!")

#         st.subheader("📄 Resume Text")
#         st.write(text[:1000])

#         skills = extract_skills(text)

#         # st.subheader("🛠 Skills Found")
#         # st.write(skills)
#         st.subheader("🛠 Skills Found")

#         for skill in skills:
#             st.success(skill)

#         st.markdown("---")

#         st.subheader("🎯 Job Description Matching")

#         jd_text = st.text_area(
#             "Enter JD Skills (comma separated)",
#             placeholder="python, sql, docker, aws, tensorflow"
#         )

#         if st.button("Analyze Match"):

#             jd_skills = [
#                 skill.strip().lower()
#                 for skill in jd_text.split(",")
#                 if skill.strip()
#             ]

#             score, matched, missing = match_skills(
#                 skills,
#                 jd_skills
#             )

#             st.subheader("📊 Match Score")
#             st.success(f"{score:.2f}%")
#             st.progress(int(score))

#             st.subheader("✅ Matched Skills")
#             st.write(matched)

#             st.subheader("❌ Missing Skills")
#             st.write(missing)

#         st.markdown("---")

#         st.header("🎓 Placement Prediction")

#         cgpa = st.number_input(
#             "CGPA",
#             min_value=0.0,
#             max_value=10.0,
#             value=8.0
#         )

#         dsa = st.slider(
#             "DSA Score",
#             0,
#             100,
#             70
#         )

#         aptitude = st.slider(
#             "Aptitude Score",
#             0,
#             100,
#             70
#         )

#         communication = st.slider(
#             "Communication Score",
#             0,
#             100,
#             70
#         )

#         internship = st.selectbox(
#             "Internship Experience",
#             ["No", "Yes"]
#         )

#         if st.button("Predict Placement"):

#             internship_value = (
#                 1 if internship == "Yes" else 0
#             )

#             prediction, accuracy = predict_student(
#                 cgpa,
#                 dsa,
#                 aptitude,
#                 communication,
#                 internship_value
#             )

#             st.subheader("🤖 Model Accuracy")
#             st.write(f"{accuracy:.2f}")

#             if prediction == 1:
#                 st.success("✅ Likely To Be Placed")
#             else:
#                 st.error("⚠️ Placement Risk")

#     except Exception as e:

#         st.error(f"Error: {e}")

import streamlit as st

from resume_parser import extract_text
from skills import extract_skills
from jd_matcher import match_skills
from predictor import predict_student
from dashboard import (
    placement_distribution,
    cgpa_vs_dsa
)
from database import (
    create_database,
    save_candidate
)

create_database()

st.set_page_config(
    page_title="AI Placement Intelligence System",
    layout="wide"
)

st.title("🚀 AI Placement Intelligence System")

candidate_name = st.text_input(
    "Candidate Name"
)

st.write(
    "Upload your resume, compare it with job requirements and predict placement chances."
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    try:

        text = extract_text(uploaded_file)

        st.success("✅ Resume Uploaded Successfully!")

        st.subheader("📄 Resume Text")
        st.write(text[:1000])

        skills = extract_skills(text)

        st.subheader("🛠 Skills Found")

        for skill in skills:
            st.success(skill)

        st.markdown("---")

        st.subheader("🎯 Job Description Matching")

        jd_text = st.text_area(
            "Enter JD Skills (comma separated)",
            placeholder="python, sql, docker, aws, tensorflow"
        )

        if st.button("Analyze Match"):

            jd_skills = [
                skill.strip().lower()
                for skill in jd_text.split(",")
                if skill.strip()
            ]

            score, matched, missing = match_skills(
                skills,
                jd_skills
            )

            st.subheader("📊 Match Score")
            st.success(f"{score:.2f}%")
            st.progress(int(score))

            st.subheader("✅ Matched Skills")
            st.write(matched)

            st.subheader("❌ Missing Skills")
            st.write(missing)

        st.markdown("---")

        st.header("🎓 Placement Prediction")

        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.0
        )

        dsa = st.slider(
            "DSA Score",
            0,
            100,
            70
        )

        aptitude = st.slider(
            "Aptitude Score",
            0,
            100,
            70
        )

        communication = st.slider(
            "Communication Score",
            0,
            100,
            70
        )

        internship = st.selectbox(
            "Internship Experience",
            ["No", "Yes"]
        )

        if st.button("Predict Placement"):

            internship_value = (
                1 if internship == "Yes" else 0
            )

            prediction, accuracy = predict_student(
                cgpa,
                dsa,
                aptitude,
                communication,
                internship_value
            )

            st.subheader("🤖 Model Accuracy")
            st.write(f"{accuracy:.2f}")

            # if prediction == 1:
            #     st.success("✅ Likely To Be Placed")
            # else:
            #     st.error("⚠️ Placement Risk")

            if prediction == 1:

                result = "Likely To Be Placed"

                st.success(result)

            else:

                result = "Placement Risk"

                st.error(result)

            save_candidate(
                candidate_name,
                0,
                result
            )

        st.markdown("---")

        st.header("📈 Placement Analytics Dashboard")

        fig1 = placement_distribution()
        st.pyplot(fig1)

        fig2 = cgpa_vs_dsa()
        st.pyplot(fig2)

    except Exception as e:

        st.error(f"Error: {e}")