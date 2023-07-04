import os
import openai
import tiktoken

openai.api_key = os.environ['OPENAI_API_KEY']



def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

unoptimised_code = '''
result = ''
for i in range(1000):
    result += str(i)
'''
prompt = "optimise this code for memory and time. Only give me executable code output and no other text. Optimise it for giving results: {}"

# Count tokens in prompt:
print('Number of tokens for prompt: {}'.format(
    num_tokens_from_string(prompt.format(unoptimised_code), "cl100k_base")
    )
)

# Chat
chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "user",
        "content": prompt.format(unoptimised_code)
    }
  ]
)
print(chat_response)

# Completions
completed_code = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt.format(unoptimised_code),
  temperature=0.2
)
print(completed_code)

# Edit
edited_code = openai.Edit.create(
  model="text-davinci-edit-001",
  input=unoptimised_code,
  instruction=prompt.format("")
)
print(edited_code)

