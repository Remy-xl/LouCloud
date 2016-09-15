#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required
from ..decorators import admin_required
from .models import User
from .forms import AddUserForm
from ..extensions import db

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/', methods=['GET'])
@login_required
def index():
    return render_template("user/index.html")
    
@user.route('/admin', methods=['GET', 'POST'])
@login_required
@admin_required
def admin():
    if request.method == 'GET':
        form = AddUserForm()
        users = User.query.filter().all()
        return render_template("user/admin.html", form=form, users=users)
    else:
        form = AddUserForm(request.form)
        if form.validate_on_submit():
            user_instance = User()
            form.populate_obj(user_instance)
            db.session.add(user_instance)
            db.session.commit()
        return redirect(url_for('user.admin'))

@user.route('/<int:user_id>/delete', methods=['GET'])
@login_required
@admin_required
def delete_user(user_id):
    user_instance = User.query.filter(User.id==user_id).first()
    if user_instance:
        db.session.delete(user_instance)
        db.session.commit()
    return redirect(url_for('user.admin'))