from monitoring.ping_server import is_server_up

def test_is_server_up_true(monkeypatch):
    class FakeResult:
        returnedcode = 0
        
    def fake_run(cmd, capture_output):
        return FakeResult()
    
    monkeypatch.setattr("subprocess.run", fake_run)
    assert is_server_up ("localhost") is True