from openai import OpenAI
from dotenv import load_dotenv
import os
from ocr import ocr_image

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4-turbo-preview"
CONTEXT_WINDOW = 4000


def create_art(data: str):
    prompt = '''
1.what part from the provided text would make for the **best** context for an art prompt? 
2. come up with art prompt from #1. the art prompt should include hyper specific details (be meticulous) and be in the style of a random famous art style from history that fits the vibe best
'''
    data = f"Raw Text: {data}\nArt Prompt:\n" 
    completion = client.chat.completions.create(
        model=GPT3_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": data},
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    data = ocr_image("./output/screenshots/screen.png")
    print(create_art(data))


