import requests
import json

def is_server_healthy():
    ret = requests.get('https://example.org/healthcheck')
    ret.raise_for_status()
    return ret.json()['healthy']

def simulate_healthy_response():
    resp = requests.Response()
    resp.url = 'https://example.org/healthcheck'
    resp.status_code = 200
    resp._content = json.dumps({'healthy': True}).encode('utf-8')
    return resp

def test_healthy(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(requests, 'get', simulate_healthy_response())
        assert is_server_healthy()
