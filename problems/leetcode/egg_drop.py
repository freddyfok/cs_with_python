"""
given some num of eggs and some num of floors
find the minimum number of drops required to find the critical floor
critical floor is where the egg breaks if you move up one more floor
"""


def egg_dropping(num_eggs, num_floors):
    memo = dict()  # memo[(egg, floor)] = tries

    if num_floors == 0 or num_eggs == 0:
        return -1

    # with 1 egg
    for floor in range(1, num_floors+1):
        memo[(1, floor)] = floor

    # with 1 floor
    for egg in range(1, num_eggs+1):
        memo[(egg, 1)] = 1

    for egg in range(2, num_eggs+1):
        for floor in range(2, num_floors+1):
            num_tries = []
            for trial_floor in range(1, floor+1):
                broken = memo[(egg-1, trial_floor-1)] if trial_floor != 1 else 0
                unbroken = memo[(egg, floor-trial_floor)] if trial_floor != floor else 0
                num_tries.append(1 + max(broken, unbroken))
            memo[(egg, floor)] = min(num_tries)

    return memo[(num_eggs, num_floors)]


if __name__ == "__main__":
    print(egg_dropping(2, 36))
