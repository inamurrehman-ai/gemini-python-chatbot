from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not configured.")
    print("Please add your API key to the .env file.")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Conversation history
history = []

# Welcome message
print("=" * 50)
print("        GEMINI PYTHON CHATBOT")
print("=" * 50)
print("Type your message to chat with Gemini.")
print("Commands:")
print("  exit  - Exit the chatbot")
print("  clear - Clear conversation history")
print("=" * 50)

while True:
    try:
        question = input("\nYou: ").strip()

        # Ignore empty input
        if not question:
            print("Gemini: Please enter a message.")
            continue

        # Exit command
        if question.lower() == "exit":
            print("\nGemini: Goodbye! 👋")
            break

        # Clear conversation
        if question.lower() == "clear":
            history.clear()
            print("Gemini: Conversation history cleared.")
            continue

        # Add user message
        history.append(f"User: {question}")

        # Create conversation prompt
        prompt = "\n".join(history) + "\nGemini:"

        print("Gemini: Thinking...")

        # Generate response
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        answer = response.text

        # Display response
        print(f"Gemini: {answer}")

        # Save response to history
        history.append(f"Gemini: {answer}")

    except KeyboardInterrupt:
        print("\n\nGemini: Goodbye! 👋")
        break

    except Exception as e:
        print(f"\nGemini: Sorry, something went wrong.")
        print(f"Error: {e}")