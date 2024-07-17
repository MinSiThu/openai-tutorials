import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="Put api key here",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is 1+1 in terms of binary",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)
print(chat_completion.choices[0].message.content)