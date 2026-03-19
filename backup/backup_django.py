import shutil
import datetime
import os

def backup_django_app(src="/var/www/myapp", dest="/var/backups/django"):
    """Create a compresed backup of the Django application folder."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(dest, exist_ok=True)
    base_name = os.path.join(dest, f"django_backup_{timestamp}")
    archive_path = shutil.make_archive(base_name, "gztar", src)
    return archive_path