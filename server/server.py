from flask import Flask, Response, stream_with_context
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

def generate_text():
    text = "This is an example text..."
    for char in text:
        yield char
        time.sleep(0.05)

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate_text()), content_type='text/plain;charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)
