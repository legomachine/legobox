# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/pipeline/inhouse/DCC/maya/int/modules/rigging/lego/scripts/lego/blocks/legobox/blockrootui.ui',
# licensing of 'D:/pipeline/inhouse/DCC/maya/int/modules/rigging/lego/scripts/lego/blocks/legobox/blockrootui.ui' applies.
#
# Created: Mon Mar  8 12:49:47 2021
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 459)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.name_le = QtWidgets.QLineEdit(self.groupBox)
        self.name_le.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name_le.setObjectName("name_le")
        self.gridLayout_3.addWidget(self.name_le, 0, 1, 1, 1)
        self.notes_pte = QtWidgets.QPlainTextEdit(self.groupBox)
        self.notes_pte.setObjectName("notes_pte")
        self.gridLayout_3.addWidget(self.notes_pte, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabs_widget = QtWidgets.QTabWidget(Form)
        self.tabs_widget.setAutoFillBackground(False)
        self.tabs_widget.setDocumentMode(False)
        self.tabs_widget.setTabsClosable(False)
        self.tabs_widget.setMovable(False)
        self.tabs_widget.setTabBarAutoHide(False)
        self.tabs_widget.setObjectName("tabs_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pre_add_btn = QtWidgets.QPushButton(self.tab)
        self.pre_add_btn.setObjectName("pre_add_btn")
        self.verticalLayout.addWidget(self.pre_add_btn)
        self.pre_new_btn = QtWidgets.QPushButton(self.tab)
        self.pre_new_btn.setObjectName("pre_new_btn")
        self.verticalLayout.addWidget(self.pre_new_btn)
        self.pre_dup_btn = QtWidgets.QPushButton(self.tab)
        self.pre_dup_btn.setObjectName("pre_dup_btn")
        self.verticalLayout.addWidget(self.pre_dup_btn)
        self.pre_remove_btn = QtWidgets.QPushButton(self.tab)
        self.pre_remove_btn.setObjectName("pre_remove_btn")
        self.verticalLayout.addWidget(self.pre_remove_btn)
        self.pre_run_btn = QtWidgets.QPushButton(self.tab)
        self.pre_run_btn.setObjectName("pre_run_btn")
        self.verticalLayout.addWidget(self.pre_run_btn)
        self.pre_edit_btn = QtWidgets.QPushButton(self.tab)
        self.pre_edit_btn.setObjectName("pre_edit_btn")
        self.verticalLayout.addWidget(self.pre_edit_btn)
        self.pre_export_btn = QtWidgets.QPushButton(self.tab)
        self.pre_export_btn.setObjectName("pre_export_btn")
        self.verticalLayout.addWidget(self.pre_export_btn)
        self.pre_import_btn = QtWidgets.QPushButton(self.tab)
        self.pre_import_btn.setObjectName("pre_import_btn")
        self.verticalLayout.addWidget(self.pre_import_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.pre_scripts_view = QtWidgets.QListWidget(self.tab)
        self.pre_scripts_view.setObjectName("pre_scripts_view")
        self.gridLayout.addWidget(self.pre_scripts_view, 1, 0, 1, 1)
        self.pre_cbox = QtWidgets.QCheckBox(self.tab)
        self.pre_cbox.setObjectName("pre_cbox")
        self.gridLayout.addWidget(self.pre_cbox, 0, 0, 1, 1)
        self.tabs_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs_widget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.post_cbox = QtWidgets.QCheckBox(self.tab_3)
        self.post_cbox.setObjectName("post_cbox")
        self.gridLayout_2.addWidget(self.post_cbox, 0, 0, 1, 1)
        self.post_scripts_view = QtWidgets.QListWidget(self.tab_3)
        self.post_scripts_view.setObjectName("post_scripts_view")
        self.gridLayout_2.addWidget(self.post_scripts_view, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.post_add_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_add_btn.setObjectName("post_add_btn")
        self.verticalLayout_2.addWidget(self.post_add_btn)
        self.post_new_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_new_btn.setObjectName("post_new_btn")
        self.verticalLayout_2.addWidget(self.post_new_btn)
        self.post_dup_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_dup_btn.setObjectName("post_dup_btn")
        self.verticalLayout_2.addWidget(self.post_dup_btn)
        self.post_remove_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_remove_btn.setObjectName("post_remove_btn")
        self.verticalLayout_2.addWidget(self.post_remove_btn)
        self.post_run_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_run_btn.setObjectName("post_run_btn")
        self.verticalLayout_2.addWidget(self.post_run_btn)
        self.post_edit_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_edit_btn.setObjectName("post_edit_btn")
        self.verticalLayout_2.addWidget(self.post_edit_btn)
        self.post_export_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_export_btn.setObjectName("post_export_btn")
        self.verticalLayout_2.addWidget(self.post_export_btn)
        self.post_import_btn = QtWidgets.QPushButton(self.tab_3)
        self.post_import_btn.setObjectName("post_import_btn")
        self.verticalLayout_2.addWidget(self.post_import_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.tabs_widget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.picker_path_le = QtWidgets.QLineEdit(self.tab_4)
        self.picker_path_le.setObjectName("picker_path_le")
        self.horizontalLayout.addWidget(self.picker_path_le)
        self.picker_import_btn = QtWidgets.QPushButton(self.tab_4)
        self.picker_import_btn.setObjectName("picker_import_btn")
        self.horizontalLayout.addWidget(self.picker_import_btn)
        self.tabs_widget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabs_widget)

        self.retranslateUi(Form)
        self.tabs_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Rig", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Rig Name", None, -1))
        self.name_le.setText(QtWidgets.QApplication.translate("Form", "rig", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Notes", None, -1))
        self.pre_add_btn.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))
        self.pre_new_btn.setText(QtWidgets.QApplication.translate("Form", "New", None, -1))
        self.pre_dup_btn.setText(QtWidgets.QApplication.translate("Form", "Duplicate", None, -1))
        self.pre_remove_btn.setText(QtWidgets.QApplication.translate("Form", "Remove", None, -1))
        self.pre_run_btn.setText(QtWidgets.QApplication.translate("Form", "Run Sel", None, -1))
        self.pre_edit_btn.setText(QtWidgets.QApplication.translate("Form", "Edit", None, -1))
        self.pre_export_btn.setText(QtWidgets.QApplication.translate("Form", "Export", None, -1))
        self.pre_import_btn.setText(QtWidgets.QApplication.translate("Form", "Import", None, -1))
        self.pre_cbox.setText(QtWidgets.QApplication.translate("Form", "Pre Scripts", None, -1))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "PreScripts", None, -1))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "skin", None, -1))
        self.post_cbox.setText(QtWidgets.QApplication.translate("Form", "Post Scripts", None, -1))
        self.post_add_btn.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))
        self.post_new_btn.setText(QtWidgets.QApplication.translate("Form", "New", None, -1))
        self.post_dup_btn.setText(QtWidgets.QApplication.translate("Form", "Duplicate", None, -1))
        self.post_remove_btn.setText(QtWidgets.QApplication.translate("Form", "Remove", None, -1))
        self.post_run_btn.setText(QtWidgets.QApplication.translate("Form", "Run Sel", None, -1))
        self.post_edit_btn.setText(QtWidgets.QApplication.translate("Form", "Edit", None, -1))
        self.post_export_btn.setText(QtWidgets.QApplication.translate("Form", "Export", None, -1))
        self.post_import_btn.setText(QtWidgets.QApplication.translate("Form", "Import", None, -1))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_3), QtWidgets.QApplication.translate("Form", "PostScripts", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Import Picker", None, -1))
        self.picker_import_btn.setText(QtWidgets.QApplication.translate("Form", "Import", None, -1))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_4), QtWidgets.QApplication.translate("Form", "Picker", None, -1))

