import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0  # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]


text = f"""
    Dorothee is sitting in bed and she is my love. I love her so much. \
    I am really glad that she is here and we can be together! \
    She is the best! I hope she has a wonderful \
    and awesome Sunday and a great rest of the week! \
    """

prompt = f"""
    Summarize the text delimited by triple backticks into a single sentence.

    Keep the sentence to under ten words.
    
    ```{text}```
    """

response = get_completion(prompt)

print(response)
