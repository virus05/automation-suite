# Automation Suite: Backup, Monitoring & Backup Metadata Tracking

## Overview for me

This project provides a Python-based automation suite to:

- Backup system config, Nginx, Django app, PostgreSQL DB, and app code.
- Monitor server availability and send email alerts.
- Log backup metadata into a PostgreSQL table (`backup_history`) using CRUD.
- Run on a schedule using systemd timers.
- Use GitHub and GitHub Actions for SCM and CI.

## Features

- Automated backups with timestamped archives.
- PostgreSQL backup via pg_dump.
- Server ping monitoring and email alerts.
- CRUD operations on backup_history table.
- TDD with pytest.
- CI pipeline using GitHub Actions.

## Architecture

(Insert ASCII diagram from the plan.)

## Setup

1. Clone the repository.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
