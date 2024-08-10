#!/usr/bin/python3

import os.path
import fmf

tree = fmf.Tree('.')

hosts = []
for node in tree.prune(keys=('ip',)):
    data = {'name': os.path.basename(node.name)}
    data.update(node.data)
    hosts.append(data)


import jinja2

print(jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./")).get_template("template.html").render(hosts=hosts))
