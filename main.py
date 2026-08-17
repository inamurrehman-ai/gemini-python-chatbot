from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

history = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Gemini: Goodbye!")
        break

    history.append(f"User: {question}")

    prompt = "\n".join(history) + "\nGemini:"

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    answer = response.text
    print("Gemini:", answer)

    history.append(f"Gemini: {answer}")