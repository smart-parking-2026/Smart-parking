from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Smart Parking is Online!</h1><p>The connection between GitHub and Render is successful.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
