from flask import Flask, request
from pymongo import MongoClient
import ssl

# Create Flask app
app = Flask(__name__)

# Connection URI to MongoDB cluster
client = MongoClient("mongodb+srv://article-api-user:MrpCs9OHJRNnOzG7@articleapi.k4ptm.mongodb.net/articles-api-db?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000, ssl_cert_reqs=ssl.CERT_NONE)

@app.route('/')
def hello():
    return 'Hello, World!'

"""
First endpoint: POST /articles should handle the receipt of some article data in JSON format, and store it within the service.
"""
@app.route('/articles', methods=['POST'])
def create_article():
    pass

"""
Second endpoint: GET /articles/{id} should return the JSON representation of the article.
"""
@app.route('/articles/<id>', methods=['GET'])
def get_article():
    pass

"""
Third endpoint: GET /tags/{tagName}/{date} will return the list of articles that have that tag name on the given date and some summary data about that tag for that day.
"""
@app.route('/tags/<tagName>/<date>', methods=['GET'])
def get_tag_summary(tagName, date):
    pass

if __name__ == "__main__":
    app.run()