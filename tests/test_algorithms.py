from backup.utils import list_backups_sorted, find_latest_backup
def test_list_backups_sorted(tmp_path):
    (tmp_path / "b_202401001.tar.gz"). write_text("x")
    (tmp_path / "a_202301001.tar.gz"). write_text("x")
    
    files = list_backups_sorted(str(tmp_path))
    assert files == ["a_20230101.tar.gz", "b_20240101.tar.gz"]
    
def test_find_latest_backup(tmp_path):
    (tmp_path / "sys_202301001.tar.gz"). write_text("x")
    (tmp_path / "sys_202401001.tar.gz"). write_text("x")
    
    latest = find_latest_backup(str(tmp_path), "sys_")
    assert latest == "sys_20240101.tar.gz"