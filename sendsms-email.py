from smtplib import SMTP
import smtplib

server = smtplib.SMTP( 'smtp.gmail.com', 587 )
server.ehlo()
server.starttls()
server.login( '<username>', '<password>' )

server.ehlo()
print('Please choose whether you want to send your message by email or sms')
service = input('\n Type "sms" or "email" :  ')
if service == 'email':
    server.ehlo()
    
    email_id = input('\n Please enter your email id : ')
    server.sendmail( '<architgarg1515@gmail.com>', email_id, 'Hello!' )
    server.close()
if service == 'sms':
    
    print(' Please Choose a carrier service from the following and enter the number ')
    print('\nMetro PCS --> 1 \n T-Mobile --> 2 \n Verizon Wireless --> 3')
    print('AT&T --> 4 \n Sprint PCS --> 5 \n Nextel --> 6 \n Cricket -->7')
    print('US Cellular --> 8 \n Cingular (GSM) --> 9 \n Cingular (TDMA) --> 10')
    carrier = input(' Please Input your carrier service : ')
    mob_num = input('Please Enter your Mobile Number : ')
    server.ehlo()
    server.login( '<architgarg1515@gmail.com>', '<@Kaminibruno05>' )

    if carrier == '1':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@metropcs.sms.us', 'Hello!' )

    if carrier == '2':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@tmomail.net', 'Hello!' )

    if carrier == '3':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@vtext.com', 'Hello!' )

    if carrier == '4':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@txt.att.net', 'Hello!' )

    if carrier == '5':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@messaging.sprintpcs.com', 'Hello!' )

    if carrier == '6':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@messaging.nextel.com', 'Hello!' )

    if carrier == '7':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@sms.mycricket.com', 'Hello!' )

    if carrier == '8':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@mms.uscc.net', 'Hello!' )

    if carrier == '9':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'cingularme.com', 'Hello!' )

    if carrier == '10':
        server.sendmail( '<architgarg1515@gmail.com>', mob_num+'@mmode.com', 'Hello!' )
    server.close()
