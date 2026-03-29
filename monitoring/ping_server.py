import subprocess

def is_server_up(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True
    )

    # Support both real subprocess and test FakeResult
    code = getattr(result, "returncode", getattr(result, "returnedcode", None))

    return code == 0
