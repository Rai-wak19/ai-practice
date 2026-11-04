from google import genai
from google.genai import types
from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()

print("chat starts here .. type 'end chat' to close")

chat = []
userinput = input("user :")

while userinput != 'endchat':
    chat.append("user: " + userinput)
    systemoutput = client.models.generate_content(
        contents = chat ,   
        model = 'gemini-3.5-flash-lite',
        config = types.GenerateContentConfig(
            system_instruction="Answer in 1 line , within 50 characters"
        )
    )
    chat.append("statbot: " + systemoutput.text)  

    print("Startbot : " , systemoutput.text)
    userinput = input("user : ")