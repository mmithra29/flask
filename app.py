from flask import Flask, jsonify # type: ignore
from flask_limiter import Limiter #type: ignore
from flask_limiter.util import get_remote_address #type: ignore
#tried flask to implement rate limiter
#haven't tested it yet
app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)
@app.route('/')
@limiter.limit("10/30 seconds") 
def index():
    return jsonify({"message": "Welcome! You have access to this site."})

@app.route('/limited')
def limited():
    return jsonify({"message": "This is a rate-limited route."})

if __name__ == '__main__':
    app.run(debug=True)
