import sqlite3


def create_database():

    conn = sqlite3.connect(
        "placement_ai.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            candidate_name TEXT,

            match_score REAL,

            prediction TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_candidate(
    candidate_name,
    match_score,
    prediction
):

    conn = sqlite3.connect(
        "placement_ai.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates (

            candidate_name,
            match_score,
            prediction

        )

        VALUES (?, ?, ?)
    """, (
        candidate_name,
        match_score,
        prediction
    ))

    conn.commit()
    conn.close()