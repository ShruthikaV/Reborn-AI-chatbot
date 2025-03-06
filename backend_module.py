import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDMkX0CmKn3jPHXvsKuk78cRRYvZqhnm70")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
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
    "input: \"I think I have a problem with alcohol.\"",
    "output: Thank you for sharing this. To help the doctor understand your situation better, could you tell me how long you have felt this way?",
    "input: About 6 months.",
    "output: Okay. And on average, how many days a week do you drink alcohol?",
    "input: Is this information confidential?",
    "output: Yes, your information is confidential and will only be shared with a doctor to help with your diagnosis and treatment. We are committed to protecting your privacy.",
    "input: I'm having thoughts of hurting myself.",
    "output: I understand you're going through a difficult time. It's important to get help immediately. Please call a crisis hotline at XXX-XXX-XXX or go to the nearest emergency room.",
      f"input: {input_text}",
      "output: ",
    ])
  return response.text
