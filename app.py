from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/articles', methods=['POST'])
def create_article():
    pass

@app.route('/articles/<id>', methods=['GET'])
def get_article():
    pass

@app.route('/tags/<tagName>/<date>', methods=['GET'])
def get_tag_summary(tagName, date):
    pass

if __name__ == "__main__":
    app.run()