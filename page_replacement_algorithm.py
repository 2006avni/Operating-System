frames = [-1] * 10
pages = [0] * 50

# FIFO Page Replacement
def fifo():
    global frames
    index = 0
    faults = 0

    for i in range(f):
        frames[i] = -1

    for i in range(n):
        flag = 0

        for j in range(f):
            if frames[j] == pages[i]:
                flag = 1
                break

        if flag == 0:
            frames[index] = pages[i]
            index = (index + 1) % f
            faults += 1

    print("FIFO Page Faults =", faults)


# LRU Page Replacement
def lru():
    global frames
    time = [0] * 10
    counter = 0
    faults = 0

    for i in range(f):
        frames[i] = -1
        time[i] = 0

    for i in range(n):
        flag = 0

        for j in range(f):
            if frames[j] == pages[i]:
                counter += 1
                time[j] = counter
                flag = 1
                break

        if flag == 0:
            min_val = time[0]
            pos = 0

            for j in range(f):
                if frames[j] == -1:
                    pos = j
                    break

                if time[j] < min_val:
                    min_val = time[j]
                    pos = j

            frames[pos] = pages[i]
            counter += 1
            time[pos] = counter
            faults += 1

    print("LRU Page Faults =", faults)


# Optimal Page Replacement
def optimal():
    global frames
    faults = 0

    for i in range(f):
        frames[i] = -1

    for i in range(n):
        flag = 0

        for j in range(f):
            if frames[j] == pages[i]:
                flag = 1
                break

        if flag == 0:
            found = 0

            for j in range(f):
                if frames[j] == -1:
                    frames[j] = pages[i]
                    faults += 1
                    found = 1
                    break

            if found:
                continue

            farthest = -1
            pos = -1

            for j in range(f):
                next_use = -1

                for k in range(i + 1, n):
                    if frames[j] == pages[k]:
                        next_use = k
                        break

                if next_use == -1:
                    pos = j
                    break

                if next_use > farthest:
                    farthest = next_use
                    pos = j

            frames[pos] = pages[i]
            faults += 1

    print("Optimal Page Faults =", faults)


# Main Function
n = int(input("Enter number of pages: "))

print("Enter page reference string:")
pages = list(map(int, input().split()))

f = int(input("Enter number of frames: "))

print("\n--- Page Replacement Results ---")

fifo()
lru()
optimal()
