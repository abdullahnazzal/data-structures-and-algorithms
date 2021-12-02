from collections import deque

class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """
    def __init__(self, value):
        """
        Initalization for a Vertex to hold a value.
        """
        self.value = value

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.

		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

    """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        """
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection
        """
        output = []
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            output.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return output

    def depth_first(self,start_vertex):
        """
        Arguments: Node (Starting point of search)
        Return: A collection of nodes in their pre-order depth-first traversal order
        Program output: Display the collection
        """
        output = []
        stack = Stack()
        visited = set()

        stack.push(start_vertex)


        while len(stack):
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                output.append(current_vertex.value)

                for edge in neighbors:
                    neighbor = edge.vertex
                    if neighbor not in visited:
                        stack.push(neighbor)

        return output







    # def is_reachable(self, vertexOne, vertexTwo):
    #     # Base case
    #     if (vertexOne == vertexTwo):
    #         return True

    #     # Mark all the vertices as not visited
    #     # visited = [False for i in range(V)]
    #     queue = Queue()
    #     visited = set()

    #     queue.enqueue(vertexOne)
    #     visited.add(vertexOne)

    #     # Mark the current node as visited and enqueue it
    #     # visited[s] = True
    #     # queue.append(s)

    #     while (len(queue) > 0):

    #         # Dequeue a vertex from queue and print
    #         s = queue.popleft()
    #         # queue.pop_front()

    #         # Get all adjacent vertices of the dequeued vertex s
    #         # If a adjacent has not been visited, then mark it
    #         # visited  and enqueue it
    #         for i in adj[s]:

    #             # If this adjacent node is the destination node,
    #             # then return true
    #             if (i == d):
    #                 return True

    #             # Else, continue to do BFS
    #             if (not visited[i]):
    #                 visited[i] = True
    #                 queue.append(i)
    #     # If BFS is complete without visiting d
    #     return False
    def is_reachable(self, vertexOne, vertexTwo):
        output = []
        queue = Queue()
        visited = set()

        queue.enqueue(vertexOne)
        visited.add(vertexOne)

        while len(queue):
            current_vertex = queue.dequeue()
            output.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return output
# graph =Graph()
# v1 = graph.add_node("Pandora")
# v2 = graph.add_node("Arendelle")
# v3 = graph.add_node("Metroville")
# v4 = graph.add_node("Monstroplolis")
# v5 = graph.add_node("Narnia")
# v6 = graph.add_node("Naboo")

# graph.add_edge(v1,v2,150)
# graph.add_edge(v1,v3,82)

# graph.add_edge(v2,v1,150)
# graph.add_edge(v2,v3,99)
# graph.add_edge(v2,v4,42)

# graph.add_edge(v3,v1,82)
# graph.add_edge(v3,v2,99)
# graph.add_edge(v3,v4,105)
# graph.add_edge(v3,v5,37)
# graph.add_edge(v3,v6,250)


# graph.add_edge(v4,v2,42)
# graph.add_edge(v4,v3,105)
# graph.add_edge(v4,v6,73)

# graph.add_edge(v5,v3,37)
# graph.add_edge(v5,v6,250)

# graph.add_edge(v6,v3,26)
# graph.add_edge(v6,v4,73)
# graph.add_edge(v6,v5,250)

# print(graph_business_trip(graph,[v1,v6]))
