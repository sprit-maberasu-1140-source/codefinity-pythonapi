import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)          # ネットからデータを取ってくる
        response.raise_for_status()           # HTTPのエラーがあれば例外を出す
        data = response.json()                # 取ってきたデータを辞書に変える
        print(data["fact"])                   # 猫の豆知識を画面に出す
    except Exception:
        print("Failed to retrieve cat fact.")  # 失敗したときのメッセージ

get_cat_fact()