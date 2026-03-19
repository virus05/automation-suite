import shutil
import datetime
import os

def backup_bginx_config(src="/etc/nginx", dest="/var/backups/nginx"):
    """Create a compresed backup of the NGINX configuration directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(dest, exist_ok=True)
    base_name = os.path.join(dest, f"nginx_backup_{timestamp}")
    archive_path = shutil.make_archive(base_name, "gztar", src)
    return archive_path