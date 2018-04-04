# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:24'

# 管理文件，通过该文件生成数据库文件与表
import os
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manage = Manager(app)
migrate = Migrate(app, db)


manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()

