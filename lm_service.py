import os

from dotenv import load_dotenv
from openai import OpenAI

from app.prompts import (
    SYSTEM_PROMPT,
    create_resume_prompt
)

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_resume(resume_text, job_description):

    prompt = create_resume_prompt(
        resume_text,
        job_description
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content