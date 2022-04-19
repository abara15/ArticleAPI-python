from flask import Flask, request
from datetime import datetime
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
    db = client['articles-api-db']
    # Count documents currently in our collection to determine new id - e.g. if we have 50 documents, then the new id will be 51
    count = db['articles'].count_documents({}) + 1
    req_tags = request.form['tags'].split(", ")
    
    db['articles'].insert_one(
        {
            "id": count,
            "title": request.form['title'],
            "date": datetime.now().strftime('%Y-%m-%d'),
            "body": request.form['body'],
            "tags": req_tags
        }
    )
    return f"Article #{count} added to database."


"""
Second endpoint: GET /articles/{id} should return the JSON representation of the article.
"""
@app.route('/articles/<id>', methods=['GET'])
def get_article(id):
    db = client['articles-api-db']
    count = db['articles'].count_documents({})
    objects = {}
    
    if (int(id) > count):
        return "Please query for a valid article."
    else:
        cursor = db['articles'].find({ 'id': int(id) })
        for document in cursor:
            objects.update(document)
        # Remove ObjectId - this is a standard field on all MongoDB documents
        objects.pop('_id')
        return objects


"""
Third endpoint: GET /tags/{tagName}/{date} will return the list of articles that have that tag name on the given date and some summary data about that tag for that day.
"""
@app.route('/tags/<tagName>/<date>', methods=['GET'])
def get_tag_summary(tagName, date):
    objects = {}
    
    # Convert date to correct format
    new_date = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    db = client['articles-api-db']
    cursor = db['articles'].find({ 'tags': tagName, 'date': new_date }).limit(10)
    count = db['articles'].count_documents({ 'tags': tagName, 'date': new_date })
    articles = []
    related_tags = []
    
    for document in cursor:
        objects.update(document)
        articles.append(objects['id'])
        for tag in objects['tags']:
            if tag not in related_tags and tag != tagName:
                related_tags.append(tag)
    
    response = {
        "tag": tagName,
        "count": count,
        "articles": articles,
        "related_tags": related_tags
    }
    
    return response

if __name__ == "__main__":
    app.run()