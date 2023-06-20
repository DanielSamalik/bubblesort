def bubble_sort(zoznam):
    print(zoznam)
    n = len(zoznam)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if zoznam[j] > zoznam[j + 1]:
                zoznam[j], zoznam[j + 1] = zoznam[j + 1], zoznam[j]
    return zoznam

print(bubble_sort([23, 10, 18, 50, 3, 90, 32, 48]))