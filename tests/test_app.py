import sys
import os

# Add the app folder to Python path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_bins_api(client):
    response = client.get("/api/bins")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_alerts_api(client):
    response = client.get("/api/alerts")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)


def test_waste_analysis(client):
    response = client.get(
        "/api/analyze/95/70"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["condition"] == "ABNORMAL"
    assert data["priority"] == "HIGH"