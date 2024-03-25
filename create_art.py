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
2. come up with art prompt from #1. the art prompt should include hyper specific details that can be illustrated (be meticulous). be in the style of a random art style from history that fits the vibe best from the list. Be creative and surprising!!! 

DO NOT USE SPACE GALAXIES OR ANY REFERENCE TO OUTER SPACE OR AWE OR ANY COLOR VOMIT ON THE CANVAS. KEEP THE PIECE COHESIVE AND CLEAN AND LITERATE.

Styles : ["Abstract Expressionism",
      "Art Deco",
      "Art Nouveau",
      "Avant-garde",
      "Baroque",
      "Bauhaus",
      "Classicism",
      "CoBrA",
      "Color Field Painting",
      "Conceptual Art",
      "Constructivism",
      "Cubism",
      "Dada / Dadaism",
      "Digital Art",
      "Expressionism",
      "Fauvism",
      "Futurism",
      "Harlem Renaissance",
      "Impressionism",
      "Installation Art",
      "Land Art",
      "Minimalism",
      "Neo-Impressionism",
      "Neoclassicism",
      "Neon Art",
      "Op Art",
      "Performance Art",
      "Pop Art",
      "Post-Impressionism",
      "Precisionism",
      "Rococo",
      "Street Art",
      "Surrealism",
      "Suprematism",
      "Symbolism",
      "Zero Group"
    ].
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


