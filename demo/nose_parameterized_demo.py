import unittest

from nose_parameterized import parameterized


class TestAdd(unittest.TestCase):

    @parameterized.expand([
        ("01",1,2,3),
        ("02",2,2,4),
        ("03",4,4,4),
    ])
    def test(self, name, a, b, c):
        print(a)
        print(b)
        print(c)

if __name__ == '__main__':
    unittest.main(verbosity=2)