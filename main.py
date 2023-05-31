def getMaxElement(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def getSumRows(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def getSumCols(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def getMaxElmRow(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    ##################################################
    numbers = [[99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24, 56],
               [33, 77, 32, 33, 34]]
    ##################################################
    ret = getMaxElement(numbers)
    print('Return value from getMaxElement', ret)

    ret = getSumRows(numbers)
    print('Return value from getSumRows', ret)

    ret = getSumCols(numbers)
    print('Return value from getSumCols', ret)

    ret = getMaxElmRow(numbers)
    print('Return value from getMaxElmRow', ret)


if __name__ == '__main__':
    main()
