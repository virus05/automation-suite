import os
from datetime import datetime, timedelta

def _normalize_filename(name: str) -> str:
    """
    Convert something like:
    'a_202301001.tar.gz' → 'a_20230101.tar.gz'
    """
    prefix, rest = name.split("_", 1)
    date_part = rest.split(".")[0][:8]  # normalize to 8 digits
    extension = ".".join(rest.split(".")[1:])
    return f"{prefix}_{date_part}.{extension}"


def list_backups_sorted(backup_dir, extension=".tar.gz"):
    """Return normalized and sorted backup filenames."""
    files = [
        f for f in os.listdir(backup_dir)
        if f.endswith(extension)
    ]

    normalized = [_normalize_filename(f) for f in files]

    return sorted(normalized)


def find_latest_backup(backup_dir, prefix):
    """Return the latest normalized backup filename."""
    files = [
        f for f in os.listdir(backup_dir)
        if f.startswith(prefix)
    ]

    if not files:
        return None

    normalized = [_normalize_filename(f) for f in files]

    return max(normalized)


def is_older_than(file_path, days):
    """Check if a file is older than a given number of days."""
    mtime = os.path.getmtime(file_path)
    file_date = datetime.fromtimestamp(mtime)
    return file_date < datetime.now() - timedelta(days=days)
