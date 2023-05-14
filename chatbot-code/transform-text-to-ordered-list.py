from chatgpt_base import get_completion


def generate_full_prompt(text):
    return f"""
      You will be provided with text delimited by triple quotes. 
      If it contains a sequence of instructions, \ 
      re-write those instructions in the following format:

      Step 1 - ...
      Step 2 - …
      …
      Step N - …

      If the text does not contain a sequence of instructions, \ 
      then simply write \"No steps provided.\"

      \"\"\"{text}\"\"\"
    """


text_1 = f"""
Making a cup of tea is easy! First, you need to get some \ 
water boiling. While that's happening, \ 
grab a cup and put a tea bag in it. Once the water is \ 
hot enough, just pour it over the tea bag. \ 
Let it sit for a bit so the tea can steep. After a \ 
few minutes, take out the tea bag. If you \ 
like, you can add some sugar or milk to taste. \ 
And that's it! You've got yourself a delicious \ 
cup of tea to enjoy.
"""

text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the \ 
trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. \ 
Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a \ 
perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""
prompt_1 = generate_full_prompt(text_1)
prompt_2 = generate_full_prompt(text_2)

response_1 = get_completion(prompt_1)
response_2 = get_completion(prompt_2)

print(f'Response 1: {response_1}')
print(f'Response 2: {response_2}')

# Output:

# Response 1: Step 1 - Get some water boiling.
# Step 2 - Grab a cup and put a tea bag in it.
# Step 3 - Once the water is hot enough, pour it over the tea bag.
# Step 4 - Let it sit for a bit so the tea can steep.
# Step 5 - After a few minutes, take out the tea bag.
# Step 6 - Add some sugar or milk to taste.
# Step 7 - Enjoy your delicious cup of tea!


# Response 2: No steps provided.
