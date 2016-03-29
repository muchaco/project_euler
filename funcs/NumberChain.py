class NumberChain:
    def __init__(self, _next, finals):
        """
        :param _next: lambda function of next element in chain
        :param finals: predefined final elements in chain
        :return:
        """
        self.next = _next
        self.end_points = {i: i for i in finals}
        self.lengths = {i: 1 for i in finals}

    def length(self, i):
        if i not in self.lengths:
            self.lengths[i] = self.length(self.next(i))+1
        return self.lengths[i]

    def end_point(self, i):
        if i not in self.end_points:
            self.end_points[i] = self.end_point(self.next(i))
        return self.end_points[i]