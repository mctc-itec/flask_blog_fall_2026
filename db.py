import sqlite3      
from datetime import datetime 
from model import Post 

database_file = 'posts.db'
create_table_sql = 'CREATE TABLE IF NOT EXISTS posts (user_id STRING, title STRING, text STRING, date INT)'
insert_post_sql = 'INSERT INTO posts VALUES (?, ?, ?, ?)'
get_all_posts_for_user_sql = 'SELECT * FROM posts WHERE user_id = ?'


with sqlite3.connect(database_file) as db:
    db.execute(create_table_sql)


def new_post(post):
    # add the current timestamp as a number if one is not provided
    # SQLlite doesn't have a date type, so store the timestamp as a float
    post_datetime = post.post_datetime or datetime.now()
    timestamp = post_datetime.timestamp()

    with sqlite3.connect(database_file) as db:
        db.execute(insert_post_sql, (post.user_id, post.title, post.text, timestamp))


def get_all_posts_for_user(user_id):
    db = sqlite3.connect(database_file)
    rows = db.execute(get_all_posts_for_user_sql, (user_id, )).fetchall()
    # Create a Post object for each row returned from the database query 
    # Create a datetime object from the float timestamp
    posts = [ Post(row[0], row[1], row[2], datetime.fromtimestamp(row[3])) for row in rows ]
    return posts 

