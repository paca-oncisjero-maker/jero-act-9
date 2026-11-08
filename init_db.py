import sqlite3
import os

DATABASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "students.db"
)

conn = sqlite3.connect(DATABASE)

conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        name TEXT NOT NULL,
        program TEXT NOT NULL,
        year INTEGER NOT NULL,
        section TEXT NOT NULL,
        source TEXT DEFAULT 'Local'
    )
""")

columns = [row[1] for row in conn.execute("PRAGMA table_info(students)")]
if "source" not in columns:
    conn.execute("ALTER TABLE students ADD COLUMN source TEXT DEFAULT 'Local'")
    conn.execute("UPDATE students SET source = 'Local' WHERE source IS NULL")

# Reset to five fictional practice records.
conn.execute("DELETE FROM students")
conn.execute("DELETE FROM sqlite_sequence WHERE name = 'students'")
conn.executemany(
    "INSERT INTO students (student_id, name, program, year, section, source) "
    "VALUES (?, ?, ?, ?, ?, ?)",
    [
        ("24-00115", "Jero Paca-oncis", "BSIT", 3, "DIJKSTRA", "Local"),
        ("24-00116", "Missy Miranda", "BSIT", 3, "DIJKSTRA", "Local"),
        ("24-00117", "Hapee Malunes", "BSIT", 3, "DIJKSTRA", "Local"),
        ("24-00118", "Ana Garcia", "BSIT", 3, "KRUSKAL", "Local"),
        ("24-00119", "Mark Lopez", "BSIT", 3, "KRUSKAL", "Local"),
    ],
)

conn.commit()
conn.close()

print("Database initialized successfully!")
