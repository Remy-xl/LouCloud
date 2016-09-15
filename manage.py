#!/usr/bin/env python
# encoding: utf-8

from loucloud import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from loucloud.user import User, USER_ADMIN, USER_NORMAL

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    admin = User(
            name=u'admin',
            password=u'123456',
            type_code=USER_ADMIN)
    demo = User(
            name=u'demo',
            password=u'123456',
            type_code=USER_NORMAL)
    db.session.add(admin)
    db.session.add(demo)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
