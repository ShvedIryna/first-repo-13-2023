# Робота з функціями

def test_func1():
    pass


def info(word):
    print(word, end="")
    print("!")


def summa(a, b):
    res = a + b
    info(res)
    return res


res1 = summa(5, 6)
res2 = summa(5.6, 4.4)
res3 = summa("hi", "word")
print(res1)


# Мінімальний

def minimal(l):
    min_num = l[0]
    for i in l:
        if i < min_num:
            min_num = i

    return min_num


nums1 = [5, 3, 7, 3, 6, -10, 0, 5]
res1_ = minimal(nums1)

nums2 = [5, 3, 7, 3, 6, -6, 0, 5]
res2_ = minimal(nums2)

if res1_ < res2_:
    print(res1_)
else:
    print(res2_)


# lambda функції(анонімні)

func = lambda x, y: x * y
print(func(5, 6))