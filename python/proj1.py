import time
import imaplib
import email
import datetime
from xlwt import Workbook,easyxf

#Connection and Authentication part

mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
username='Girishkumar399@gmail.com'
password='Girirebel'
#username=raw_input('please enter the username:')
#password=raw_input('please input your password:')
mail.login(username,password)
mail.select("INBOX")

#Excel part pattern: back_color gray25 italic 1

wb=Workbook()
sheet=wb.add_sheet("Email Data")
style=easyxf('font: name Calibri, bold on, height 280;border: top thick, right thick, bottom thick, left thick;font: underline on;pattern: pattern fine_dots, fore_color white, back_color orange;font: color black; align: horiz center')
style2=easyxf('font: name Times New Roman,bold off, height 215;borders: top double, bottom double, left double, right double;pattern:fore_colour white, back_color brown ;font: color black;align: horiz center')
sheet.write(0,0,"SL.NO",style)
sheet.write(0,1,"FROM",style)
sheet.write(0,2,"TO",style)
sheet.write(0,3,"CC",style)
sheet.write(0,4,"SUBJECT",style)
sheet.write(0,5,"DATE",style)
sheet.write(0,6,"CONTENT",style)
style1=easyxf('font: name Times New Roman,bold off, height 215;borders: top double, bottom double, left double, right double;pattern:fore_colour white, back_color brown ;font: color black')


#Mailbox selection and Body part pattern solid,fore_colour green


def loop():
    n=0
    mail.select("INBOX",readonly=True)
    (retcode,messages)=mail.search(None,'(ALL)')
    print retcode,messages
    if retcode=='OK':
        for num in messages[0].split():
            n=n+1
            print n
            typ,data=mail.fetch(num,'(RFC822)')
            for response_part in data:
                if isinstance (response_part,tuple):
                    original=email.message_from_string(response_part[1])
                    data=original['From']
                    data1=original['Subject']
                    data2=original['To']
                    data3=original['CC']
                    date=original['Date']
                    print "From:",data
                    print "To:",data2
                    print "CC:",data3
                    print "Date:",date
                    print "Subject:",data1
                    sheet.col(0).width=2000
                    sheet.col(1).width=11000
                    sheet.col(2).width=9000
                    sheet.col(3).width=9000
                    sheet.col(4).width=12000
                    sheet.col(5).width=10000
                    sheet.col(6).width=65535
                    sheet.write(n,0,n,style2)
                    sheet.write(n,1,data,style1)
                    sheet.write(n,2,data2,style1)
                    sheet.write(n,3,data3,style1)
                    sheet.write(n,4,data1,style1)
                    sheet.write(n,5,date,style1)
                    
                    
            for part in original.walk():
                if part.get_content_type()=='multipart/related' or part.get_content_type()=='text/plain':
                    print part.get_payload(decode=True)
                    sheet.write(n,6,part.get_payload(),style1)
            wb.save('Emailreport.xls')
            typ,data=mail.store(num,'+FLAGS','\\Seen')
        print n     



# Main function part
if __name__=='__main__':
    try:
        loop()
    finally:
        print 'Thanks'
