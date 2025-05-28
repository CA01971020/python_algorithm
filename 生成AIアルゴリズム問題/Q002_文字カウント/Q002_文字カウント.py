import collections

def count_characters(s: str):
    a = collections.Counter(s)
    print(a)

count_characters("banana")

print("----------")
# 例コード
def count_characters(s: str) -> None:
    # 出現回数を記録するための辞書を作成
    count_dict = {}
    
    # 文字ごとにループして出現回数をカウント
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # アルファベット順に並べて出力
    for char in sorted(count_dict):
        print(f"{char}: {count_dict[char]}")

count_characters("banana")
