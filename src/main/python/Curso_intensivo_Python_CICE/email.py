# -*- coding: utf-8 -*-
"""

"""
import smtplib

me = input('meter mi email aqui: ')
passw = input('meter mi pass: ')
destino = input('meter el email del destinatario final: ')
destino_cc = input('meter email en copia: ')
asunto = input('meter el asunto del email: ')
mensjae = input('cuerpo del email: ')

server = smtplib.SMTP(smtpserver)

def sendemail(from_addr, to_addr_list, cc_addr_list,subject, message,login, password,smtpserver='smtp.gmail.com:587'):
    header  = f'From: {from_addr}'
    header += f'To: {to_addr_list}'
    header += f'Cc: {cc_addr_list}'
    header += f'Subject:{subject}'
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(me,passw)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    

    
sendemail(me, destino, destino_cc, asunto, mensaje, me, passw) 
