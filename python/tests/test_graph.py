from graph.graph import Graph, Vertex
import pytest

@pytest.fixture
def graphs():
    graph =Graph()
    v1 = graph.add_node("Pandora")
    v2 = graph.add_node("Arendelle")
    v3 = graph.add_node("Metroville")
    v4 = graph.add_node("Monstroplolis")
    v5 = graph.add_node("Narnia")
    v6 = graph.add_node("Naboo")

    graph.add_edge(v1,v2)

    graph.add_edge(v2,v1)
    graph.add_edge(v2,v3)
    graph.add_edge(v2,v4)

    graph.add_edge(v3,v2)
    graph.add_edge(v3,v4)
    graph.add_edge(v3,v5)
    graph.add_edge(v3,v6)


    graph.add_edge(v4,v2)
    graph.add_edge(v4,v3)
    graph.add_edge(v4,v6)

    graph.add_edge(v5,v3)
    graph.add_edge(v5,v6)

    graph.add_edge(v6,v3)
    graph.add_edge(v6,v4)
    graph.add_edge(v6,v5)
    return v1,graph

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected

def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected

def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected

def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

def test_breadth_first_search(graphs):
    """
    Successfully returns a collection of nodes in the order they were visited IN BFS approach.
    """
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

    actual = graphs[1].breadth_first_search(graphs[0])

    assert actual == expected
