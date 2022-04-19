# Article API

The purpose of this exercise is for us to get a sense of how you would approach designing and implementing a simple service, before we get you in for an interview. We’ve tried to avoid tricky algorithmic tests in favor of something that shows how you would organise a codebase.

Once complete please share your repository (public repo preferred), forward a zip file of the source code and dependencies, or use a service like Dropbox to share the file.

Feel free to use any language/toolset you like, however, submission written in Go (without compromising code quality) will be looked on favourably. The only requirement is that you can describe how to set it up on a mac so we can see it running.

If you make any assumptions about requirements, or use any online resources to solve a problem, please make note of these somewhere obvious inside the solution (e.g. code comments).

Your solution will be evaluated internally by one or more of your potential co workers. You should expect a response from us within 2 business days.

## Requirements

You will be required to create a simple API with three endpoints.

The first endpoint, POST `/articles` should handle the receipt of some article data in JSON format, and store it within the service.

The second endpoint GET `/articles/{id}` should return the JSON representation of the article.

The final endpoint, GET `/tags/{tagName}/{date}` will return the list of articles that have that tag name on the given date and some summary data about that tag for that day.

An article has the following attributes `id`, `title`, `date`, `body`, and list of `tags`. for example:

```json
{
  "id": "1",
  "title": "latest science shows that potato chips are better for you than sugar",
  "date" : "2016-09-22",
  "body" : "some text, potentially containing simple markup about how potato chips are great",
  "tags" : ["health", "fitness", "science"]
}
```

The GET `/tags/{tagName}/{date}` endpoint should produce the following JSON. Note that the actual url would look like /tags/health/20160922.

```json
{
  "tag" : "health",
  "count" : 17,
  "articles" :
    [
      "1",
      "7"
    ],
  "related_tags" :
    [
    "science",
    "fitness"
    ]
}
```

The `related_tags` field contains a list of tags that are on the articles that the current tag is on for the same day. It should not contain duplicates.

The `count` field shows the number of tags for the tag for that day.

The `articles` field contains a list of ids for the last 10 articles entered for that day.

## Deliverables

Please submit the following deliverables to: `amp HYPHEN tech HYPHEN test HYPHEN submissions HYPHEN group AT fairfaxmedia DOT com DOT au`.

1. Source code for the solution described above
2. Setup/installation instructions
3. A quick (1-2 page) description of your solution, outlining anything of interest about the code you have produced. This could be anything from why you chose the language and or libraries, why you structured the project the way that you did, why you chose a particular error handling strategy, how you approached testing etc
4. A list of assumptions that you’ve made while putting this together. We’ve only given you a very loose spec, so you’ll probably need to fill in some blanks while you are working. If you note down the assumptions, for us, then we will be able review the code within the context of those assumptions
5. [Optional] Tell us what you thought of the test and how long it took you to complete
6. [Optional] Tell us what else you would have added to the code if you had more time

Note: We prefer that you send us a link to a (public) repository. If you send an attachment via a zip file with your source code, please be aware that your email may get blocked. You will receive a confirmation email for your submission.
