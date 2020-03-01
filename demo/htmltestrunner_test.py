import os
import unittest

from HTMLTestRunner import HTMLTestRunner


class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("this is class method\n")

    def setUp(self):
        print("this is setup")

    def test01(self):
        # flag = False
        print("this is test01")
        self.assertEqual('1', '2', '数据错误')
        # self.assertNotEqual(1, 2)
        # self.assertTrue(flag)

    # @unittest.skip("CaseTest")  # 用这个方法跳过下面的测试案例

    def test02(self):
        print("this is test02")

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is tearDownClass")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test02"))
    suite.addTest(CaseTest("test01"))
    # unittest.TextTestRunner().run(suite)
    xlsx_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    html_file = xlsx_path+"/report/report.html"
    fp = open(html_file, "wb")

    runner = HTMLTestRunner(stream =  fp,
                        title = "xxx接口测试报告",
                        description = "测试用例执行情况：").run(suite)
    fp.close()  # 关闭报告文件
