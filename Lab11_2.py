class Node:
    def __init__(self, term, explanation):
        self.term = term
        self.explanation = explanation
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def insert(self, term, explanation):
        if self.root is None:
            self.root = Node(term, explanation)
        else:
            self.root = self._insert_recursive(self.root, term, explanation)

    def _insert_recursive(self, node, term, explanation):
        if node is None:
            return Node(term, explanation)

        if term < node.term:
            node.left = self._insert_recursive(node.left, term, explanation)
        else:
            node.right = self._insert_recursive(node.right, term, explanation)

        return self._balance_node(node)

    def _balance_node(self, node):
        balance_factor = self.height(node.left) - self.height(node.right)

        if balance_factor > 1:
            if self.height(node.left.left) < self.height(node.left.right):
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        elif balance_factor < -1:
            if self.height(node.right.right) < self.height(node.right.left):
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def find(self, term):
        return self._find_recursive(self.root, term)

    def _find_recursive(self, node, term):
        if node is None or node.term == term:
            return node
        if term < node.term:
            return self._find_recursive(node.left, term)
        return self._find_recursive(node.right, term)

    def remove(self, term):
        self.root = self._remove_recursive(self.root, term)

    def _remove_recursive(self, node, term):
        if node is None:
            return node

        if term < node.term:
            node.left = self._remove_recursive(node.left, term)
        elif term > node.term:
            node.right = self._remove_recursive(node.right, term)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_right = self._find_min(node.right)
            node.term = min_right.term
            node.explanation = min_right.explanation
            node.right = self._remove_recursive(node.right, min_right.term)

        return self._balance_node(node)
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.left:
            self.display(node.left, level + 1)
        print(f"{' ' * 2 * level}{node.term}:\n{' ' * 2 * level}{node.explanation}\n")
        if node.right:
            self.display(node.right, level + 1)
            
        
def save_tree_to_file(tree, filename):
    data = tree.sorted_list()
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item['term']}|{item['explanation']}\n")

def load_tree_from_file(tree, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                term, explanation = line.strip().split('|', 1)
                tree.insert(term, explanation)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")

def input_term_and_explanation():
    term = input("Введіть термін: ").strip()
    explanation = input("Введіть пояснення: ").strip()
    return term, explanation

def menu():
    tree = BinarySearchTree()
    while True:
        print("1: Додати термін та пояснення")
        print("2: Знайти пояснення за терміном")
        print("3: Видалити термін")
        print("4: Відобразити дерево")
        print("5: Зберегти дерево в файл")
        print("6: Завантажити дерево з файлу")
        print("0: Вихід")

        choice = input("Введіть номер опції: ")

        if choice == "1":
            term = input("Введіть термін: ")
            explanation = input("Введіть пояснення: ")
            tree.insert(term, explanation)
        elif choice == "2":
            term = input("Введіть термін для пошуку: ")
            node = tree.find(term)
            if node:
                print(f"Пояснення: {node.explanation}")
            else:
                print("Термін не знайдено.")
        elif choice == "3":
            term = input("Введіть термін для видалення: ")
            tree.remove(term)
        elif choice == "4":
            tree.display()
        elif choice == "5":
            filename = input("Введіть ім'я файлу: ")
            save_tree_to_file(tree, filename)
        elif choice == "6":
            filename = input("Введіть ім'я файлу: ")
            load_tree_from_file(tree, filename)
        elif choice == "0":
            break
        else:
            print("Невірний номер опції, спробуйте ще раз.")

if __name__ == "__main__":
    menu()

