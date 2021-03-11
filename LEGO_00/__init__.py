# -*- coding:utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# maya
import pymel.core as pm

# lego
from lego.core.api import log, const
from lego.blocks import lib

LEGO = "LEGO_00"
VERSION = "0.0.0"

def build(context, node, step):
    log.log(level=0, msg="step : {0}\ntype : {1}\nversion : [2}".format(step, LEGO, VERSION))
    if step == 0:
        create_object(context, node)
    elif step == 1:
        create_attribute(context, node)
    elif step == 2:
        create_connections(context, node)

def create_object(context, node):
    pass

def create_attribute(context, node):
    pass

def create_connections(context, node):
    pass

def get_output(node):
    name_format = nameRule.format(name=name, side=side, index=index, description="{description}", extension="{extension}")
    output = [lib.get_node_name(name_format, "", "out")]
    return output
