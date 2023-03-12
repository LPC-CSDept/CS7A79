import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    # datastr = 'are arrow amore aspire aero'
    # sys.stdin = io.StringIO(datastr)

    rsum, csum, rowidx, maxnum = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    print(rsum)
    assert len(rsum) == 3
    assert rsum[0] == 317
    assert rsum[1] == 242
    assert rsum[2] == 209
    assert len(csum) == 5
    assert csum[0] == 176
    assert csum[1] == 109
    assert csum[2] == 163
    assert csum[3] == 207
    assert csum[4] == 113
    assert rowidx == 0
    assert maxnum == 99
