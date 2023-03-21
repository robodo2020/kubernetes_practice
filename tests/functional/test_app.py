import json

from rock_paper_scissors.app import app


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """


    with app.test_client() as test_client:
        response = test_client.post('/rps',
                                    data=json.dumps(dict(move='Rock')),
                                    content_type='application/json')
        assert response.status_code == 200
