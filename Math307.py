import igraph
##from igraph import plot
g = Graph()
g.add_vertices(7)
g.vs["name"] = ["Charleston", "Atlanta", "North Carolina", "Virgina", "Pennsylvania", "Michigan", "New York"]
g.es["miles"] = [259.04, 596.03, 168.73, 505.39, 204.88, 405.28, 339.67, 200.73, 508.21, 226.43, 213.12,
                 527.30, 367.34, 501]
g.es["minutes"] = [42, 89, 38, 54, 55, 68, 65, 36, 78, 42, 45, 79, 63, 78]
# 1 - Charleston
# 2 - Atlanta
# 3 - NC
# 4 - Virgina
# 5 - Pennsylvania
# 6 - Michigan
# 7 - New York
g.add_edges([(0,1), (1,6), (0,2), (2,3), (3,4), (3,5), (4,6), (4,5), (5,6), (1,2), (3,6),
             (1,4), (2,4), (2,5)])
style = [(300, 360), (200, 400), (325, 300), (350,250), (375, 200), (225,100), (360, 100)]
visual_style = {}
visual_style["vertex_size"] = 20
visual_style["bbox"] = (500, 500)
visual_style["margin"] = 50
visual_style["vertex_label"] = g.vs["name"]
visual_style["layout"] = style
visual_style["vertex_label_dist"] = 1
plot(g, **visual_style)
print(g.get_adjacency())
