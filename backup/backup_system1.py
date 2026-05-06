import tarfile
import datetime
import os

def backup_system_config(src, dest):
	os.makedirs(dest, exist_ok=True)
	timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
	archive_path = os.path.join(dest, f"etc-backup-{timestamp}.tar.gz")

	with tarfile.open(archive_path, "w:gz") as tar:
		tar.add(src, arcname="etc")
	return archive_path
