
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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

    def dfs(self, starting_vertex):
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
        l = []
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            #print('path', path)
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            #print('last_vertex', last_vertex)
            
            # Check if there's no ancestor and append the whole path
            if self.vertices[last_vertex] == set():
                l.append(path)

            # If that vertex has not been visited...
            if last_vertex not in visited:
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
                    #print(s.stack)

        # Return longest path
        length = len({len(i) for i in l})
        if len(l) > 1 and length == 1:
          return l[0][-1]
        elif len(l) > 1:
          prev = l[0]
          for i in l[1:]:
            if len(prev) < len(i):
              prev = i
          return i[-1]
        else:
          if len(l[0]) > 1:
            return l[0][-1]
          else:
            # If None
            return -1

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for i in range(1,12):
        g.add_vertex(i)

    for j in ancestors:
        g.add_edge(j[1], j[0])

    return g.dfs(starting_node)