# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:31'

from flask import current_app, render_template
from flask_mail import Message
from threading import Thread
from app import mail



def send_async_emial(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    # msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    #               sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    # msg.body = render_template(template+ '.txt', **kwargs)
    # msg.html = render_template(template+'.html', **kwargs)
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender=app.config['MAIL_USERNAME'], recipients=['1227314815@qq.com'])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_emial, args=[app, msg])
    thr.start()
    return thr