import os
from datetime import datetime, timedelta

def list_backups_sorted(backup_dir, extension=".tar.gz"):
    """Return a sorted list of backup files in a directory.
    Sorting is by filename, which includes a timestamp."""
    
    files = [
        f for f in os.listdir(backup_dir)
        if f.endswith(extension)
    ]
    return sorted(files)

def find_latest_backup(backup_dir, prefix):
    """Find the latest backup file with a given prefix."""
    
    files = list_backups_sorted(backup_dir)
    candidates = [f for f in files if f.startswith(prefix)]
    if not candidates:
        return None
    return candidates[-1]

def is_older_than(file_path, days):
    """Check if a file is older than a given number of days."""
    
    mtime = os.path.getmtime(file_path)
    file_date = datetime.fromtimestamp(mtime)
    return file_date < datetime.now() - timedelta(days=days) 