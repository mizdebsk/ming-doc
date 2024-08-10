#!/usr/bin/python3

import os.path
import fmf

tree = fmf.Tree('.')

must_set = (
    'name',
    'ip',
    'purpose',
    'model',
    'os',
    'cpu/model',
    'cpu/cores',
    'memory/size',
    'memory/type',
    'memory/speed',
    'memory/config',
    'location/site',
    'location/room',
)

def check(node, path, data):
    curr_path = ''
    for key in path.split('/'):
        if not curr_path:
            curr_path = key
        else:
            curr_path = curr_path + '/' + key
        if key not in data:
            raise Exception(f"Host node {node.name} has missing required key {curr_path}")
        data = data[key]
        

hosts = []
for node in tree.prune(keys=('ip',)):
    data = {'name': os.path.basename(node.name)}
    data.update(node.data)
    for key in must_set:
        check(node, key, data)
    hosts.append(data)


import jinja2

print(jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./")).get_template("template.html").render(hosts=hosts))
