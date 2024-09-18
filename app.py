from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Indie artists data with images, SoundCloud links, and relevance (mocked)
indie_artists = {
    "rock": [
        {"name": "Dea Matrona", "image": "https://cdns-images.dzcdn.net/images/cover/55896eaf05f1a3409b128ac457bc1c73/1900x1900-000000-80-0-0.jpg", "soundcloud": "https://open.spotify.com/intl-pt/artist/2mjBLM7k51GwUPhN1miEHY", "relevance": 90},
        {"name": "The Strokes", "image": "https://example.com/the_strokes.jpg", "soundcloud": "https://soundcloud.com/the-strokes", "relevance": 85},
        {"name": "Phoebe Bridgers", "image": "https://example.com/phoebe_bridgers.jpg", "soundcloud": "https://soundcloud.com/phoebe-bridgers", "relevance": 80}
    ],
    "pop": [
        {"name": "Clairo", "image": "https://example.com/clairo.jpg", "soundcloud": "https://soundcloud.com/clairo", "relevance": 95},
        {"name": "Girl in Red", "image": "https://example.com/girl_in_red.jpg", "soundcloud": "https://soundcloud.com/girl-in-red", "relevance": 90},
        {"name": "Still Woozy", "image": "https://example.com/still_woozy.jpg", "soundcloud": "https://soundcloud.com/still-woozy", "relevance": 85}
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('musicInput').lower()

    # Simple mock logic to recommend indie artists based on user input
    if "rock" in user_input:
        recommendations = [(artist["name"], artist["image"], artist["soundcloud"], artist["relevance"], artist["relevance"] * 3) for artist in indie_artists["rock"]]
    elif "pop" in user_input:
        recommendations = [(artist["name"], artist["image"], artist["soundcloud"], artist["relevance"], artist["relevance"] * 3) for artist in indie_artists["pop"]]
    else:
        recommendations = [
            ("Dea Matrona", "https://cdns-images.dzcdn.net/images/cover/55896eaf05f1a3409b128ac457bc1c73/1900x1900-000000-80-0-0.jpg", "https://open.spotify.com/intl-es/artist/2mjBLM7k51GwUPhN1miEHY", 80, 80 * 3),
            ("The Last Dinner Party", "https://dynamicmedia.livenationinternational.com/r/i/k/248ca42b-9e8c-4e90-9dad-a061ece28f8e.jpg", "https://soundcloud.com/thelastdinnerparty", 75, 75 * 3),
            ("Pacifica", "https://es.rollingstone.com/wp-content/uploads/2023/07/pacifica.jpg", "https://open.spotify.com/intl-pt/artist/4YcQuAswXPWdO2WAxTRXse", 70, 70 * 3)
        ]  # Default fallback

    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
