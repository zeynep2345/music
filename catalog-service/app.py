from flask import Flask, jsonify

app = Flask(__name__)

# Örnek şarkı veritabanı
songs = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams", "image": "https://images.unsplash.com/photo-1493225255756-d9584f8606e9?w=300"},
        {"title": "Uptown Funk", "artist": "Bruno Mars", "image": "https://images.unsplash.com/photo-1514525253342-b0bb4d722967?w=300"}
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele", "image": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?w=300"},
        {"title": "Fix You", "artist": "Coldplay", "image": "https://images.unsplash.com/photo-1445985543470-41fba5c3144a?w=300"}
    ],
    "energetic": [
        {"title": "Thunderstruck", "artist": "AC/DC", "image": "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=300"}
    ]
}

@app.route('/songs/<mood>')
def get_songs(mood):
    return jsonify(songs.get(mood.lower(), []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
