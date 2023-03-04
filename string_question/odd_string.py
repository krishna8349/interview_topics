from msilib.schema import ODBCDataSource


def odd_string(str):
    oddstr = ''
    for i in range(len(str)):
        if i % 2 == 0:
            oddstr = oddstr+str[i]
    print(oddstr)

str = "letsplayef"
odd_string(str)