def sort(list):
    for i in range(1, len(list)):
        high = i
        low = 0
        while high >= low:
            mid = int((high + low) / 2)
            if list[mid] < list[i]:
                low = mid + 1
            if list[mid] > list[i]:
                high = mid - 1
            if list[mid] == list[i]:
                low = mid
                break
        insert(list, i, low)
    return list


# src > dest
def insert(list, src, dest):
    temp = list[src]
    for i in range(src - 1, dest - 1, -1):
        list[i + 1] = list[i]
    list[dest] = temp


if __name__ == '__main__':
    a = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1]
    ret = sort(a)
    print(ret)
