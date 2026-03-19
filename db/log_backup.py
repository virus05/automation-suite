from db.db import create_backup_record

def log_backup(backup_type, file_path):
    """
    Helper to log a backup run into the database.
    """
    return create_backup_record(backup_type, file_path)