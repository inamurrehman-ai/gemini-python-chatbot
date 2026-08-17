Gemini Python Chatbot

A simple command-line AI chatbot built with Python using the Google Gemini API.

Features

- Interactive command-line chatbot
- Conversation memory
- AI responses using Google Gemini
- Secure API key management using ".env"
- Easy local setup

Technologies Used

- Python
- Google Gemini API
- google-genai
- python-dotenv
- Git & GitHub

Installation

Clone the repository:

git clone https://github.com/inamurrehman-ai/gemini-python-chatbot.git
cd gemini-python-chatbot

Install all required dependencies:

pip install -r requirements.txt

API Key Setup

Create a ".env" file in the project folder:

GEMINI_API_KEY=YOUR_API_KEY

Never share your API key or upload the ".env" file to GitHub.

Run the Chatbot

python main.py

Example

You: My name is Inam
Gemini: Nice to meet you, Inam!

You: What is my name?
Gemini: Your name is Inam.

Type "exit" to close the chatbot.

Project Structure

gemini-python-chatbot/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

«Note: ".env" is intentionally excluded from GitHub using ".gitignore".»

Author

Inam Ur Rehman

GitHub: https://github.com/inamurrehman-ai
