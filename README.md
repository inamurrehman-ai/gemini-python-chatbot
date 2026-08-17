Gemini Python Chatbot

A simple command-line AI chatbot built with Python using the Google Gemini API.

Features

- Interactive command-line chatbot
- Uses Google Gemini for AI responses
- Secure API key management with ".env"
- Easy to run locally
- GitHub-ready with ".gitignore"

Technologies Used

- Python
- Google Gemini API
- "google-genai"
- "python-dotenv"
- Git & GitHub

Installation

Clone the repository:

git clone https://github.com/inamurrehman178/gemini-python-chatbot.git
cd gemini-python-chatbot

Install the required packages:

pip install google-genai python-dotenv

API Key Setup

Create a ".env" file in the project folder:

GEMINI_API_KEY=YOUR_API_KEY

Never share your API key or upload the ".env" file to GitHub.

Run the Chatbot

Run:

python main.py

Then type your question:

You: Hello
Gemini: Hello! How can I help you today?

To exit the chatbot:

You: exit

Project Structure

gemini-python-chatbot/
│
├── main.py
├── .gitignore
└── .env

«Note: ".env" is intentionally excluded from GitHub using ".gitignore".»

Author

Inam Ur Rehman

GitHub: https://github.com/inamurrehman178
