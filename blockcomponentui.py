# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/pipeline/inhouse/DCC/maya/int/modules/rigging/lego/scripts/lego/blocks/legobox/blockcomponentui.ui',
# licensing of 'D:/pipeline/inhouse/DCC/maya/int/modules/rigging/lego/scripts/lego/blocks/legobox/blockcomponentui.ui' applies.
#
# Created: Mon Mar  8 12:49:57 2021
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 289)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(90, 0))
        self.label_6.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.parent_le = QtWidgets.QLineEdit(self.groupBox)
        self.parent_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parent_le.setReadOnly(True)
        self.parent_le.setObjectName("parent_le")
        self.gridLayout.addWidget(self.parent_le, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(90, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ref_cbbox = QtWidgets.QComboBox(self.groupBox)
        self.ref_cbbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ref_cbbox.setObjectName("ref_cbbox")
        self.ref_cbbox.addItem("")
        self.gridLayout.addWidget(self.ref_cbbox, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(90, 0))
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.name_le = QtWidgets.QLineEdit(self.groupBox)
        self.name_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_le.setObjectName("name_le")
        self.gridLayout.addWidget(self.name_le, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(90, 0))
        self.label_4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.side_le = QtWidgets.QLineEdit(self.groupBox)
        self.side_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.side_le.setObjectName("side_le")
        self.gridLayout.addWidget(self.side_le, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        self.label_5.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.index_spbox = QtWidgets.QSpinBox(self.groupBox)
        self.index_spbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.index_spbox.setObjectName("index_spbox")
        self.gridLayout.addWidget(self.index_spbox, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(90, 0))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.ui_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.ui_le.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ui_le.setObjectName("ui_le")
        self.gridLayout_2.addWidget(self.ui_le, 0, 1, 1, 1)
        self.ui_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ui_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ui_btn.setObjectName("ui_btn")
        self.gridLayout_2.addWidget(self.ui_btn, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.joint_cbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.joint_cbox.setChecked(True)
        self.joint_cbox.setObjectName("joint_cbox")
        self.verticalLayout.addWidget(self.joint_cbox)
        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "parent", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "reference space", None, -1))
        self.ref_cbbox.setItemText(0, QtWidgets.QApplication.translate("Form", "default", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "name", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "side", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "index", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "UI", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "UI Root", None, -1))
        self.ui_btn.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Form", "outputs", None, -1))
        self.joint_cbox.setText(QtWidgets.QApplication.translate("Form", "joint", None, -1))

