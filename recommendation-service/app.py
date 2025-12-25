from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Docker Compose içinde servis adı kullanılarak erişilir
CATALOG_SERVICE_URL = os.getenv("CATALOG_URL", "http://localhost:5001")

@app.route('/', methods=['GET', 'POST'])
def index():
    playlist = []
    selected_mood = None
    error = None

    if request.method == 'POST':
        selected_mood = request.form.get('mood')
        try:
            response = requests.get(f"{CATALOG_SERVICE_URL}/songs/{selected_mood}")
            if response.status_code == 200:
                playlist = response.json()
            else:
                error = "Katalog servisine ulaşılamadı."
        except Exception as e:
            error = f"Bağlantı hatası: {str(e)}"

    return render_template('index.html', playlist=playlist, selected_mood=selected_mood, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
