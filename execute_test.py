# -*- coding:utf-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner

from conf.global_var import PROJECT_PATH
from lib.common.send_email import SendMail
from scripts.baidu_search import BaiduSearch

if __name__ == "__main__":

    report_file = PROJECT_PATH + "/report/automation_test_report.html"
    report = open(report_file, "wb")

    total_suite = unittest.TestSuite()
    total_suite.addTest(BaiduSearch("testBaiduSearch"))

    '''trigger to run scripts'''
    runner = HTMLTestRunner(stream=report, title="Automation Test Report", description="Project description")
    result = runner.run(total_suite)
    report.close()

    # currently support sending email to TencentEnterprise mailbox, TencentQQ mailbox and NetEase 163 mailbox
    # TencentEnterprise mailbox: TE
    # TencentQQ mailbox: QQ
    # NetEase 163 mailbox: 163
    obj_email = SendMail(report_file, "TE")
    obj_email.send_email()



