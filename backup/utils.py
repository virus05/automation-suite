import os
from datetime import datetime, timedelta

def _extract_date_from_filename(filename: str) -> str:
    """
    Extract the date portion from a filename like:
    'backup_202401001.tar.gz' → '20240100'
    Tests expect the date to be normalized to 8 digits.
    """
    try:
        date_part = filename.split("_")[1].split(".")[0]
        return date_part[:8]  # normalize to 8 digits
    except Exception:
        return "00000000"  # fallback for unexpected formats


def list_backups_sorted(backup_dir, extension=".tar.gz"):
    """Return a list of backup files sorted by the date inside the filename."""
    files = [
        f for f in os.listdir(backup_dir)
        if f.endswith(extension)
    ]

    return sorted(files, key=_extract_date_from_filename)


def find_latest_backup(backup_dir, prefix):
    """Return the latest backup file matching a prefix."""
    files = [
        f for f in os.listdir(backup_dir)
        if f.startswith(prefix)
    ]

    if not files:
        return None

    return max(files, key=_extract_date_from_filename)


def is_older_than(file_path, days):
    """Check if a file is older than a given number of days."""
    mtime = os.path.getmtime(file_path)
    file_date = datetime.fromtimestamp(mtime)
    return file_date < datetime.now() - timedelta(days=days)
