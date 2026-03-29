import os
from datetime import datetime, timedelta

def _normalize_filename(name: str) -> str:
    """
    Convert something like:
    'a_202301001.tar.gz' → 'a_20230101.tar.gz'
    """
    prefix, rest = name.split("_", 1)
    raw_date = rest.split(".")[0]

    # Correct normalization:
    # first 6 digits (YYYYMM) + last 2 digits (DD)
    date_part = raw_date[:6] + raw_date[-2:]

    extension = ".".join(rest.split(".")[1:])
    return f"{prefix}_{date_part}.{extension}"


def list_backups_sorted(backup_dir, extension=".tar.gz"):
    files = [
        f for f in os.listdir(backup_dir)
        if f.endswith(extension)
    ]

    normalized = [_normalize_filename(f) for f in files]

    return sorted(normalized)


def find_latest_backup(backup_dir, prefix):
    files = [
        f for f in os.listdir(backup_dir)
        if f.startswith(prefix)
    ]

    if not files:
        return None

    normalized = [_normalize_filename(f) for f in files]

    return max(normalized)


def is_older_than(file_path, days):
    mtime = os.path.getmtime(file_path)
    file_date = datetime.fromtimestamp(mtime)
    return file_date < datetime.now() - timedelta(days=days)
