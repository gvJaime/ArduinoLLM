import sys
import openai

MODEL = "gpt-3.5-turbo"

def generate_ino(prompt: str):
    openai.Completion.create(
        model=MODEL,
        prompt=prompt
    )

if __name__ == "__main__":
    import json
    f = open('token.json')
    data = json.load(f)
    openai.api_key = data['key']
    openai.organization = data['org']
    prompt = sys.argv[1:]
    print("introducing: " + prompt[0])
    print(generate_ino(prompt=prompt))