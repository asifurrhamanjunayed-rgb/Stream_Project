from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)


def code_analyzer(image, option):
    if option == "Hints":
        prompt = "Analyze the code and give me Hints not show the answer"
    else:
        prompt = "Analyze the code and give me the correct code"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response.text
