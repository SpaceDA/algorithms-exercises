from dijkstra_two_stack import Evaluate


def test_two_stack():
    a = Evaluate()
    assert a.main("(1+((2+1)*(3+1)))") == 13