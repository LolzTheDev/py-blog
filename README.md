# Py-Blog - By LolzTheDev

> What is Py-Blog?

Py-Blog is a simple project I made that lets people create blogs! You will need experience in MongoDB though, since this only ships the rendering and front-end.

You can use `post_creator.py` to format posts, but make sure to configure it from source first. If you want, you can check the comments and docstrings in `post_creator.py` for info on how posts are stored (only if you wish to make your own posting client).

Screenshots:
![Blog](static/images/examples/blog.png)

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
