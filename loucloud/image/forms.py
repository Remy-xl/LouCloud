#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import TextField, SubmitField, IntegerField
from wtforms.validators import Required

class AddImageForm(Form):
    imagename = TextField(u'Imagename', [Required()])
    imagepath = TextField(u'Imagepath', [Required()])

    submit = SubmitField(u'Add')

