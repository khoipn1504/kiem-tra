import pyodbc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

serverInfo = "DESKTOP-7PLBSPR\MSSQLSERVER01"
databaseName = "CRM"
userId = 'khoipn'
userPass = '123456789'

driver = '{SQL Server}'
# port = '1433'

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                            serverInfo+';DATABASE='+databaseName+';UID='+userId+';PWD='+userPass)

cursor = connection.cursor()


def AddHocVien(*info):
    sql = "INSERT INTO HOC_VIEN VALUES(?,?,?,?,?,?,?)"
    val = info
    cursor.execute(sql, val)
    connection.commit()
    print("record inserted.")


def send_mail(content):
    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('user', 'pass')

        msg = MIMEMultipart()       # create a message

        msg['From'] = 'hoiquanbienhoa.channel@gmail.com'
        msg['To'] = 'tbtoanit@gmail.com'
        msg['Subject'] = "Thông báo"

        msg.attach(MIMEText(content, 'plain'))

        s.send_message(msg)
        s.quit()
        print('Đã gui được')
    except:
        print('Chưa gui được email')


try:
    hocvien = []
    content = ''
    with open("hoc_vien1.txt", 'r') as f:
        patten = ['HEADER', 'DATE', 'MA_HOCVIEN',
                  'TEN_HOCVIEN', 'LOP', 'EMAIL', 'SO_DIEN_THOAI']
        temp = f.readlines()
        content = ''.join(temp)
        for i in range(7):
            if patten[i] == 'DATE':
                date = temp[i][len(patten[i])+1:-1].replace('-', '')
                hocvien.append(date)
            else:
                hocvien.append(temp[i][len(patten[i])+1:-1])

    AddHocVien(*hocvien)
    # print(content)
    send_mail(content)
except:
    print("Khong co du lieu nhu mong muon")
