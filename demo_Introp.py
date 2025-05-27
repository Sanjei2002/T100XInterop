from ollama import chat
from ollama import ChatResponse
import ollama


# newlist = [expression for item in iterable if condition == True]
# extract what models to use in .config if not found pull it using oolama

localModels = [local_llm["model"]
               for local_llm in ollama.list()["models"] if True]

stream = chat(
    model=str(localModels[0]),
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ], stream=True
)

# print(response.message.content)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    pass
