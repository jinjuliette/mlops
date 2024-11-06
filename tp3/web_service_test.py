from fastapi.testclient import TestClient
import pytest
from web_service import app

client = TestClient(app)

@pytest.mark.parametrize(
    "data",
    [
        [6.1, 2.8, 4.7, 1.2],
    ],
)
def test_post_predict(data):
    response = client.post("/predict", json=data)
    print(response.json())
    assert response.status_code == 200

def test_post_update_model():
    model_uri = 'runs:/5e90a4a12f844c6bbcafdc172eade159/iris_model'
    
    response = client.post("/update-model", params={"new_model_uri": model_uri})
    print(response.json())
    assert response.status_code == 200

# def test_post_accept_next_model():
#     response = client.post("/accept-next-model")
    
#     print(response.json())
    
#     assert response.status_code == 200
#     assert response.json().get("status") == "next model accepted as current", "Next model was not accepted correctly"
