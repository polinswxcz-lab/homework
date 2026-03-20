import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
)
""")

conn.commit()

books = [
    ("1984", "George Orwell"),
    ("Harry Potter", "J.K. Rowling"),
    ("The Hobbit", "J.R.R. Tolkien")
]

cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books)
conn.commit()

cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()

for book in all_books:
    print(book)

book_id = int(input("введи id книги для видалення"))

cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
conn.commit()

print("книгу видалено")

conn.close()