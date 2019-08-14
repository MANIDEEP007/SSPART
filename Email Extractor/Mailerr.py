'''Module to Read Emails from Gmail or Outlook - Linux OS Based'''
import imaplib #Internet Message Access Protocol Library
import email
import os
import getpass #Get Password Library
import datetime


TODAY = datetime.datetime.now()
TODAY_STR = TODAY.strftime("%d%m%y%H%M%S")
IMAGE_EXT = ["jpg", "jpeg", "png"]
def read_mail(user, passkey, type_input="Outlook"):
    '''Function to Read Mails from a mailbox'''
    try:
        #Get Mail Server URL based on User Choice
        if type_input == "Outlook":
            mail_server = imaplib.IMAP4_SSL("smtp-mail.outlook.com")
        else:
            mail_server = imaplib.IMAP4_SSL('smtp.gmail.com',465)
        mail_server.login(user, passkey) #Login to SMTP Server
        print("Login Successful")
        mail_server.select("inbox") #Label Selection
        mail_type, mail_ids = mail_server.search(None, 'ALL') #Select All Mail ID in Inbox
        del mail_type
        id_list = str(mail_ids[0])[2:-1].split()
        first, last = int(id_list[0]), int(id_list[-1]) #Get first and Last Email ID
        #Make folders to store Mail Contents and Attachments with Dynamic name
        os.system("mkdir "+BASE_DIR+ "\\Mails_"+TODAY_STR)
        os.system("mkdir "+ BASE_DIR + "\\Mails_"+TODAY_STR+"\\Images_"+TODAY_STR)
        os.system("mkdir "+ BASE_DIR + "\\Mails_"+TODAY_STR+"\\Content_"+TODAY_STR)
        os.system("mkdir "+ BASE_DIR + "\\Mails_"+TODAY_STR+"\\PDF_"+TODAY_STR)
        os.system("mkdir "+ BASE_DIR + "\\Mails_"+TODAY_STR+"\\Text_Files_"+TODAY_STR)
        #End of Make folders to store Mail Contents and Attachments with Dynamic name
        for i in range(last, first-1, -1):
            file_mail = open(BASE_DIR+ "/Mails_"+TODAY_STR+"/Content_"+TODAY_STR+"/Mail_"\
                +str(i), "a")
            msg_type, msg_data = mail_server.fetch(str(i), '(RFC822)')
            del msg_type
            for response in msg_data:
                if isinstance(response, tuple):
                    msg_content = email.message_from_bytes(response[1])
                    print("From :"+ msg_content['from'], file=file_mail) #Get from Email Address
                    print("Subject: "+ msg_content['subject'], file=file_mail)#Get Subject of Mail
                    try:
                        message = {}
                        for part in email.message_from_bytes(response[1]).walk():
                            if part.get('Content-Disposition') is not None:
                                file_name = part.get_filename()
                                file_path = ""
                                if file_name.split(".")[-1].lower() in IMAGE_EXT:
                                    file_path = BASE_DIR + "\\Mails_"+TODAY_STR+"\\Images_"+TODAY_STR
                                elif file_name.split(".")[-1].lower() == "pdf":
                                    file_path = BASE_DIR + "\\Mails_"+TODAY_STR+"\\PDF_"+TODAY_STR
                                file_obj = open(file_path+"\\"+file_name, "wb")
                                file_obj.write(part.get_payload(decode=True))
                                file_obj.close()
                            #Get Content and Store it as dictionary
                            message[part.get_content_type()] = part.get_payload()
                        print(message["text/plain"], file=file_mail) #Store Text Content of Email
                        file_mail.close()
                    except Exception as exc:
                        print("Exception in Message " + str(exc))
    except Exception as exc:
        print("Login "+str(exc))

TYPE_INP = str(input("Enter 1 for Outlook and 2 for Gmail: "))
USER = str(input("Enter UserName: "))
PASSWORD = getpass.getpass("Enter Password: ")
BASE_DIR = str(input("Enter Drive")) + ":"
if "1" in TYPE_INP:
    read_mail(USER, PASSWORD)
else:
    read_mail(USER, PASSWORD, "Gmail")