#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.header import Header
'''
sender = 'chen_jiawei666@163.com'
receivers = ['1004317804@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
message['To'] = Header("测试", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "chenjiawei@gagogroup.com"  # 用户名
mail_pass = "96UM7iykd4SfaVFt"  # 口令

sender = 'chenjiawei@gagogroup.com'
receivers = ['chenjiawei@gagogroup.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('自动化测试报告', 'plain', 'utf-8')
message['From'] = Header("陈家伟1", 'utf-8')
message['To'] = Header("陈家伟2", 'utf-8')

subject = '自动化测试报告'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
sender = 'chenjiawei@gagogroup.com'  # 发件人邮箱账号
my_pass = '96UM7iykd4SfaVFt'  # 发件人邮箱密码
my_user = 'chenjiawei@gagogroup.com'  # 收件人邮箱账号，我这边发送给自己
SMTP_SSL =''
result = '自动化测试报告：\n' \
         '成功：7；' \
         '失败：2；' \
         '跳过：1'

class Send_email:

    def __init__(self,sender,password,addressee,smtp_ssl,port):
        self.sender = sender  # 发件人邮箱账号
        self.password = password  # 发件人邮箱密码
        self.addressee = addressee  # 收件人邮箱账号，我这边发送给自己
        self.smtp_ssl = smtp_ssl
        self.port = port
        result = '自动化测试报告：\n' \
                 '成功：7；' \
                 '失败：2；' \
                 '跳过：1'

    def mail(self):
        ret = True
        try:
            msg = MIMEMultipart()
            msg.attach(MIMEText(result, 'plain', 'utf-8'))
            # msg = MIMEText('自动化测试报告', 'plain', 'utf-8')
            msg['From'] = formataddr([self.sender, self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr([self.addressee, self.addressee])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "陈家伟发送邮件测试"  # 邮件的主题，也可以说是标题

            att1 = MIMEText(open('/Users/chenjiawei/Desktop/IMG_3627.jpg', 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="dog.jpg"'
            msg.attach(att1)

            server = smtplib.SMTP_SSL(self.smtp_ssl, self.port)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender, [self.addressee, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            print("邮件发送成功")
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
            print("邮件发送失败")
        return ret


if __name__ == '__main__':
    test = Send_email(sender='chenjiawei@gagogroup.com',password='96UM7iykd4SfaVFt',addressee='chenjiawei@gagogroup.com',smtp_ssl='smtp.exmail.qq.com',port=465)
    test.mail()