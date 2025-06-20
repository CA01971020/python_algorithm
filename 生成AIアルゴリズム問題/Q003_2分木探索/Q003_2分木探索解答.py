class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_deepest_node(root: Node) -> str:
    # ここに実装を書く
    pass

# テスト用の木構造
root = Node("A",
            Node("B",
                 Node("D")),
            Node("C"))

print(find_deepest_node(root))  # 出力例: "D"