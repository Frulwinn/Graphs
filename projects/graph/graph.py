"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        """
        Add a vertex to the graph.
        """
        #pass  # TODO

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise IndexError("Hey, that vertex doesn't exist!")
        """
        Add a directed edge to the graph.
        """
        #pass  # TODO

    def bft(self, starting_vertex):
        #keep track of all visited nodes
        explored = []

        #keep track of nodes to be checked
        queue = [starting_vertex]

        #keep looping until there are nodes still to be checked
        while queue:
            #pop first node from queue
            node = queue.pop(0)
            if node not in explored:
                #add node to list of checked nodes
                explored.append(node)
                neighbours = starting_vertex[node]

                #add neighbourgs of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)

        return explored

        """
        BFT
        
        # Create an empty STACK and push the starting vertex ID
        # Create a set to store visited vertices
            # While the queue is not empty...
                # POP the firxt vertex
                # if that vertex has not been visted ...
                    # Mark it as visted ...
                    # Then PUSH all of its neighbors to the back of the Queue

        Print each vertex in breadth-first order
        beginning from starting_vertex.
        #create an empty queue and enqueue the starting vertex ID
        q = Queue()

        #create a set to store visited vertices
        visited = set()

        #while the queue is not empty...
        while queue.size() > 0:
            #dequeue the first vertex
            vertex = queue.dequeue()

            #if the vertex has not been visited...
            if vertext not in visited:
                print(vertext)

                #mark it as visited ... you can just use the .add syntax for sets, very useful!
                visited.add(vertex)

                #then add all of its neighbors to the back of the queue
                for neighbors in self.vertices(v):
                    queue.enqueue(neighbor)

        """
        #pass  # TODO

    def dft(self, starting_vertex):
        #create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)

        #create a set to store visited vertices
        visited = set()

        #while the queue is not empty...
        while stack.size() > 0:

            #pop the first vertex
            vertex = stack.pop()
            #print(vertex)

            #if vertex has not been visited ...
            if vertex not in visited:
                #Mark it as visited ...
                #Then push all of its neighbors to the back of the stack
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        # DFT
        # Create an empty STACK and push the starting vertex ID
        # Create a set to store visited vertices
            # While the queue is not empty...
                # POP the firxt vertex
                # if that vertex has not been visted ...
                    # Mark it as visted ...
                    # Then PUSH all of its neighbors to the back of the STACK


        """
        #pass  # TODO

    def dft_recursive(self, starting_vertex):
        stack = [starting_vertex]
        path = []

        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)

            for neighbor in self.vertices[vertex]:
                stack.append(neighbor) 

        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





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
