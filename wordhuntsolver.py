import os
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def add_word(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class BoggleSolver:
    def __init__(self, board_string, width=4, height=4):
        self.width = width
        self.height = height
        self.board = [board_string[i:i+width] for i in range(0, len(board_string), width)]
        self.found_words = set()
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.trie = TrieNode()

    def in_bounds(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width

    def dfs(self, x, y, path, visited, trie_node):
        if (x, y) in visited:
            return

        visited.add((x, y))
        path += self.board[x][y]

        next_trie_node = trie_node.children.get(self.board[x][y])
        if not next_trie_node:
            visited.remove((x, y))
            return

        if next_trie_node.is_end_of_word and len(path) >= 4:
            self.found_words.add(path)

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny):
                self.dfs(nx, ny, path, visited, next_trie_node)

        visited.remove((x, y))

    def load_dictionary(self, file_path):
        with open(file_path, 'r') as file:
            for word in file:
                self.trie.add_word(word.strip().lower())

    def solve(self):
        for x in range(self.height):
            for y in range(self.width):
                self.dfs(x, y, "", set(), self.trie)
        return sorted(self.found_words, key=len, reverse=True)

if __name__ == "__main__":
    try:
        board_string = input("Enter the board letters from left to right, top down (e.g., 'aeagmirctoynptnl'): ").lower()
        if len(board_string) != 16:
            print("Invalid board size. Please enter exactly 16 characters.")
        else:
            solver = BoggleSolver(board_string)
            solver.load_dictionary(r'C:\<directory>\words.txt')

            start_time = time.time()
            words = solver.solve()
            end_time = time.time()

            print(f"Found {len(words)} words in {end_time - start_time:.2f} seconds:")
            for word in words:
                print(word)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("\nPress Enter to close the program...")
