from fastapi.testclient import TestClient
from cenv.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'region': 'us-central1', 'sku': 'starter'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'region': 'us-central1', 'sku': 'unlimited'}).json()
    assert bad["passed"] is False
    assert "sku" in bad["failed"]
