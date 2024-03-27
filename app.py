from flask import Flask, render_template, jsonify
from filter import get_top_100_movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_100', methods=['GET'])
def get_100():
    data = get_top_100_movies()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
