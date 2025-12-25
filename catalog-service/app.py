from flask import Flask, jsonify, request
import random

app = Flask(_name_)

# Müzik Veritabanı (Stateless)
# Resimler için rastgele 'picsum' servisini kullanıyoruz.
songs = [
    {"id": 1, "title": "Happy Vibes", "artist": "The Sunshines", "mood": "happy", "image": "https://picsum.photos/id/10/300/300"},
    {"id": 2, "title": "Morning Coffee", "artist": "Chill Beats", "mood": "chill", "image": "https://picsum.photos/id/20/300/300"},
    {"id": 3, "title": "Gym Power", "artist": "Fit Nation", "mood": "energetic", "image": "https://picsum.photos/id/30/300/300"},
    {"id": 4, "title": "Sad Piano", "artist": "Melancholy", "mood": "sad", "image": "https://picsum.photos/id/40/300/300"},
    {"id": 5, "title": "Summer Dance", "artist": "Party Maker", "mood": "happy", "image": "https://picsum.photos/id/50/300/300"},
    {"id": 6, "title": "Focus Mode", "artist": "Brain Waves", "mood": "study", "image": "https://picsum.photos/id/60/300/300"},
    {"id": 7, "title": "Running Fast", "artist": "Speedy", "mood": "energetic", "image": "https://picsum.photos/id/70/300/300"},
    {"id": 8, "title": "Rainy Window", "artist": "Lofi Girl", "mood": "chill", "image": "https://picsum.photos/id/80/300/300"},
]

@app.route('/songs', methods=['GET'])
def get_songs():
    mood = request.args.get('mood')
    if mood:
        # Python list comprehension ile filtreleme yapıyoruz
        filtered_songs = [s for s in songs if s['mood'] == mood]
        return jsonify(filtered_songs)
    return jsonify(songs)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5001)
