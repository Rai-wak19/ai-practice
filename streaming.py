from google import genai
import os 

os.environ["GEMINI_API_KEY"] = "AIzaSyB-IITRhAf8bBb7IgVPMRsDhI0uW0BVSjg"

client = genai.Client()
response = client.models.generate_content_stream(
    model="gemini-3.5-flash-lite",
    contents="Write a short story about a robot learning to love.",
    )

for chunk in response:
    if chunk.text:
        print(chunk.text, end="",flush = True)
