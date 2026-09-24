SYSTEM_PROMPT = """
You are an expert technical recruiter and resume analyst.

Your task is to compare a candidate's resume
with a job description.

Analyze the information objectively.

Do not invent information that is not present
in the resume.

Provide the following sections:

1. Match Percentage
2. Matching Skills
3. Missing Skills
4. Relevant Experience
5. Resume Improvement Suggestions
6. Interview Questions
"""


def create_resume_prompt(resume_text, job_description):

    prompt = f"""
Analyze the following resume against the job description.

====================
RESUME
====================

{resume_text}

====================
JOB DESCRIPTION
====================

{job_description}

====================
TASK
====================

Please provide:

1. Estimated skill match percentage
2. Matching technical skills
3. Missing technical skills
4. Relevant experience
5. Resume improvement suggestions
6. Five interview questions based on the job description

Only use information available in the provided resume.

Do not create or assume qualifications
that are not mentioned in the resume.
"""

    return prompt