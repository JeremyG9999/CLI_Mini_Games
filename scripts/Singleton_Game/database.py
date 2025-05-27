import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'leaderboards.db')

def setup_database():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS leaderboard (circle INTEGER, square INTEGER, triangle INTEGER)")
        cursor.execute("SELECT COUNT(*) FROM leaderboard")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO leaderboard (circle, square, triangle) VALUES (0, 0, 0)")
        conn.commit()

def update_score(shape):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if shape == "circle":
            cursor.execute("UPDATE leaderboard SET circle = circle + 1")
        elif shape == "square":
            cursor.execute("UPDATE leaderboard SET square = square + 1")
        elif shape == "triangle":
            cursor.execute("UPDATE leaderboard SET triangle = triangle + 1")
        conn.commit()

def retrieve_high_scores():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM leaderboard')
        scores = cursor.fetchall()
        for score in scores:
            print(f"\nCircle is {score[0]}")
            print(f"Square is {score[1]}")
            print(f"Triangle is {score[2]}\n")
    return scores

def delete_scores():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE leaderboard SET circle = 0, square = 0, triangle = 0")
        conn.commit()
