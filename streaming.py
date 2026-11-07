import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
response = client.models.generate_content_stream(
    model="gemini-3.5-flash-lite",
    contents="Write a short story about a robot learning to love.",
)

for chunk in response:
    if chunk.text:
        print(chunk.text, end="", flush=True)
