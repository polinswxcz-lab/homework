from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        due_date TEXT,
        due_time TEXT,
        created_at TEXT,
        completed INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/planner')
def planner():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('planner.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    due_time = request.form.get('due_time')

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title, description, due_date, due_time, created_at) VALUES (?, ?, ?, ?, ?)",
        (title, description, due_date, due_time, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()

    return redirect(url_for('planner'))

@app.route('/complete/<int:id>')
def complete_task(id):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET completed = 1 WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('planner'))

@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('planner'))

if __name__ == "__main__":
    app.run(debug=True)