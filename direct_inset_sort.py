def sort(list):
    for i in range(len(list)):
        for j in range(i-1, -1, -1):
            if list[j+1] < list[j]:
                swap(list, j+1, j)
    return list


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


if __name__ == '__main__':
    a = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1]
    ret = sort(a)
    print(ret)
