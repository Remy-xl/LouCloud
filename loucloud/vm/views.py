#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required
from .forms import AddVmForm
from .models import Vm
from ..extensions import db
from ..decorators import admin_required

vm = Blueprint('vm', __name__, url_prefix='/vms')

@vm.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    if request.method == 'GET':
        form = AddVmForm()
        vm_list = Vm.query.filter().all()
        return render_template("vm/index.html", form=form, vm_list=vm_list)

    else:
        form = AddVmForm(request.form)
        if form.validate_on_submit():
            vm_instance = Vm()
            form.populate_obj(vm_instance)
            db.session.add(vm_instance)
            db.session.commit()
        return redirect(url_for('vm.index'))


@vm.route('/<int:vm_id>/delete', methods=['GET'])
@login_required
@admin_required
def delete_vm(vm_id):
    vm_instance = Vm.query.filter(Vm.id==vm_id).first()
    if vm_instance:
        db.session.delete(vm_instance)
        db.session.commit()
    return redirect(url_for('vm.index'))
