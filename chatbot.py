import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        self.messages = []

    def ask_question(self, question):
        self.messages.append({'role': 'user', 'content': question})
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=self.messages)
        answer = response.choices[0].message['content']
        self.messages.append({'role': 'assistant', 'content': answer})
        return answer
    