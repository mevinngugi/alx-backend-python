import sqlite3
import functools

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE """
def log_queries(func):
    def wrapper_log_queries(*args, **kwargs):
        print("Log query before executing: ")
        print(f' Args: {args}' )
        print(f' Kwargs: {kwargs}' )
        print(kwargs["query"])
    return wrapper_log_queries

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
