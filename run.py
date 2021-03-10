# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.ramificacion_acotacion_search(ab).path())

# Result:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
