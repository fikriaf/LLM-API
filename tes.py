# python3
# please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI

client = OpenAI(api_key="sk-25f383d145e64708a892178268aa5458", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)