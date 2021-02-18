
import copy as cp


class LatinSquare:

    def __str__(self):

        string = ''
        for row in self.square:
            for elem in row:
                string = string + f"{elem:>3d}" + " "
            string = string[0:-1] + "\n"

        return string[0:-1]

    def __init__(self, n):

        self.n = n
        self.square = [[0 for _ in range(n)] for _ in range(n)]
        self.possibilities = [[[(i + 1) for i in range(n)] for _ in range(n)] for _ in range(n)]

    def insert_trace(self, arr):

        for i in range(self.n):
            self.set_cell(i, i, arr[i])

    def set_cell(self, row, col, num):

        # print(self.possibilities)
        # print(f"set_cell({row}, {col}, {num})")

        self.square[row][col] = num
        self.possibilities[row][col] = [0]
        self.update_poss(row, col)
        # self.no_more_options_check(row, col)

    def no_more_options_check(self, row, col):
        """ checks a row or column to see if there is only one option for a number """

        # check rows
        poss_count = dict()

        # creates dictionary to keep track of how many occurrences there are of each possibility
        for i in range(self.n):
            poss_count.clear()
            print(f"checking row {i}")
            for poss in self.possibilities[row][i]:
                if poss != 0:
                    if poss not in poss_count:
                        poss_count[poss] = [1, i]   # count, col (for remembering where the single is)
                    else:
                        poss_count[poss][0] += 1

        # checks dictionary for lonely possibilities
        print(f"poss_count: {poss_count}")
        for poss in poss_count:
            if poss_count[poss][0] == 1:   # if there's only one entry, it's a new num!
                print(f"NMO find at [{row}][{poss_count[poss][1]}]: \n >>>>>> {self.possibilities}")
                self.set_cell(row, poss_count[poss][1], poss)

        # check cols

        for i in range(self.n):
            poss_count.clear()
            print(f"checking col {i}")
            for poss in self.possibilities[i][col]:
                if poss != 0:
                    if poss not in poss_count:
                        poss_count[poss] = [1, i]
                    else:
                        poss_count[poss][0] += 1

        print(f"poss_count: {poss_count}")
        for poss in poss_count:
            if poss_count[poss][0] == 1:
                print(f"NMO find at [{poss_count[poss][1]}][{col}]: \n >>>>>> {self.possibilities}")
                self.set_cell(poss_count[poss][1], col, poss)

    def update_poss(self, row, col):
        """ updates the possibility values for a row and column of a new cell value """

        new_cell_val = self.square[row][col]

        # updates col
        for i in range(self.n):

            # culls new_cell_val from possibilities lists
            if new_cell_val in self.possibilities[i][col]:
                self.possibilities[i][col].remove(new_cell_val)

            # checks that cell for certainty
            if len(self.possibilities[i][col]) == 1 and self.possibilities[i][col][0] != 0:
                self.set_cell(i, col, self.possibilities[i][col][0])

        # updates row
        for i in range(self.n):

            if new_cell_val in self.possibilities[row][i]:
                self.possibilities[row][i].remove(new_cell_val)

            if len(self.possibilities[row][i]) == 1 and self.possibilities[row][i][0] != 0:
                self.set_cell(row, i, self.possibilities[row][i][0])

    def is_full(self):
        """ returns true if the square is full of numbers (not necessarily correct), false otherwise """

        # some overlap among these three methods..

        for row in self.square:
            for e in row:
                if e == 0:
                    return False
        return True

    def is_finished(self):
        """ returns True if the 'latin' square is complete, False otherwise """

        for row in range(self.n):
            checklist = [(i + 1) for i in range(self.n)]
            for c in range(self.n):
                elem = self.square[row][c]
                if elem not in checklist:
                    return False
                else:
                    checklist.remove(elem)
            if len(checklist) > 0:
                return False

        for col in range(self.n):
            checklist = [(i + 1) for i in range(self.n)]
            for r in range(self.n):
                elem = self.square[r][col]
                if elem not in checklist:
                    return False
                checklist.remove(elem)
            if len(checklist) > 0:
                return False

        return True

    def is_valid(self):
        """ returns True if the array is valid (not necessarily complete), False otherwise"""

        for row in range(self.n):
            seen = []
            for c in range(self.n):
                elem = self.square[row][c]
                if elem in seen and elem != 0:
                    return False
                seen.append(elem)

        for col in range(self.n):
            seen = []
            for r in range(self.n):
                elem = self.square[r][col]
                if elem in seen and elem != 0:
                    return False
                seen.append(elem)

        return True

    def find_guess_cell(self):
        """ finds the cell with the fewest possibilities, returns row, col coordinates """

        min_options = self.n
        guess_cell = None

        for r in range(self.n):
            for c in range(self.n):
                if len(self.possibilities[r][c]) < min_options and self.possibilities[r][c][0] != 0:
                    guess_cell = (r, c)
                    min_options = len(self.possibilities[r][c])

        assert (guess_cell is not None), "There are no cells left to guess."
        return guess_cell

    def guess_to_solve(self):

        # print(self.square)
        # print(self.possibilities)

        if self.is_full():

            return self

        else:

            base_exp_array = cp.deepcopy(self)

            r, c = base_exp_array.find_guess_cell()
            poss = base_exp_array.possibilities[r][c]

            for p in poss:
                # print(f">>>>>>>>>>>>>>>> guessing {p} at spot [{r}][{c}]")
                exp_array = cp.deepcopy(base_exp_array)
                exp_array.set_cell(r, c, p)
                sol = exp_array.guess_to_solve()
                if sol != -1 and sol.is_valid():
                    return sol
                # else:
                    # print(f"{p} at spot [{r}][{c}] was a bad guess")

            return -1

    def solve(self):
        sol = self.guess_to_solve()
        if sol == -1:
            return -1    # no solution for this arrangement
        else:
            # print(sol.square)
            # print(sol.is_finished())
            return sol


