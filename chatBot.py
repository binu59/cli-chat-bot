from google import genai
from dotenv import load_dotenv
import os

#Load the API key from the .env file
load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Start a chat session
chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": "You are a helpful assistant."
    }
)

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        #Send the message to the model and get the response
        response = chat.send_message(user_input)
        print(f"Bot: {response.text}\n")
        
    except Exception as e:
        print(f"\n[ERROR]: {e}")
        break