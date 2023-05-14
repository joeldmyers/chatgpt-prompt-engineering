from chatgpt_base import get_completion

prompt = f"""
Generate a list of five made-up song names along with artist names and genres. \
Provide them in JSON format with the following keys: 
song_id, title, artist, genre.
"""

response = get_completion(prompt)

print(response)

# Output:

# {
#   "song_id": 1,
#   "title": "Electric Dreams",
#   "artist": "Nova Wave",
#   "genre": "Synthwave"
# },
# {
#   "song_id": 2,
#   "title": "Midnight Mirage",
#   "artist": "Luminous Echo",
#   "genre": "Chillstep"
# },
# {
#   "song_id": 3,
#   "title": "Neon Nights",
#   "artist": "Retro Future",
#   "genre": "Synthpop"
# },
# {
#   "song_id": 4,
#   "title": "Galactic Groove",
#   "artist": "Cosmic Funk",
#   "genre": "Funk"
# },
# {
#   "song_id": 5,
#   "title": "Dreamscape Symphony",
#   "artist": "Celestial Harmony",
#   "genre": "Ambient"
# }
