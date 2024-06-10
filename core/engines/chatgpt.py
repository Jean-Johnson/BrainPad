import os
from openai import OpenAI
class LLM:
	def __init__(self,api_key) -> None:
		self.client = OpenAI(api_key=api_key)
	def generate(self,prompt):
		messages = [ 
			{"role": "system", "content": "You are a sentence generator who completes the sentence, given below is a unfinished text. generate the rest of the text and output only the text. no explanation is needed"},{"role": "user", "content": "Hi i am very happy because "}] 
		chat = self.client.chat.completions.create(messages=messages,model="gpt-3.5-turbo")
		reply = chat.choices[0].message.content 
		print(f"ChatGPT: {reply}") 
		messages.append({"role": "assistant", "content": reply}) 
		return reply




