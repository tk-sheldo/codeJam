
class Pattern:

    def __init__(self, rule):

        self.rule = rule

    """
    def add(self, new_pattern):

        # if new_pattern is empty
        if len(new_pattern.rule) == 0:
            return self

        else:
            first_chunk_new = new_pattern.rule.split('*')
            first_chunk_old = self.rule.split('*')

            if new_pattern[0] != '*' and self:
                pass

        elif len(self.rule) == 1 and not self.any_start and not self.any_end:
            return -1


        for chunk in self.rule:
            if new_pattern.rule[0] in chunk:
    """


def first_chunk(rule_string):
    return rule_string.split('*')[0]


def find_spots(chunk, rule):
    """" ... """

    # rule: *DEK*ALAM*DELE*LEMONADE*DREDGE*ADE*EDGE
    # chunk ADE
    #
    # return [(0, -1), (2,-1), (3, 5), (5, 0), (6, -2)]
    #          ^ chunk     ^ location in chunk (neg. indicates prior to start)

    split_rule = rule.split('*')

    for c in range(len(split_rule)):

        rule_chunk = '$' * (len(chunk) - 1) + split_rule[c] + '$' * (len(chunk) - 1)

        print(rule_chunk)

def integrate_rules(r1, r2):
    """ integrates r1 into r2 """

    if r1 == '*':
        return r2
    if r2 == '*':
        return r1

    # must fit together nicely at start
    if r1[0] != '*' and r2[0] != '*':

        beg1 = first_chunk(r1)
        beg2 = first_chunk(r2)

        sht_chk = min(beg1, beg2, key=len)
        lng_chk = max(beg1, beg2, key=len)

        for i in range(len(sht_chk)):
            if sht_chk[i] != lng_chk[i]:
                return -1

        r2 = lng_chk + r2[(len(beg2)):]
        r1 = r1[len(beg1):]

    if r1[-1] != '*' and r2[-1] != '*':

        end1 = r1.split('*')[-1]
        end2 = r2.split('*')[-1]

        sht_chk = min(end1, end2, key=len)
        lng_chk = max(end1, end2, key=len)

        # check for real incompatibility
        for i in range(len(sht_chk)):
            if sht_chk[-i] != lng_chk[-i]:
                return -1

        # replace end piece with longest end
        r2 = r2[:-len(end2)] + lng_chk
        r1 = r1[:-len(end1)]

    print(f"r1: {r1}")
    print(f"r2: {r2}")


a = 'DELK*ILSS*AM'
b = 'DEL*ALAM'



