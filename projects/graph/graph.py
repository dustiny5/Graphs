"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('The vertex does not exist.')
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create an empty set to store visited verticies
        visted = set()

        # While the queue is not empty...
        while q.size() > 0 :

            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertex has not been visted...
            if v not in visted:

                # Mark it as visted
                print(v)
                visted.add(v)

                # Then add all of its neighbors to the back of the queue
                for neighbor in self.verticies[v]:
                    q.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visted vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:

            # Pop the first vertex
            v = s.pop()

            # If that vertex has not been visted...
            if v not in visited:

                # Mark it as visited...
                print(v)
                visited.add(v)

                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Initialize visited, if it hasn't been initialized yet
        if not visited:
            visited = set()

        if neighbor not in visited:
            # Print vertex
            print(starting_vertex)
            # Mark as visited
            visited.add(starting_vertex)
            # Loop through connected vertex
            for neighbor in self.vertices[starting_vertex]:
                # Call DFT recursion
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            #print('path', path)
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            #print('last_vertex', last_vertex)
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(last_vertex)
                #print('visited', visited)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[last_vertex]:
                  # COPY THE PATH
                  copy_path = list(path)
                  copy_path.append(neighbor)
                  # APPEND THE NEIGHOR TO THE BACK
                  q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            #print('path', path)
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            #print('last_vertex', last_vertex)
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(last_vertex)
                #print('visited', visited)
                # Then add A PATH TO its neighbors to the back of the stack
                for neighbor in self.vertices[last_vertex]:
                  # COPY THE PATH
                  copy_path = list(path)
                  copy_path.append(neighbor)
                  # APPEND THE NEIGHOR TO THE BACK
                  s.push(copy_path)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
