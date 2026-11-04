from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from PIL import Image


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client()



image = Image.open("image/2i.jpg")
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=[image, "Tell me about this image"],
    config = types.GenerateContentConfig(
        system_instruction="response should be with  in 1000 words , be funny",
        temperature = 0
)
)  

for chunk in response:
    print(chunk.text,end ="---/--")


#print("The response is ")
#print(".................")
#print(".................")
#print(response.text)

