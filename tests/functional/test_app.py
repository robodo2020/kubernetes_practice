import json

from rock_paper_scissors.app import app


def test_health():
    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.data == b"OK"


def test_rps_invalid():
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps(dict(move="-1")), content_type="application/json"
        )
        assert response.status_code == 500


def test_rps(mocker):
    """
    Test Flask Application and API for Rock Paper Scissors
    """
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)

    mapping = ["Rock", "Paper", "Scissors"]
    for move in mapping:
        with app.test_client() as test_client:
            response = test_client.post(
                "/rps",
                data=json.dumps(dict(move=move)),
                content_type="application/json",
            )
            assert response.status_code == 200

            data = json.loads(response.data)

            result, game_result, pc_choice = (
                data["result"],
                data["game_result"],
                int(data["pc_choice"]),
            )
            if game_result == 0:
                assert result == "Tie"

            elif game_result == 1:
                assert result == f"You win, {move} beats {mapping[pc_choice]}"

            elif game_result == -1:
                assert result == f"I win, {mapping[pc_choice]} beats {move}"
