import requests

def print_three_cat_facts():
    # ① 3回くり返す
    for _ in range(3):
        # ② API（猫の豆知識サービス）に「GET」リクエストを送る
        response = requests.get("https://catfact.ninja/fact")
        # ③ 返ってきたJSONを辞書にする
        data = response.json()
        # ④ “fact”（豆知識）の中身を取り出して表示
        print(data["fact"])

print_three_cat_facts()