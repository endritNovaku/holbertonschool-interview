#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """return pascal triangle"""
    pascalArr = []
    if n <= 0:
        return([[]])

    for i in range(0, n):
        if i == 0:
            pascalArr.append([1])
        elif i == 1:
            pascalArr.append([1, 1])
        elif i == 2:
            pascalArr.append([1, 2, 1])
        else:
            pascalArr.append([])
            for j in range(0, len(pascalArr[i-1])):
                if j == 0:
                    pascalArr[i].append(1)
                    pascalArr[i]\
                        .append(pascalArr[i-1][j] + pascalArr[i-1][j+1])
                elif j != len(pascalArr[i-1])-1:
                    pascalArr[i]\
                        .append(pascalArr[i-1][j] + pascalArr[i-1][j+1])
                else:
                    pascalArr[i].append(1)
    return(pascalArr)
