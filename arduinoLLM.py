import generator
import sys
import os

OUT_FILE = "out/main.ino"

if __name__ == "__main__":
    filename = sys.argv[1]
    input = open(filename, "r")
    prompt = input.read()
    input.close()

    print("creating output file...")
    if os.path.exists(OUT_FILE):
        os.remove(OUT_FILE)
    
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

    with open(OUT_FILE, "w") as output:
        print("prompting API...")

        response = generator.generate_ino(prompt)

        output.write(response.choices[0].message.content)

        print("done")
