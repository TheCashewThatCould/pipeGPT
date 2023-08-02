import openai
import sys
import json

# Your OpenAI API Key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Read from stdin
data = sys.stdin.read()

# Send the content of the stdin to the chat models
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",  # Replace this with the GPT-4 model if necessary
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": data}
    ]
)

# Print the assistant's reply
print(response['choices'][0]['message']['content'])
