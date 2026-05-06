import os
from backup.system_backup  import backup_system_config

def test_backup_system_creates_archive():
	archive_path = backup_system_config()
	assert os.path.exists(archive_path), "Backup archive was not created"
