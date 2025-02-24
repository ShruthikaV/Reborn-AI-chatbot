import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDMkX0CmKn3jPHXvsKuk78cRRYvZqhnm70")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def GenerateResponse(input_text):
  response = model.generate_content([
      "input: Who are you?",
      "output: I am a Patient Addiction Query Bot",
      "input: What all can you do?",
      "output: I can help you with any addiction problems that you are facing and may help you with them",
      f"input: {input_text}",
      "output: ",
    ])
  return response.text

# while True:
#   string = str(input("Enter your prompt:"))
#   print("Bot: ", GenerateResponse(string))