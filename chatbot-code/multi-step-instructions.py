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
# example 1
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
response = get_completion(prompt_1)
print("Completion for prompt 1:")
print(response)

# Output:

# Completion for prompt 1:
# Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

# Zwei Geschwister, Jack und Jill, machen sich auf die Suche nach Wasser aus einem Brunnen auf einem Hügel, aber ein Missgeschick führt dazu, dass sie beide den Hügel hinunterstürzen und leicht verletzt nach Hause zurückkehren, aber ihre abenteuerlichen Geister bleiben ungetrübt.

# Jack, Jill.

# {
#   "german_summary": "Zwei Geschwister, Jack und Jill, machen sich auf die Suche nach Wasser aus einem Brunnen auf einem Hügel, aber ein Missgeschick führt dazu, dass sie beide den Hügel hinunterstürzen und leicht verletzt nach Hause zurückkehren, aber ihre abenteuerlichen Geister bleiben ungetrübt.",
#   "num_names": 2
# }
