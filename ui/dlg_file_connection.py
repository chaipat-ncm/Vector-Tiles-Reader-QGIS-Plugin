# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_file_connection.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DlgFileConnection(object):
    def setupUi(self, DlgFileConnection):
        DlgFileConnection.setObjectName(_fromUtf8("DlgFileConnection"))
        DlgFileConnection.setWindowModality(QtCore.Qt.WindowModal)
        DlgFileConnection.resize(1057, 705)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgFileConnection.sizePolicy().hasHeightForWidth())
        DlgFileConnection.setSizePolicy(sizePolicy)
        DlgFileConnection.setMinimumSize(QtCore.QSize(573, 655))
        DlgFileConnection.setSizeGripEnabled(False)
        DlgFileConnection.setModal(True)
        self.gridLayout_4 = QtGui.QGridLayout(DlgFileConnection)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(DlgFileConnection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 190))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 981, 330))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.chkMergeTiles = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.chkMergeTiles.setChecked(False)
        self.chkMergeTiles.setObjectName(_fromUtf8("chkMergeTiles"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.chkMergeTiles)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.rbZoomMax = QtGui.QRadioButton(self.formLayoutWidget_2)
        self.rbZoomMax.setChecked(True)
        self.rbZoomMax.setObjectName(_fromUtf8("rbZoomMax"))
        self.buttonGroup_2 = QtGui.QButtonGroup(DlgFileConnection)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rbZoomMax)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.rbZoomMax)
        self.rbZoomAuto = QtGui.QRadioButton(self.formLayoutWidget_2)
        self.rbZoomAuto.setObjectName(_fromUtf8("rbZoomAuto"))
        self.buttonGroup_2.addButton(self.rbZoomAuto)
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.rbZoomAuto)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.spinNrOfLoadedTiles = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinNrOfLoadedTiles.setEnabled(False)
        self.spinNrOfLoadedTiles.setMinimumSize(QtCore.QSize(0, 21))
        self.spinNrOfLoadedTiles.setMinimum(1)
        self.spinNrOfLoadedTiles.setMaximum(9999)
        self.spinNrOfLoadedTiles.setProperty("value", 10)
        self.spinNrOfLoadedTiles.setObjectName(_fromUtf8("spinNrOfLoadedTiles"))
        self.gridLayout_5.addWidget(self.spinNrOfLoadedTiles, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chkLimitNrOfTiles = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.chkLimitNrOfTiles.setObjectName(_fromUtf8("chkLimitNrOfTiles"))
        self.gridLayout_5.addWidget(self.chkLimitNrOfTiles, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.SpanningRole, self.gridLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbZoomManual = QtGui.QRadioButton(self.formLayoutWidget_2)
        self.rbZoomManual.setText(_fromUtf8(""))
        self.rbZoomManual.setObjectName(_fromUtf8("rbZoomManual"))
        self.buttonGroup_2.addButton(self.rbZoomManual)
        self.horizontalLayout.addWidget(self.rbZoomManual)
        self.zoomSpin = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.zoomSpin.setEnabled(False)
        self.zoomSpin.setMaximumSize(QtCore.QSize(70, 16777215))
        self.zoomSpin.setObjectName(_fromUtf8("zoomSpin"))
        self.horizontalLayout.addWidget(self.zoomSpin, QtCore.Qt.AlignLeft)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout_2.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.chkApplyStyles = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.chkApplyStyles.setChecked(True)
        self.chkApplyStyles.setObjectName(_fromUtf8("chkApplyStyles"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.SpanningRole, self.chkApplyStyles)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout_2.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btnOpen = QtGui.QPushButton(DlgFileConnection)
        self.btnOpen.setEnabled(False)
        self.btnOpen.setCheckable(False)
        self.btnOpen.setDefault(False)
        self.btnOpen.setFlat(False)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.horizontalLayout_2.addWidget(self.btnOpen)
        self.btnCancel = QtGui.QPushButton(DlgFileConnection)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(DlgFileConnection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBrowse = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/vectortilereader/folder.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowse.setIcon(icon)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 0, 2, 1, 1, QtCore.Qt.AlignVCenter)
        self.lblError = QtGui.QLabel(self.groupBox)
        self.lblError.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.lblError.setScaledContents(False)
        self.lblError.setWordWrap(True)
        self.lblError.setIndent(-1)
        self.lblError.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblError.setObjectName(_fromUtf8("lblError"))
        self.gridLayout.addWidget(self.lblError, 1, 1, 1, 2, QtCore.Qt.AlignTop)
        self.txtPath = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPath.sizePolicy().hasHeightForWidth())
        self.txtPath.setSizePolicy(sizePolicy)
        self.txtPath.setMinimumSize(QtCore.QSize(20, 0))
        self.txtPath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        self.gridLayout.addWidget(self.txtPath, 0, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(DlgFileConnection)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgFileConnection.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgFileConnection)

    def retranslateUi(self, DlgFileConnection):
        DlgFileConnection.setWindowTitle(_translate("DlgFileConnection", "Add Vector Tile Layer", None))
        self.groupBox_2.setTitle(_translate("DlgFileConnection", "Options", None))
        self.chkMergeTiles.setText(_translate("DlgFileConnection", "Merge Tiles (disable for performance)", None))
        self.label_5.setText(_translate("DlgFileConnection", "Zoom", None))
        self.rbZoomMax.setText(_translate("DlgFileConnection", "Max. Zoom", None))
        self.rbZoomAuto.setText(_translate("DlgFileConnection", "Auto (scale-dependent)", None))
        self.chkLimitNrOfTiles.setText(_translate("DlgFileConnection", "Limit the number of loaded tiles", None))
        self.chkApplyStyles.setText(_translate("DlgFileConnection", "Apply default styles for OpenMapTiles", None))
        self.btnOpen.setText(_translate("DlgFileConnection", "Open", None))
        self.btnCancel.setText(_translate("DlgFileConnection", "Cancel", None))
        self.groupBox.setTitle(_translate("DlgFileConnection", "Source", None))
        self.btnBrowse.setText(_translate("DlgFileConnection", "Browse", None))
        self.lblError.setText(_translate("DlgFileConnection", "Show any errors here", None))
        self.label_2.setText(_translate("DlgFileConnection", "Source", None))

import resources_rc
