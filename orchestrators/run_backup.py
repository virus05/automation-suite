from backup.backup_system import backup_system_config
from backup.backup_nginx import backup_bginx_config
from backup.backup_django import backup_django_app
from backup.backup_postgres import backup_postgres_db
from db.log_backup import log_backup

def main():
    #System config
    system_backup = backup_system_config()
    log_backup("system", system_backup)
    
    #Nginx
    nginx_backup = backup_bginx_config()
    log_backup("system", nginx_backup)
    
    #Django app
    djngo_backup = backup_django_app()
    log_backup("django", djngo_backup)
    
    #PostgreSQL DB
    postgres_backup = backup_postgres_db("mydb")
    log_backup("postgres", postgres_backup)

if __name__ == "__main__":
    main()
    