from graph.graph_trip import Graph,business_trip
import pytest
@pytest.fixture
def graph_trip():
    graph =Graph()
    v1 = graph.add_node("Pandora")
    v2 = graph.add_node("Arendelle")
    v3 = graph.add_node("Metroville")
    v4 = graph.add_node("Monstroplolis")
    v5 = graph.add_node("Narnia")
    v6 = graph.add_node("Naboo")

    graph.add_edge(v1,v2,150)
    graph.add_edge(v1,v3,82)

    graph.add_edge(v2,v1,150)
    graph.add_edge(v2,v3,99)
    graph.add_edge(v2,v4,42)

    graph.add_edge(v3,v1,82)
    graph.add_edge(v3,v2,99)
    graph.add_edge(v3,v4,105)
    graph.add_edge(v3,v5,37)
    graph.add_edge(v3,v6,250)


    graph.add_edge(v4,v2,42)
    graph.add_edge(v4,v3,105)
    graph.add_edge(v4,v6,73)

    graph.add_edge(v5,v3,37)
    graph.add_edge(v5,v6,250)

    graph.add_edge(v6,v3,26)
    graph.add_edge(v6,v4,73)
    graph.add_edge(v6,v5,250)
    return graph,v1,v2,v3,v4,v5,v6
def test_business_trip(graph_trip):
    """
    Successfully returns a.
    """
    expected1 = (True,'$82')
    actual1 = business_trip(graph_trip[0],[graph_trip[3], graph_trip[1]])

    expected2 = (True,'$115')
    actual2 = business_trip(graph_trip[0],[graph_trip[2], graph_trip[4],graph_trip[6]])

    expected3 = (False,'$0')
    actual3 = business_trip(graph_trip[0],[graph_trip[6], graph_trip[1]])

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
