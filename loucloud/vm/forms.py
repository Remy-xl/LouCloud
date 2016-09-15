#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)
from wtforms.validators import Required

class AddVmForm(Form):
    vmname = TextField(u'虚拟机名字', [Required()])
    usetemplateID = IntegerField(u'使用的模板ID', [Required()])
    vmowner = IntegerField(u'虚拟机所有者', [Required()])
    vmcreatetime= TextField(u'虚拟机创建时间', [Required()])

    submit = SubmitField(u'创建')
