from chatgpt_base import get_completion

# This came up in the context of the principle of "giving the model time to think".
# To me, this principle means, "break down complex requests into discrete steps".

text = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""

# Example 1
prompt_1 = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into German.
3 - List each name in the German summary.
4 - Output a json object that contains the following \
keys: german_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""
# response = get_completion(prompt_1)
# print("Completion for prompt 1:")
# print(response)

# Output:

# Completion for prompt 1:
# Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

# Zwei Geschwister, Jack und Jill, machen sich auf die Suche nach Wasser aus einem Brunnen auf einem Hügel, aber ein Missgeschick führt dazu, dass sie beide den Hügel hinunterstürzen und leicht verletzt nach Hause zurückkehren, aber ihre abenteuerlichen Geister bleiben ungetrübt.

# Jack, Jill.

# {
#   "german_summary": "Zwei Geschwister, Jack und Jill, machen sich auf die Suche nach Wasser aus einem Brunnen auf einem Hügel, aber ein Missgeschick führt dazu, dass sie beide den Hügel hinunterstürzen und leicht verletzt nach Hause zurückkehren, aber ihre abenteuerlichen Geister bleiben ungetrübt.",
#   "num_names": 2
# }


# Example 2 - specify the structure of the output you want.

prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
response = get_completion(prompt_2)
print("\nCompletion for prompt 2:")
print(response)

# Output:

# Completion for prompt 2:
# Summary: Jack and Jill go on a quest to fetch water, but misfortune strikes and they tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.
# Translation: Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.
# Names: Jack, Jill
# Output JSON: {"french_summary": "Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.", "num_names": 2}
