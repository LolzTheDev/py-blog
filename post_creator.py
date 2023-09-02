import pymongo, datetime, time, os

os.system("clear||cls")

"""
If you wish to contribute,
REMOVE THE DB_URL!!

And add this file to your .gitignore!

Feel free to use this to make posts.
Have fun!

(I recommend using this in a folder OUTSIDE of your server's folder).
"""

unix_timestamp = time.mktime(datetime.datetime.now().timetuple())

def main():
    """
    Create a post and add it to the database
    Every client must include:
        - Post title
        - Post author (configured in config.json)
        - Post content
        - Unix timestamp (time.mktime(datetime.datetime.now().timetuple()))
    """

    db_url = "<your-db-string>"

    mongo = pymongo.MongoClient(db_url)
    db = mongo["blogdb"]
    posts = db["posts"]

    print("- Create a new Post -")
    post_title = input("Title: ")
    post_author = input("Author: ")
    post_content = input("Content: ")

    posts.insert_one({
        'title': post_title,
        'author': post_author,
        'content': post_content,
        'date': int(unix_timestamp)
    })

if __name__ == "__main__":
    main()