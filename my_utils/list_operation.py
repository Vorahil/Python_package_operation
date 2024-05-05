def list_double_number(list1):  # 对列表取偶
    list2 = []
    for i in list1:
        if i % 2 == 0:
            list2.append(i)
    print(list2)


if __name__ == '__main__':
    list_double_number([1, 2, 3, 4])


