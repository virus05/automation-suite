import pytest
from db.db import create_backup_record, get_recent_backups, verify_backup, delete_old_backup

@pytest.mark.integration
def test_create_and_read_backup_record():
    backup_id = create_backup_record("test", "/tmp/test.tar.gz")
    backups = get_recent_backups(limit=5)
    ids = [b[0] for b in backups]
    assert backup_id in ids
    
@pytest.mark.integration
def test_verify_backup():
    backup_id = create_backup_record("test", "/tmp/test2.tar.gz")
    verify_backup(backup_id)
    backups = get_recent_backups (limit=5)
    record = [b for b in backups if b[0] == backup_id][0]
    assert record[4] is True # verified column
    
@pytest.mark.integration
def test_delete_old_backups():
    # This assumes there are some old backups; in real tests you control time
    
    deleted = delete_old_backup(365)
    assert isinstance(deleted, int)