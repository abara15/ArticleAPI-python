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
    # Get the database we need in our cluster
    db = client['articles-api-db']
    # Count documents currently in our collection to determine new id - e.g. if we have 50 documents, then the new id will be 51
    count = db['articles'].count_documents({}) + 1
    # Split string of tags (separated by commas & space) into a list.
    req_tags = request.form['tags'].split(", ")
    
    # Insert new article into database
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
    # Get the database we need in our cluster
    db = client['articles-api-db']
    # Count documents currently in our collection to determine new id - e.g. if we have 50 documents, then the new id will be 51
    count = db['articles'].count_documents({})
    # Initialise empty dict
    result = {}
    
    if (int(id) > count):
        # Guarantees to terminate API call if the requested ID is not in the database.
        return "Please query for a valid article."
    else:
        # Get all the documents with the requested ID - will return a Cursor of one document.
        cursor = db['articles'].find({ 'id': int(id) })
        # Put the requested article into the dict
        for document in cursor:
            result.update(document)
        # Remove ObjectId - this is a standard field on all MongoDB documents that we don't need
        result.pop('_id')
        # Return the result in JSON format.
        return result


"""
Third endpoint: GET /tags/{tagName}/{date} will return the list of articles that have that tag name on the given date and some summary data about that tag for that day.
"""
@app.route('/tags/<tagName>/<date>', methods=['GET'])
def get_tag_summary(tagName, date):
    # Convert date to correct format
    new_date = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
    
    # Get the database we need in our cluster
    db = client['articles-api-db']
    # Get all the documents with the requested tag/date.
    cursor = db['articles'].find({ 'tags': tagName, 'date': new_date }).limit(10)
    # Count how many articles are within the parameters.
    count = db['articles'].count_documents({ 'tags': tagName, 'date': new_date })
    # Initialised empty list for article
    articles = []
    related_tags = []
    # Initialised empty dict which we will use
    objects = {}
    
    # Loop over each article with the given tag.
    for document in cursor:
        # Set the current document to our temporary dict
        objects.update(document)
        # Append the id of the current document to tjeu array.
        articles.append(objects['id'])
        # Loop over each tag in the current document
        for tag in objects['tags']:
            # Condition to filter out tags which are already in our array.
            if tag not in related_tags and tag != tagName:
                related_tags.append(tag)
    
    # Create our JSON model for what was required
    response = {
        "tag": tagName,
        "count": count,
        "articles": articles[-10:], # Takes the last 10 article IDs
        "related_tags": related_tags
    }
    
    return response

if __name__ == "__main__":
    app.run()