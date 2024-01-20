from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

while True:
    message = str(input("Ask ChatGPT: "))

    if message=="exit": break

    client = OpenAI(
        api_key=os.environ.get("OPEN_API_KEY"),
    )

    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': message,
            }
        ],
    )

    print()
    print(completion.choices[0].message.content)
    print()