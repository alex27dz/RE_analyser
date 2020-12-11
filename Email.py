# sending Email , using yagmail library
import yagmail

'''
#  ---------------------------- sending Email , using yagmail library -----------------------------
    #try
    #body = data_list  # body = 'hello world'
    #subject = 'test'
    #email = 'alex27dz@gmail.com'  # input front end

    #def send_email(email, subject, body):
        #ya_email = yagmail.SMTP('space.generation.world@gmail.com', 'NV27vnmc')
        #ya_email.send(email, subject, body)
        #print('Email sent')
        #return 'Email Sent'

    #send_email(email, subject, body)

#builders = Builders(metropolitan, xls_name)
#builders.lennar_filter()
#builders.copy_addr_to_list()
#builders.closeBrowser()Test Email account for sending emails with information
space.generation.world@gmail.com
Pass: NV27vnmc

Simple email send:
import yagmail
yag = yagmail.SMTP(‘YOUR_EMAIL@gmail.com’, ‘YOUR_PASSWORD’)
body = ‘large body that I have generated ‘
yag.send(‘to@someone.com’, ‘subject’, body)

Adding image in the body of the email, you need to use yagmail.inline:
import yagmail
yag = yagmail.SMTP(‘YOUR_EMAIL@gmail.com’, ‘YOUR_PASSWORD’)
contents = [“Some Text”, yagmail.inline( full_path_to_image )]
yag.send(send_to, subject, contents)
yag = yagmail.SMTP(‘YOUR_EMAIL@gmail.com’, ‘YOUR_PASSWORD’)
contents = [“Some Text”, yagmail.inline( full_path_to_image )]
yag.send(send_to, subject, contents)


# sending Email , using yagmail library
#body = 'hello world'
#subject = 'test'
#email = 'alex27dz@gmail.com'  # input front end
#ya_email.send(email, subject, body)

#ya_email = yagmail.SMTP('space.generation.world@gmail.com', 'NV27vnmc')  # using gmail test account to send all info
'''

# need email address and send Flag - to start running
def send_email(email, subject, body):
    ya_email = yagmail.SMTP('space.generation.world@gmail.com', 'NV27vnmc')
    ya_email.send(email, subject, body)

#send_email(email, subject, body)







