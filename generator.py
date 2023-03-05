import sys
import openai

MODEL = "gpt-3.5-turbo"

SYS_ID = 'sysId'

APIKEY = 'key'
ORG = 'org'

def generate_ino(prompt: str):
    import json
    f_conf = open('config.json')
    config = json.load(f_conf)
    sysId = config[SYS_ID]

    userPrompt = {
        "role": "user",
        "content": prompt[0]
    }

    return openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            sysId,
            userPrompt
        ]
    )

if __name__ == "__main__":
    import json
    f = open('token.json')
    data = json.load(f)
    openai.api_key = data[APIKEY]
    openai.organization = data['org']
    prompt = sys.argv[1:]
    print("introducing: " + prompt[0])
    print(generate_ino(prompt=prompt))