def minimumBribes(q):
    count = 0
    count_array = [0 for _ in range(len(q))]
    for j in range(len(q)):
        for i in range(len(q)-j-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                count += 1
                count_array[q[i]-1] -= 1
                count_array[q[i+1]-1] += 1
                if count_array[q[i]-1] > 2 or count_array[q[i+1]-1] > 2:
                    print("Too chaotic")
                    return
    print(count)


if __name__ == "__main__":
    arr = [2,1,5,3,4]
    minimumBribes(arr)
