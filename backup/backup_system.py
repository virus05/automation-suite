import shutil
import datetime
import os

def backup_system_config(src="/etc", dest="/var/backups/system"):
    """Create a compresed backup of the system configuration directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(dest, exist_ok=True)
    base_name = os.path.join(dest, f"system_backup_{timestamp}")
    archive_path = shutil.make_archive(base_name, "gztar", src)
    return archive_path