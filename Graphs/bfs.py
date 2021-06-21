from typing import Dict, List, Set

class Graph:
    def __init__(self) -> None:
        self.vertices: Dict[int, List[int]] = {}

    def print_graph(self) -> None:
        for i in self.vertices:
            print(i, " : ", "->".join([str(j) for j in self.vertices[i]]))

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]

    def bfs(self, start_vertex: int) -> Set[int]:
        """
            g = Graph()
            g.add_edge(0,1)
            g.add_edge(0,1)
            g.add_edge(0,2)
            g.add_edge(1,2)
            g.add_edge(2,0)
            g.add_edge(2,3)
            g.add_edge(3,3)
            sorted(g.bfs(2))
        """
        visited = set()     # intialize set for storing visited vertices

        queue = []          # queue to store all vertices for bfs

        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            vertex = queue.pop(0)

            # loop through all adjacent vertices and add to queue if not yet visited
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.add(adjacent_vertex)
        return visited


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)

    g.print_graph()

    assert sorted(g.bfs(0)) == [0, 1, 2, 3]