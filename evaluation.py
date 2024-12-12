import requests

def getBestMove(FEN):
    url = 'https://chess-api.com/v1'
    data = {
        'fen': FEN
    }

    response = requests.post(url, json=data)

    return response.json()['text']