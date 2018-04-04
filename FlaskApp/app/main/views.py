# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:22'

# 视图，前端界面的显示响应
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from .forms import NameForm
from ..models import User
from ..email import send_email
# from flask import current_app
# from ..models import User, Role



@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/', methods=['GET', 'POST'])
def index():
    # app = current_app._get_current_object()
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            db.session.commit()
            # if app.config['FLASKY_ADMIN']:
            send_email('', 'New User', 'mail/new_user', user=user)

        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())