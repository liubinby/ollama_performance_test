import time
from ollama import Client

client = Client()

prompt = "Write a short story about a robot learning to paint."
num_tokens = 100  # Adjust this to the number of tokens you want to generate

start_time = time.time()

response = client.generate(model='deepseek-coder:6.7b', prompt=prompt, stream=False, options={'num_predict': num_tokens})

end_time = time.time()

generated_text = response['response']
tokens_generated = len(generated_text.split())  # This is a rough estimate
time_taken = end_time - start_time

tokens_per_second = tokens_generated / time_taken

print(f"Tokens generated: {tokens_generated}")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Tokens per second: {tokens_per_second:.2f}")