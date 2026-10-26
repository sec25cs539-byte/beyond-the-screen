from app import app

def test_homepage_shows_project_and_tasks():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Beyond the Screen" in response.data
    assert b"Choose a guided task" in response.data

def test_tasks_api_returns_json_list():
    client = app.test_client()
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert {"id", "title", "steps"}.issubset(data[0].keys())

def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
