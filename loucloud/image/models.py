#!/usr/bin/env python
# encoding: utf-8


from sqlalchemy import Column
from ..extensions import db
from .constants import IMAGE_OK


class Image(db.Model):

    __tablename__ = 'images'

    id = Column(db.Integer, primary_key=True)
    imagename = Column(db.String(32), default="shiyanlou")
    imagepath = Column(db.String(32), default="shiyanlou")

