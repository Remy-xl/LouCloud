#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import TextField, SubmitField, IntegerField, SelectField
from .constants import USER_NORMAL, USER_TYPE
from wtforms.validators import Required, AnyOf

class AddUserForm(Form):
    name = TextField(u'Username', [Required()])
    password = TextField(u'Password', [Required()])
    type_code = SelectField(
        u'UserType',
        [AnyOf([str(val) for val in USER_TYPE.keys()])],
        choices=[(str(val), label) for val, label in USER_TYPE.items()],
        default=USER_NORMAL)

    submit = SubmitField(u'Add')