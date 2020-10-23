from RandomNumbers import RandomNumbers


def slectSort(a: list):                    # 选择排序
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def slectSort1(a:list):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    return a


def bubbleSort(a: list):                    # 冒泡排序
    print(f"原始数据: {a}")
    for i in range(len(a) - 1):
        flag = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if not flag:
            break
        print(f"第{i+1}轮排序结果为: {a}")
    return a


if __name__ == '__main__':
    a = RandomNumbers.RandomNumbers(20)
    b = bubbleSort(a)
    print(b)

