from google import genai
from google.genai import types
from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash-lite")



print("chat starts here .. type 'end chat' to close")

userinput = input("user : ")

while userinput != 'endchat':
    response = chat.send_message(userinput)
    print("Startbot : " + response.text)
    userinput = input("user : ")

for message in chat.get_history():
    print(f"role - {message.role}")
    print(message.parts[0].text)
