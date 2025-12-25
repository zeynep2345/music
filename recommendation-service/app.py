from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Docker ağındaki diğer servisin adresi
CATALOG_SERVICE_URL = "http://catalog-service:5001/songs"

@app.route('/', methods=['GET', 'POST'])
def index():
    playlist = []
    selected_mood = None
    error = None

    if request.method == 'POST':
        selected_mood = request.form.get('mood')
        
        # Diğer servise istek at (Service Communication)
        try:
            response = requests.get(f"{CATALOG_SERVICE_URL}?mood={selected_mood}")
            if response.status_code == 200:
                playlist = response.json()
            else:
                error = "Müzik listesi alınamadı."
        except:
            error = "Katalog servisine ulaşılamıyor."

    return render_template('index.html', playlist=playlist, selected_mood=selected_mood, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
