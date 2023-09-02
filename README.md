# Py-Blog v1.0.0 - By LolzTheDev

> What is Py-Blog?

Py-Blog is a simple project I made that lets people create blogs! You will need experience in MongoDB though, since this only ships the rendering and front-end.

To actually post a new post you will need to create your own post client. Something simple like:

```py
Post Title: <your-post-title>
Post Content: <post-content>
Post Author: <your-name-here>
```

I *might* make software that lets people create posts by myself, but this project is only focusing on rendering the frontend.

> Can I contribute?

Of Course! Feel free to clone the repo and make pull requests. I don't use GitHub too much so the request might take a while to actually review.

If you wish, you can fork this and make it better!

> Can I use this for free?

Yep. That's why I made it lmao.

## Setup Instructions
> How Do I Set my Blog Up?

1. Open [MongoDB](https://mongodb.com)
2. Create an account (if you don't have one)
3. Create a cluster
4. Create a login for the db access
5. Open config.json (or make it if it doesn't exist)
6. Put your DB connection string in `mongodb_url`

Make sure you make a gitignore for the config since it reveals your DB connection string (which can be exploited by others)!