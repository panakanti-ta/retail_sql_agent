import sqlite3
from src.config import DB_PATH
from src.safety import validate_sql

def run_select_query(sql: str) -> list[dict]:
    safe_sql = validate_sql(sql)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(safe_sql)
    rows = [dict(row) for row in cursor.fetchall()]
    
    cursor.close()
    conn.close()
    return rows
