from time import perf_counter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

        self.start = None
        self.finish = None
        self.G = None

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def get_nx_graph(self):
        if self.G:
            return self.G
        self.G = nx.Graph()

        for i in range(len(self.list_view)):
            for j in range(len(self.list_view[i])):
                if self.list_view[i][j] != '#':
                    if self.list_view[i][j] == 'O':
                        self.start = (i, j)
                    if self.list_view[i][j] == 'X':
                        self.finish = (i, j)
                    if i + 1 < len(self.list_view) and self.list_view[i + 1][j] != '#':
                        self.G.add_edge((i, j), (i + 1, j))
                    if j + 1 < len(self.list_view[i]) and self.list_view[i][j + 1] != '#':
                        self.G.add_edge((i, j), (i, j + 1))
        return self.G

    def draw_graph(self):
        self.G = self.get_nx_graph()
        pos = dict()
        for i, j in set(self.G):
            pos[(i, j)] = np.array([j, -i])
        nx.draw(self.G, pos, with_labels=True)
        plt.show()

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"
    G = maze.get_nx_graph()
    node_reverse_paths = dict()
    for node1, node2 in nx.bfs_edges(G, source=maze.start):
        node_reverse_paths[node2] = node1

    x = maze.finish
    while x != maze.start:
        path += _get_step(node_reverse_paths[x], x)
        x = node_reverse_paths[x]
    path = path[:: -1]

    print(f"Found: {path}")
    maze.print(path)

def _get_step(node1, node2):
    if node1[0] > node2[0]:
        return 'U'
    elif node1[0] < node2[0]:
        return 'D'
    elif node1[1] < node2[1]:
        return 'R'
    else:
        return 'L'


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    maze.draw_graph()
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
