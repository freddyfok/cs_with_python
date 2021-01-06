def counting_twos(n):
    count = 0

    for i in range(n+1):
        current = i
        while current != 0:
            # find remainder
            if current % 10 == 2:
                count += 1
            current //= 10

    return count


print(counting_twos(25))
