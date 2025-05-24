import sqlite3
import functools
import logging
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE """
def log_queries(func):
    @functools.wraps(func)
    def wrapper_log_queries(*args, **kwargs):
        logger = logging.getLogger(f'{func.__name__}()')
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        logger.info(f'is making a db query using {kwargs["query"]} at {datetime.now()}')
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
