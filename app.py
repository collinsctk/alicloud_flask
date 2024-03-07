#!/usr/bin/env python3.8
# -*- coding=utf-8 -*-

from flask import Flask, render_template
import os
from database.orm_search_data import get_all_users
import requests

# 默认目录为当前目录的templates
template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)

app.debug = True


@app.route('/')
def index():
    instance_id = requests.get("http://100.100.100.200/latest/meta-data/instance-id").text
    region_id = requests.get("http://100.100.100.200/latest/meta-data/region-id").text
    return render_template('index.html',
                           devnet_main='乾颐堂AWS测试',
                           instance_id=instance_id,
                           region_id=region_id,
                           active='首页')


@app.route('/staff_info')
def staff_info():
    staff_list = get_all_users()
    return render_template('staff.html', staff_list=staff_list, active='员工信息')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
