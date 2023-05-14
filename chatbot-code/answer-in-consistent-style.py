from chatgpt_base import get_completion

# Note: the child grandparent is an example of few-shot prompting.
# The below is from the tutorial. I will try out another example.

# prompt = f"""
# Your task is to answer in a consistent style.

# <child>: Teach me about patience.

# <grandparent>: The river that carves the deepest \
# valley flows from a modest spring; the \
# grandest symphony originates from a single note; \
# the most intricate tapestry begins with a solitary thread.

# <child>: Teach me about resilience.
# """
# response = get_completion(prompt)
# print(response)

prompt = f"""
  Your task is to answer in a consistent style.
  
  <student>: What is the concept of knowledge, according to Foucault?

  <professor>: In The Archaeology of Knowledge, Foucault rejected the notion \
    of transcendental knowledge and instead argued that all knowledge is \
    related to and an extension of power. He asks the question of whether all knowledge is, \
    in the final analysis, mere ideology. This leads to a radical critique \
    of Western European culture, attempting to show that what appear to be \
    at first glance progressive ideas of modernity are in fact reflections \
    of the dominant power structure.
  
  <student>: What are the core concepts surrounding ethics, according to Levinas?
"""

response = get_completion(prompt)
print(response)

# Output:

# <professor>: Levinas' philosophy centers around the concept of the Other,
# which he sees as a fundamental aspect of ethics. He argues that our
# responsibility to the Other is not based on any pre-existing moral code
# or principle, but rather arises from a direct encounter with their vulnerability
# and need. This encounter creates an ethical demand that cannot be ignored or reduced
# to a calculation of self-interest. Levinas also emphasizes the importance of humility
# and openness to the Other, as well as the recognition of our own limitations and
# fallibility. Overall, his ethics is characterized by a radical emphasis on the primacy
# of the Other and a rejection of any attempt to reduce ethics to a set of rules or principles.
