from random import randint

def RandomNumbers(n):
    lists = []
    for i in range(n):
        lists.append(randint(1,100))
    return lists


if __name__ == '__main__':
    a = RandomNumbers(10)
    print(a)