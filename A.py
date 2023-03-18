def star(graph,start,end):
    def h(node):
        return ((node[0] - end[0])**2 + (node[1] - end[1])**2)**0.5
    boundary = {start}
    length=len(boundary)
    comefrom = {}
    gvalues = {start: 0}
    dist = {start: 0}
    while  length> 0:
        current = min(boundary, key=lambda x: gvalues[x] + h(x))
        boundary.remove(current)
        if current == end:
            path = [end] 
            while (path[-1] != start):
                path.append(comefrom[path[-1]])
            path.reverse()
            return path,gvalues[end]
        for neighbors in graph[current]:
            g = gvalues[current] + 1
            if neighbors not in gvalues or gvalues[neighbors] > g:
                gvalues[neighbors] = g
                dist[neighbors] = dist[current] + 1
                boundary.add(neighbors)
                comefrom[neighbors] = current
#adjacency list ex:
#graph A,B,C,D,E,F,G,H,I
graph = {
    (0, 0): [(0,1), (1,2)],
    (0, 1): [(0,0), (1,1),(0,2),(1,2)],
    (0, 2): [(0,1),(2,0),(1,1),(1,0)],
    (1, 0): [(0,2), (2,0)],
    (1, 2): [(0,0), (0,1),(1,1),(2, 0),(2,1)],
    (1, 1): [(0,1), (1,2), (2,0),(0,2)],
    (2, 0) : [(2,2),(1,2),(1,1),(0,2),(1,0)], 
    (2, 1): [(1,2)],
    (2,2): [(2,0)]
}

#start , end point:
start = (0,0 )
end = (1, 0)
c,p = star(graph, start, end)
print(c)
print(p)
####output:[(0, 0), (1, 2), (2, 0), (1, 0)]
####3
