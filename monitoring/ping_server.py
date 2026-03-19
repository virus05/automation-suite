import subprocess

def is_server_up(host):
    """Ping a host once and return True is is reachable."""
    
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True
    )
    return result.returncode == 0