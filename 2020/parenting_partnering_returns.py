import numpy

num_cases = int(input())
case = 1


def is_conflict(a1, a2):
    # takes two tuples representing activities (start and end times)
    if a1[0] < a2[0]:
        if a1[1] <= a2[0]:
            return False
    elif a1[0] >= a2[1]:
        return False
    return True


while case <= int(num_cases):

    # reading input
    num_act = int(input())
    activities = []
    for act_num in range(num_act):
        act = [int(i) for i in input().split()]
        act.append(act_num)
        act.append(-1) #placeholder for name
        activities.append(act)

    # sort activities by start time
    activities = numpy.array(activities)
    activities = activities[activities[:, 0].argsort()]

    J_up = True
    impossible = False
    last_J_event = [0, 0]
    last_C_event = [0, 0]

    #print(activities)

    for i in range(len(activities)):
        current_act = activities[i]
        if i == 0:
            activities[i][3] = 1
            last_J_event = current_act
        else:
            if is_conflict(activities[i], activities[i-1]):
                J_up = not J_up
                if (J_up and is_conflict(activities[i], last_J_event)) or ((not J_up) and is_conflict(activities[i], last_C_event)):
                    impossible = True
            if J_up:
                activities[i][3] = 1
                last_J_event = activities[i]
            else:
                activities[i][3] = 0
                last_C_event = activities[i]

    activities = activities[activities[:, 2].argsort()]

    schedule = ''

    for a in activities:
        if a[3] == 0:
            schedule = schedule + 'C'
        elif a[3] == 1:
            schedule = schedule + 'J'

    if impossible:
        schedule = 'IMPOSSIBLE'

    print(f"Case #{case}: {schedule}")
    case += 1
