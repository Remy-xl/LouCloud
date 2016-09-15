#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)
from wtforms.validators import Required

class AddTemplateForm(Form):
    templatename = TextField(u'模板名', [Required()])
    relateimageID = IntegerField(u'关联的镜像ID', [Required()])
    cpunum = IntegerField(u'cpu数目', [Required()])
    ramnum = IntegerField(u'内存数目', [Required()])

    submit = SubmitField(u'创建')
