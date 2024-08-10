#!/usr/bin/python3

import os.path
import fmf

tree = fmf.Tree('.')

must_set = ('name','ip','purpose')
hosts = []
for node in tree.prune(keys=('ip',)):
    data = {'name': os.path.basename(node.name)}
    data.update(node.data)
    for key in must_set:
        if key not in data:
            raise Exception(f"Host node {node.name} has missing required key {key}")
    hosts.append(data)


import jinja2

print(jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./")).get_template("template.html").render(hosts=hosts))
