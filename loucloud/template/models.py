#!/usr/bin/env python
# encoding: utf-8


from sqlalchemy import Column
from ..extensions import db
from .constants import TEMPLATE_OK
from .constants import TEMPLATE_CPUNUM
from .constants import TEMPLATE_RAMNUM

class Template(db.Model):

    __tablename__ = 'templates'

    id = Column(db.Integer, primary_key=True)
    templatename = Column(db.String(32), default="shiyanlou")
    relateimageID = Column(db.SmallInteger, default= TEMPLATE_OK)
    cpunum = Column(db.SmallInteger, default= TEMPLATE_CPUNUM)
    ramnum = Column(db.SmallInteger, default= TEMPLATE_RAMNUM)
