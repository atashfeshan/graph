from collections import OrderedDict
# g = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [4, 8, 2, 6], 6: [3], 7: [4, 8], 8: [5, 9, 7], 9: [8, 6]}

g = {
    1: [2, 4],
    2: [1, 5],
    3: [],
    4: [7, 5, 1],
    5: [6, 4, 2],
    6: [5, 9],
    7: [4],
    8: [],
    9: [6]
}
class Nearest:
    def __init__(self):
        self.address = []
        self.node = 0

    @staticmethod
    def flatten(list_input):
        return list(set([y for x in list_input for y in x]))

    def way(self, graph, node, end):
        self.node = node
        node_now = graph[node]
        if end in graph[node]:
            return graph[node][graph[node].index(end)]
        connection = []
        for i in graph[node]:
            connection.append(graph[i])
        temp = graph[node]
        graph[node] = self.flatten(connection)
        for j in temp:
            if j in graph[node]:
                graph[node].remove(j)
        point = self.way(graph, node, end)
        if node in node_now:
            node_now.remove(node)
        self.address.append(point)
        for i in node_now:
            if point in graph[i]:
                self.address.append(i)
                return i

    def give_address(self):
        self.address = list(OrderedDict.fromkeys(self.address))
        self.address.append(self.node)
        self.address.reverse()
        return self.address


# find nearest way from node 1 to node 9
way = Nearest()
way.way(g, 6, 7)
print(way.give_address())
