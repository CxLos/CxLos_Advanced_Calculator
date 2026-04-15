# # ============ Imports =========== #

# import pytest
# from fastapi.testclient import TestClient
# from main import app

# # ============ Client =========== #

# client = TestClient(app)

# # ============ GET / =========== #

# def test_root_returns_html():
#     """GET / should return the index.html template (200 OK)"""
#     response = client.get("/")
#     assert response.status_code == 200

# # ============ GET /health =========== #

# def test_health_check():
#     """GET /health should return status healthy"""
#     response = client.get("/health")
#     assert response.status_code == 200
#     assert response.json() == {"status": "healthy"}

# # ============ POST /add =========== #

# def test_add_two_positive_numbers():
#     response = client.post("/add", json={"a": 10, "b": 5})
#     assert response.status_code == 200
#     assert response.json() == {"result": 15.0}

# def test_add_negative_numbers():
#     response = client.post("/add", json={"a": -3, "b": -7})
#     assert response.status_code == 200
#     assert response.json() == {"result": -10.0}

# def test_add_floats():
#     response = client.post("/add", json={"a": 1.5, "b": 2.5})
#     assert response.status_code == 200
#     assert response.json() == {"result": 4.0}

# def test_add_invalid_input():
#     response = client.post("/add", json={"a": "x", "b": 2})
#     assert response.status_code == 400

# # ============ POST /subtract =========== #

# def test_subtract_two_numbers():
#     response = client.post("/subtract", json={"a": 10, "b": 3})
#     assert response.status_code == 200
#     assert response.json() == {"result": 7.0}

# def test_subtract_resulting_in_negative():
#     response = client.post("/subtract", json={"a": 3, "b": 10})
#     assert response.status_code == 200
#     assert response.json() == {"result": -7.0}

# def test_subtract_floats():
#     response = client.post("/subtract", json={"a": 5.5, "b": 2.2})
#     assert response.status_code == 200
#     assert abs(response.json()["result"] - 3.3) < 0.0001

# def test_subtract_invalid_input():
#     response = client.post("/subtract", json={"a": 10, "b": "y"})
#     assert response.status_code == 400

#   # ============ POST /multiply =========== #

# def test_multiply_two_numbers():
#     response = client.post("/multiply", json={"a": 4, "b": 5})
#     assert response.status_code == 200
#     assert response.json() == {"result": 20.0}

# def test_multiply_by_zero():
#     response = client.post("/multiply", json={"a": 99, "b": 0})
#     assert response.status_code == 200
#     assert response.json() == {"result": 0.0}

# def test_multiply_negative_numbers():
#     response = client.post("/multiply", json={"a": -3, "b": 4})
#     assert response.status_code == 200
#     assert response.json() == {"result": -12.0}

# def test_multiply_invalid_input():
#     response = client.post("/multiply", json={"a": "z", "b": 5})
#     assert response.status_code == 400

# # ============ POST /divide =========== #

# def test_divide_two_numbers():
#     response = client.post("/divide", json={"a": 10, "b": 2})
#     assert response.status_code == 200
#     assert response.json() == {"result": 5.0}

# def test_divide_resulting_in_float():
#     response = client.post("/divide", json={"a": 7, "b": 2})
#     assert response.status_code == 200
#     assert response.json() == {"result": 3.5}

# def test_divide_by_zero_returns_400():
#     response = client.post("/divide", json={"a": 10, "b": 0})
#     assert response.status_code == 400
#     assert "error" in response.json()

# def test_divide_negative_dividend():
#     response = client.post("/divide", json={"a": -9, "b": 3})
#     assert response.status_code == 200
#     assert response.json() == {"result": -3.0}

# def test_divide_invalid_input():
#     response = client.post("/divide", json={"a": 10, "b": "z"})
#     assert response.status_code == 400
# # ===========================================================