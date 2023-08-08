from flask import Flask, render_template, request, jsonify
from WebScraper import scraper

app = Flask(__name__)

@app.route("/")
def home():
    return ("Hello World Sooriya")

@app.route("/jobs", methods=['POST', 'GET'])
def jobs():
    if (request.method == 'GET'):
        return (render_template("index.html"))
    else:
        count = int(request.form.get('count'))
        result = scraper(count)
        return (jsonify(result))

if __name__ == '__main__':
    app.run(debug=True, port=5001)