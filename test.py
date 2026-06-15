#pip install tiktoken

import tiktoken
encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
input = "ChatGPT is amazing. "
tokens = encoder.encode(input)
print(f"Token count: {len(tokens)}")