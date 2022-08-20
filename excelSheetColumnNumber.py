#171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        colNumber = 0
        colTitles = list(columnTitle[::-1])
        for i in range(len(colTitles)):
            colNumber += (ord(colTitles[i])-64)*(26**i)
        return colNumber
