def evenOdd(input1: list[int], input2: int) -> str:
    result = ""
    for i in range(input2):
        if input1[i] % 2 == 0:
            result += "Even "
        else:
            result += "Odd "
    return result


print(evenOdd([1, 2, 3], 3))
