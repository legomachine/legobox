# -*- coding:utf-8 -*-
""" create block guide """

from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

from lego.blocks import blueprint
from lego.blocks import guide
from lego.core.api import const

# mgear
from mgear.core import (
    node, 
    fcurve, 
    applyop, 
    vector, 
    icon,
    attribute,
    transform,
    primitive,
    pyqt
)
from mgear.vendor.Qt import QtWidgets, QtCore

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya.app.general.mayaMixin import MayaQDockWidget

# maya
import pymel.core as pm 
import pymel.core.datatypes as dt

from setting import Ui_Form as sui

BLOCK_TYPE          = "LEGO_00"
BLOCK_VERSION       = "0.0.0"
BLOCK_NAME          = "control"
BLOCK_SIDE          = "C"


def draw():
    parent, p_network = blueprint.is_guide()
    if not parent:
        parent, p_network = blueprint.init_guide_hierarchy()

    origin = dt.Vector(0, 0, 0)
    origin_matrix = transform.getTransformFromPos(origin)

    BLOCK_INDEX = blueprint.find_index(name=BLOCK_NAME, side=BLOCK_SIDE)
    root = icon.guideRootIcon(parent, name="{0}_{1}{2}_root".format(BLOCK_NAME, BLOCK_SIDE, BLOCK_INDEX), width=1, color=[1, 0, 0], m=origin_matrix)
    root.isGearGuide.delete()
    attribute.addAttribute(root, const.ISLEGOGUIDE, "bool", True, keyable=False)
    attribute.addAttribute(root, const.ISROOT, "bool", True, keyable=False)

    network = blueprint.add_network(root)
    network.attr(const.BLOCK_TYPE).set(BLOCK_TYPE)
    network.attr(const.BLOCK_VERSION).set(BLOCK_VERSION)
    network.attr(const.BLOCK_NAME).set(BLOCK_NAME)
    network.attr(const.BLOCK_SIDE).set(BLOCK_SIDE)
    network.attr(const.BLOCK_INDEX).set(BLOCK_INDEX)

    p_network.attr(const.CHILDREN) >> network.attr(const.BLOCK_PARENT)

def get_positions():
    pass


# block setting ui
###################
class BlockSettingTab(QtWidgets.QDialog, sui):
    """ setting tab """
    
    def __init__(self, parent=None):
        super(BlockSettingTab, self).__init__(parent=parent)
        self.setupUi(self)
    
# setting ui
#############
class Settings(MayaQWidgetDockableMixin, guide.BlockComponentUI):
    """ settings window """

    def __init__(Self, parent=None):
        pyqt.deleteInstances(self, MayaQDockWidget)

        super(Settings, self).__init__(parent=parent)
        self.setting_tab = BlockSettingTab()
