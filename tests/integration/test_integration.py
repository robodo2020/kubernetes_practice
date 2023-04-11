import os
import json
import requests

# TODO: get url from env
APP_URL = "http://localhost:8080"


def test_health_route():
    response = requests.get(f"{APP_URL}/health")
    assert response.status_code == 200
    assert response.content == b"OK"


def test_rps_route():
    mapping = ["Rock", "Paper", "Scissors"]
    for move in mapping:
        response = requests.post(
            f"{APP_URL}/rps",
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