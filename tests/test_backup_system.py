import os
from backup.backup_system import backup_system_config

def test_backup_system_create_archive (tmp_path, monkeypatch) :
    # Use a tmp src directory
    src = tmp_path / "etc"
    src.mkdir()
    (src / "config.txt").write_text("test")
    
    dest = tmp_path / "backups"
    
    backup_file = backup_system_config(str(src), str(dest))
    
    assert backup_file.endswith(".tar.gz")
    assert os.path.exists(backup_file)