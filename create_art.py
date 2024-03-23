from openai import OpenAI
from dotenv import load_dotenv
import os
from ocr import ocr_image

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4-turbo-preview"
CONTEXT_WINDOW = 4000


def create_art_prompt(data: str):
    prompt = '''
1.what part from the provided text would make for the **best** context for an art prompt? 
2. come up with art prompt from #1. the art prompt should include hyper specific details (be meticulous) and be in the style of a random art style from history that fits the vibe best from the list: [
    "Pre-Historic",
    "Ancient Egyptian",
    "Mesopotamian",
    "Minoan and Mycenaean",
    "Ancient Greek and Roman",
    "Byzantine",
    "Islamic Art",
    "Medieval",
    "Renaissance",
    "Mannerism",
    "Baroque",
    "Rococo",
    "Neoclassicism",
    "Romanticism",
    "Realism",
    "Impressionism",
    "Post-Impressionism",
    "Symbolism",
    "Art Nouveau",
    "Expressionism",
    "Cubism",
    "Futurism",
    "Dada",
    "Surrealism",
    "Abstract Expressionism",
    "Pop Art",
    "Minimalism",
    "Conceptual Art",
    "Performance Art",
    "Installation Art",
    "Digital Art",
    "Street Art",
    "Contemporary Art"
]. Leverage the rule of thirds and golden ratio in your prompt. And make sure the eye is drawn to the focal point of the art.
'''
    data = f"Raw Text: {data}\nArt Prompt:\n"
    completion = client.chat.completions.create(
        model=GPT4_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": data },
        ]
    )
    return completion.choices[0].message.content


def create_art(data: str):
    res = client.images.generate(
        model="dall-e-3",
        prompt=data,
        n=1,
        size="1024x1024"
    )

    return res.data[0].url


