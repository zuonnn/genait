

import os
import google.generativeai as genai
api_key="AIzaSyCpSIq8LG5rr7TRqeI33tSXXTyjvj_U8Xg"
genai.configure(api_key=api_key)
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')
promt = input("What do you want to ask?: ")
response = model.generate_content(promt)    
print(response.text)


