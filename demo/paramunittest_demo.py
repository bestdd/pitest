import time
import unittest

import paramunittest


# 先设置参数组
# @paramunittest.parametrized(
#     {'a': 1, 'b': 1, 'c': 2},
#     {'a': 1, 'b': 0, 'c': 1},
#     {'a': 1, 'b': 0, 'c': 0}
# )
@paramunittest.parametrized(
    ('1', '2','3'),
    ('4', '5','6'),
    {'a': 7, 'b': 8,'c':9},

)
class Testfun(unittest.TestCase):

    def setParameters(self, a, b, c):  # 感觉就是初始化__init__
        self.a = a
        self.b = b
        self.c = c

    def testcase(self):
        print('开始执行-----')
        time.sleep(1)
        print('a:%s' % self.a)
        print('b:%s' % self.b)
        print('c:%s' % self.c)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity就是打印好看一些