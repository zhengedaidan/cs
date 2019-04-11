import time
import unittest
from HtmlTestRunner import HTMLTestRunner
test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="*test*.py")
if __name__=="__main__":
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'w')as f:
        runner=HTMLTestRunner(output="ok",stream=f,report_title="Test Report",descriptions="test baidu")
        runner.run(discover)
