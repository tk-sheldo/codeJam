
import copy as cp

class PascalTriangle:

    def __str__(self):

        string = ''

        for row in self.val_tri:
            for cell in row:
                string = string + str(cell[0]) + "  "
            string = string + "\n"

        return string

    def __init__(self, height):

        """
        :param height:

        val_tri holds original pascal values
        sum_tri holds list of potential sums
        visited is boolean
        """

        self.height = height

        self.val_tri = [[1]]

        r = 1

        while r < height:

            new_row = [None] * (r + 1)

            new_row[0], new_row[-1] = 1, 1

            k = 1

            while k < r:

                new_val = self.val_tri[r - 1][k - 1] + self.val_tri[r - 1][k]

                new_row[k] = new_val

                k += 1

            self.val_tri.append(new_row)

            r += 1

        self.sum_tri = []

        for row in self.val_tri:

            ro = []

            for val in row:

                sum_cell = [(val, ())]

                ro.append(sum_cell)

            self.sum_tri.append(ro)


        """
        self.sum_tri = []

        for row in self.val_tri:

            r = []
            for cell_val in row:
                r.append({cell_val: []})

            self.sum_tri.append(r)

        self.visited = []

        for row in self.val_tri:

            r = []
            for cell_val in row:
                r.append(False)

            self.visited.append(r)
            
        """

    def get_cell_val(self, r, k):

        return self.val_tri[r - 1][k - 1]

    def get_cell_sums(self, r, k):

        return self.sum_tri[r - 1][k - 1]

    def has_visited(self, r, k):

        return self.visited[r - 1][k - 1]

    def add_sum(self, r, k, val, path):

        self.sum_tri[r - 1][k - 1].append((val, path))

    def visit(self, r, k):

        self.visited[r - 1][k - 1] = True

    def get_neighbors(self, r, k):

        neighbors = []

        if k != 1:
            neighbors.append((r - 1, k - 1))
            neighbors.append((r, k - 1))

        if k != r:
            neighbors.append((r - 1, k))
            neighbors.append((r, k + 1))

        if r != self.height:
            neighbors.append((r + 1, k))
            neighbors.append((r + 1, k + 1))

        return neighbors

    def get_unvisited_neighbors(self, r, k):

        neighbors = self.get_neighbors(r, k)

        for i in range(len(neighbors)):
            n_r, n_k = neighbors[i]
            if self.has_visited(n_r, n_k):
                neighbors.pop(i)

        return neighbors

    def pascal_walk(self, val):

        return self.sum_find(val, 1, 1, [])

    def sum_find(self, val, r, k, visited):

        this_val = self.get_cell_val(r, k)
        this_pot = self.get_cell_pot(r, k)

        if val in this_pot:

            for cell in this_pot[val]:
                if cell in visited:
                    pass

            return this_pot[val]

        elif (val - this_val) < 0:

            return -1

        else:

            neighbors = self.get_unvisited_neighbors(r, k)

            while len(neighbors) > 0:

                n_r, n_k = neighbors.pop()

                res = self.sum_find(val - this_val, n_r, n_k)

                if res != -1:

                    self.add_sum(r, k)
                    return res

            return -1









p = PascalTriangle(3)







