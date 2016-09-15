#!/usr/bin/env python
# encoding: utf-8


from sqlalchemy import Column
from ..extensions import db
from .constants import VM_OK


class Vm(db.Model):

    __tablename__ = 'vms'

    id = Column(db.Integer, primary_key=True)
    vmname = Column(db.String(32), default="vm1")
    usetemplateID = Column(db.SmallInteger, default=VM_OK)
    vmowner = Column(db.SmallInteger, default=VM_OK)
    vmcreatetime = Column(db.String(32), default="2015-8-4")

