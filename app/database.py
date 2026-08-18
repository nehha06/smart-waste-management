import sqlite3
import os

DATABASE = "database/waste.db"


def get_connection():
    os.makedirs("database", exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bin_id TEXT UNIQUE,
            location TEXT,
            fill_level INTEGER,
            temperature REAL,
            condition TEXT,
            priority TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bin_id TEXT,
            message TEXT,
            status TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM bins")

    if cursor.fetchone()[0] == 0:
        bins = [
            ("B101", "Zone 1", 92, 35, "NORMAL", "HIGH"),
            ("B102", "Zone 2", 68, 32, "NORMAL", "LOW"),
            ("B103", "Zone 3", 81, 37, "NORMAL", "MEDIUM"),
            ("B104", "Zone 4", 95, 70, "ABNORMAL", "HIGH")
        ]

        cursor.executemany("""
            INSERT INTO bins
            (bin_id, location, fill_level, temperature, condition, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, bins)

        alerts = [
            ("B104", "Abnormal temperature detected", "OPEN"),
            ("B101", "Bin requires collection", "OPEN"),
            ("B103", "Bin approaching capacity", "OPEN")
        ]

        cursor.executemany("""
            INSERT INTO alerts
            (bin_id, message, status)
            VALUES (?, ?, ?)
        """, alerts)

    connection.commit()
    connection.close()