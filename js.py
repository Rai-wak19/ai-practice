from google import genai
from google.genai import types
from pydantic import ValidationError
from dotenv import load_dotenv

load_dotenv()
client = genai.client()

prompt = """ Analyze this applicant: I study Software Engineering.
I know Python, JavaScript, and React.
I built an AI tourism project.
I want a junior developer internship.

Extract the education, skills, projects, and target role.
Only use information supported by the description """

try:
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = prompt,
        config = types.GenerateContentConfig(
            response_
        )
    )

