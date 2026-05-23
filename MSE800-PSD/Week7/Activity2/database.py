import sqlite3
from fish import FISH_CATEGORIES

DB_FILE = "aquarium.db"


class Database:
    """Singleton — only one Database object is created for the whole app."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect(DB_FILE)
            cls._instance._setup_database()
        return cls._instance

    def _setup_database(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS fish_inventory ("
            "category TEXT PRIMARY KEY, "
            "count INTEGER DEFAULT 0, "
            "color TEXT, "
            "type TEXT)"
        )

        for category in FISH_CATEGORIES:
            self.conn.execute(
                "INSERT OR IGNORE INTO fish_inventory "
                "(category, count, color, type) VALUES (?, 0, '', '')",
                (category,),
            )
        self.conn.commit()

    def add_fish(self, category, amount, color, fish_type):
        self.conn.execute(
            "UPDATE fish_inventory "
            "SET count = count + ?, color = ?, type = ? "
            "WHERE category = ?",
            (amount, color, fish_type, category),
        )
        self.conn.commit()

    def get_inventory(self):
        cursor = self.conn.execute(
            "SELECT category, count, color, type "
            "FROM fish_inventory ORDER BY category"
        )
        return cursor.fetchall()

    def get_count(self, category):
        cursor = self.conn.execute(
            "SELECT count FROM fish_inventory WHERE category = ?", (category,)
        )
        row = cursor.fetchone()
        if row:
            return row[0]
        return 0
