import datetime
import os
import unittest

import paramunittest as paramunittest

from HTMLTestRunner import HTMLTestRunner
from excel_utils import read_excel, update_excel
from http_utils import send_post_json, send_post, send_get
from mysql_utils import query

xlsx_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
df = read_excel(xlsx_path + '/resource/case-template.xlsx', '工作表1')


@paramunittest.parametrized(*df)
class test(unittest.TestCase):
    def setParameters(self, a, b, c, d, e, f, g, h, i, j):
        self.test_id = int(a)
        self.test_title = b
        self.http_url = c
        self.http_type = str(d)
        self.http_param_type = str(e)
        self.http_param = f
        self.result_key = g
        self.result_mysql = j

    def setUp(self):
        # 初始化测试执行时间
        self.test_time = datetime.datetime.now()
        # 初始化测试结果
        self.test_result = "FAIL"

    def test_pitest(self):
        if "POST" == self.http_type and "Json" == self.http_param_type:
            res = send_post_json(self.http_url, self.http_param)
        elif "POST" == self.http_type and "Key:Value" == self.http_param_type:
            res = send_post(self.http_url + "?" + self.http_param)
        elif "GET" == self.http_type and "Key:Value" == self.http_param_type:
            res = send_get(self.http_url + "?" + self.http_param)
        else:
            raise RuntimeError('暂不支持！！！')
        # 关键字校验
        result_key_array = str(self.result_key).replace("\n", "").split(";")
        for key in result_key_array:
            if res.find(key) < 0:
                raise RuntimeError("测试用例【" + self.test_title + "】执行失败，关键字" + key + "匹配失败")
        # 数据库校验
        result_mysql_array = str(self.result_mysql).replace("\n", "").split(";")
        for sql in result_mysql_array:
            if '' == sql:
                break
            num = query(sql)
            if num < 0:
                raise RuntimeError("测试用例【" + self.test_title + "】执行失败，数据库查询无匹配值")
            if num > 1:
                raise RuntimeError("测试用例【" + self.test_title + "】执行失败，数据库查询目标值匹配不唯一，共计" + num + "条")

        self.test_result = 'PASS'
        print("测试用例【" + self.test_title + "】执行通过")

    def tearDown(self):
        # 回填测试结果
        update_excel(xlsx_path + '/resource/case-template.xlsx', '工作表1', self.test_id - 1, "执行结果", self.test_result)
        update_excel(xlsx_path + '/resource/case-template.xlsx', '工作表1', self.test_id - 1, "测试时间", self.test_time)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(xlsx_path, pattern='test.py', top_level_dir=None)

    suite.addTest(discover)

    html_file = xlsx_path + "/report/report.html"
    fp = open(html_file, "wb")
    HTMLTestRunner(stream=fp).run(suite)
