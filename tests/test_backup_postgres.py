import os
from backup.backup_postgres import backup_postgres_db

def test_backup_postgres_creates_file(tmp_path, monkeypatch):
    def fake_run(cmd, check):
        #Simulate pg_dump by creating an empty file
        
        output_index = cmd.index("-f") + 1
        open(cmd[output_index], "w").close()
        
    monkeypatch.setattr("subprocess.run", fake_run)
    
    dest = tmp_path / "pg"
    
    dest.mkdir()
    
    backup_fie = backup_postgres_db("testdb", str(dest))
    
    assert backup_fie.endswith(".sql")
    assert os.path.exists(backup_fie)