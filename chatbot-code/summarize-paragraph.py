from get_completion import get_completion

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
