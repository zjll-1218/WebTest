# coding=utf-8
import smtplib
from datetime import datetime
from email.header import Header
from email.mime.text import MIMEText
from Common import CommonConfiguration as cc


def sendMail(send_from, send_to, text):
    """
    :param send_from:发件人
    :param send_to:收件人
    :param text:正文
    :return:
    """
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = Header('测试服务', 'utf-8')
    msg['To'] = Header('测试人员', 'utf-8')
    subject = "[Automation]TestReport_" + str(cc.getCurrentTime())
    msg['Subject'] = subject

    try:
        so = smtplib.SMTP()
        so.connect(host='smtp.exmail.qq.com')
        so.login(user='zhangjie@ytzhihui.com', password='4fxYp46CW6U4endj')
        assert isinstance(send_to, list)
        so.sendmail(send_from, send_to, msg.as_string())
        print('ok')
    except smtplib.SMTPException:
        print('error')


if __name__ == '__main__':
    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
    f = 'zhangjie@ytzhihui.com'
    t = ['zhangjie@ytzhihui.com']
    sendMail(f, t, mail_msg)
