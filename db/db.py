import psycopg2
from contextlib import contextmanager

DB_CONFIG = {
    "dbname" : "mydb",
    "user" : "myuser",
    "password" : "mypassword",
    "host" : "localhost",
    "port" : 5432,
}

@contextmanager
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

def create_backup_record(backup_type, file_path):
    """
    CREATE: Insert a new backup record.
    """
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO backup_history (backup_type, file_path)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (backup_type, file_path)
        )
        backup_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    return backup_id

def get_recent_backups(limit=10):
    """READ: Get the most recent backups."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT id, backup_type, file_path, created_at, verified
            FROM backup_history
            ORDER BY created_at DESC
            LIMIT %s;
            """,
            (limit,),
        )
        rows = cur.fetchall()
        cur.close()
    return rows


def verify_backup(backup_id):
    """UPDATE: Mark a backup as verified."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE backup_history
            SET verified = TRUE
            WHERE id = %s;
            """,
            (backup_id,),
        )
        conn.commit()
        cur.close()


def delete_old_backup(days):
    """DELETE: Remove backups older than a given number of days."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM backup_history
            WHERE created_at < NOW() - INTERVAL '%s days';
            """ % days
        )
        deleted = cur.rowcount
        conn.commit()
        cur.close()
    return deleted

