class Graph:
    def __init__(self, name=""):
        self.name = name
        self.list_neighbor = {}
        self.list_node = {}

    def add_node(self, node):
        self.list_node[node] = True

    def add_edge(self, node, nodebis):
        try:
            self.list_neighbor[node].add(nodebis)
        except KeyError:
            self.list_neighbor[node] = set()
            self.list_neighbor[node].add(nodebis)

    def neighbors(self, node):
        try:
            return self.list_neighbor[node]
        except KeyError:
            return set()

    def nodes(self):
        return self.list_node.keys()

    def delete_edge(self, node, nodebis):
        self.list_neighbor[node].discard(nodebis)

    def delete_node(self, node):
        del self.list_node[node]
        try:
            for nodebis in self.nodes():
                self.list_neighbor[nodebis].discard(node)
            del self.list_neighbor[node]
        except KeyError:
            return "error"
