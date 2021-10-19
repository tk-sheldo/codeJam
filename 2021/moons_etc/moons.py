

def remove_double_empties(mural):
    i = 0
    while i < len(mural):
        if mural[i] == '?':
            while i + 1 < len(mural) and mural[i+1] == '?':
                #print('e', mural)
                mural.pop(i+1)
        i += 1
        #print('g', mural)



    return mural


def finish_mural(mural):

    if mural == ['?']:
        return 'J'
    else:
        for i in range(len(mural)):
            if mural[i] == '?':
                if i == 0:
                    mural[i] = mural[i+1]
                elif i == len(mural) - 1:
                    mural[i] = mural[i-1]
                else:
                    pre = mural[i-1]
                    post = mural[i+1]
                    if pre == post:
                        mural[i] = pre
                    elif pre == 'J':
                        mural[i] = 'J'
                    elif pre == 'C':
                        mural[i] = 'C'

            #print(mural)

        return mural


def cost_calc(xc, yc, finished_mural):

    cost = 0

    for i in range(len(finished_mural)):
        if i == 0:
            pass
        else:
            if finished_mural[i] != finished_mural[i-1]:
                if finished_mural[i] == 'J':
                    cost += xc
                else:
                    cost += yc

    return cost


#2 3 CJ?CC?

t = int(input())

for i in range(t):

    x_cost, y_cost, mural_string = input().split()

    mural_arr = list(mural_string)

    #print(mural_arr)
    mural_arr = remove_double_empties(mural_arr)
    #print(mural_arr)

    x_cost = int(x_cost)
    y_cost = int(y_cost)
    fm = finish_mural(mural_arr)

    cost = cost_calc(x_cost, y_cost, fm)

    print(f"Case #{i + 1}: {cost}")

    


        