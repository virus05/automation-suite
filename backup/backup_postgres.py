import subprocess
import datetime
import os

def backup_postgres_db(db_name, dest="/var/backups/postgres"):
    """Use pg_dump to create a backup of the PostgreSQL database."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(dest, exist_ok=True)
    output_file = os.path.join(dest, f"{db_name}_{timestamp}.sql")
    cmd = ["pg_dump", db_name, "-f", output_file]
    subprocess.run(cmd, check=True)
    return output_file