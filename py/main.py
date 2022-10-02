# import math
#
# fun = lambda x: 1 if x == 1 else math.ceil(math.sinh(fun(x - 1)))
# print(fun(5))
import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            # self.id, self.title, self.pages = fields
            # self.lst_values = lst_values
            res = zip(fields, lst_values)
            r = list(res)
            return r


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__)

# def f(l1, l2):
#     return filter(zip,(l1, l2))
#
# l1 = [1, 2, 3]
# l2 = ['one', 'two', 'three']
#
# # res = (filter(zip, l1))
# print(*f(l1,l2))