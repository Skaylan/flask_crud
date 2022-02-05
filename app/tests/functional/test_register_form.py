from app import app


def test_register_form():
    with app.test_client() as test_client:
        response = test_client.get('/register')
        assert response.status_code == 200
        