# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Graph(object):
    def setupUi(self, Dialog_Graph):
        Dialog_Graph.setObjectName("Dialog_Graph")
        Dialog_Graph.resize(803, 678)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Graph)
        self.buttonBox.setGeometry(QtCore.QRect(410, 600, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog_Graph)
        self.graphicsView.setGeometry(QtCore.QRect(130, 90, 481, 361))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Dialog_Graph)
        self.buttonBox.accepted.connect(Dialog_Graph.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Graph.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Graph)

    def retranslateUi(self, Dialog_Graph):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Graph.setWindowTitle(_translate("Dialog_Graph", "Dialog"))
