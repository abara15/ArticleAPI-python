# Article API Technical Test

## Deliverables

### Source Code
Please see the files in this repository for source code. All of the code currently is in the ```app.py``` file.

### Mac Setup
In order to run this application, enter the following command into your Terminal:

```
python3 app.py
```

### Solution
Before going into coding this solution, I took some time to think about how I would be handling my data. I knew I would definitely need a database to store data in after POST requests, and to pull data after GET requests. I picked MongoDB since this is a solution I've heard about before, but never actually used. Additonally, I picked MongoDB over relational database management systems due to its support for dynamic queries, easy to use structure, and schema-less nature, which is very similar to Google Firebase's database services, which I have used in the past.

Next, I had to decide on what language to code this solution in. Originally, I wanted to use Golang since the spec said this would be favourable, however in the end I decided to build a Flask application with Python. The biggest reason I chose this was because I have experience writing back-end with Flask, and I kept getting stuck when trying to build this API in Golang.




A quick (1-2 page) description of your solution, outlining anything of interest about the code you have produced. 
This could be anything from why you chose the language and or libraries, 
why you structured the project the way that you did, why you chose a particular error handling strategy, 
how you approached testing etc

### Assumptions
One of my first assumptions for this project was regarding the payload for our first endpoint. Given the model of an article given to me, I wasn't sure whether the payload would include the ```id``` and ```date```. I decided to assume that the payload would only include the ```title```, ```body```, and ```tags```. This is because I thought of this in terms of an actual user using a form for example to submit an article. It wouldn't make sense for them to put their own ```id```, since this looked like the ```id```'s for each article will simply increment.
As a result, I simply count how many documents are in my ```articles``` collection in my database, and just add 1 to it - for example, if there were 20 documents in my collection, then the new article will have ```id = 21```. I also thought it would be easier to use the datetime library in Python to just generate the current date, as users may enter their dates in varied formats, which would make it hard to conduct queries on the database. This way, we keep a nice and consistent date format. I also assumed that the ```tags``` field would simply be entered as one long string in the format "tag1, tag2, ...".

The second endpoint seemed easy enough and straightforward.

For the third endpoint, I assumed that the ```count``` field simply shows the number of times the given tag is assigned to the articles for that day.

### What did you think of the test and how long did it take to complete?
I think this was a great test. It was a fun challenge and allowed me to experiment in terms of the assumptions I made. This took me about 5 hours worth of coding and debugging to finish. I was slowed down by trying to figure out how MongoDB works, however I also spent a few hours trying to implement this in Golang and doing research on MongoDB.

### What else you would have added to the code if you had more time?
If I had more time, I would've definitely given it a crack in Golang. I also would have tried to simplify my third endpoint a lot more and make this solution a bit more "production ready". I also would have done more to handle my PyMongo errors, but I ran out of time.