def has_black_sheep(a):
    """
    Looks at an array to determine if all but one element is the same

    If this is the case, the function returns the index of the unique element.
    Otherwise, it returns -1
    """

    #  [1, 1] -> -1
    #  [4, 4, 3, 4, 4, 4] -> 2

    nums = dict()

    for i in range(len(a)):

        if a[i] not in nums:
            nums[a[i]] = 1
        else:
            nums[a[i]] += 1

        if len(nums) > 2:
            return -1

    # now we know that len(nums) = 1 or 2

    for k in list(nums.keys()):
        if nums[k] == 1:
            return a.index(k)

    return -1


def find_trace(s, nu):
    """ finds the trace for a k*k matrix that adds to sum, returns -1 if malformed """

    assert s >= nu, "can't be done"
    assert s <= nu ** 2, "can't be done"

    def fc_recurse(su, n):
        """ returns an array of n ints between [1, n] that add to 'su'  """

        # print(f"find_components({su}, {n})")

        if su == n:
            return [1] * n
        else:
            arr = fc_recurse(su - 1, n)   # recursive call

            # find where to add one in
            for i in range(len(arr)):

                if arr[i] < n:

                    arr[i] += 1

                    if has_black_sheep(arr) == -1:

                        return arr

                    else:
                        for j in range(len(arr)):
                            arr = arr
                            if j != i and arr[j] < n and arr[j] != arr[i] - 1:
                                arr[j] += 1
                                arr[i] -= 1

                                return arr

                    # print(f"find_components({su}, {n}) -> {arr}")
                    return arr

    sol = fc_recurse(s, nu)

    #
    if has_black_sheep(sol) == -1:
        return sol
    else:
        return -1   # impossible


t = int(input())

for i in range(t):

    print(f"Case #{i + 1}: ", end = '')
    n, k = [int(i) for i in input().split()]

    tr = find_trace(k, n)
    if tr == -1:
        print("IMPOSSIBLE")
    else:
        sq = LatinSquare(n)
        sq.insert_trace(tr)
        sol = sq.solve()
        if sol == -1:
            print("IMPOSSIBLE")
        else:
            print("POSSIBLE")
            print(sol)


