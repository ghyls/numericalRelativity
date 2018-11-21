# -*- coding: utf-8 -*-

from christ import christoffel

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(658, 462)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ds1 = QtWidgets.QLineEdit(self.tab)
        self.ds1.setObjectName("ds1")
        self.horizontalLayout.addWidget(self.ds1)
        self.ds2 = QtWidgets.QLineEdit(self.tab)
        self.ds2.setObjectName("ds2")
        self.horizontalLayout.addWidget(self.ds2)
        self.ds3 = QtWidgets.QLineEdit(self.tab)
        self.ds3.setObjectName("ds3")
        self.horizontalLayout.addWidget(self.ds3)
        self.ds4 = QtWidgets.QLineEdit(self.tab)
        self.ds4.setObjectName("ds4")
        self.horizontalLayout.addWidget(self.ds4)

        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.m10 = QtWidgets.QLineEdit(self.tab)
        self.m10.setObjectName("m10")
        self.gridLayout.addWidget(self.m10, 1, 0, 1, 1)
        self.m30 = QtWidgets.QLineEdit(self.tab)
        self.m30.setText("")
        self.m30.setObjectName("m30")
        self.gridLayout.addWidget(self.m30, 3, 0, 1, 1)
        self.m00 = QtWidgets.QLineEdit(self.tab)
        self.m00.setObjectName("m00")
        self.gridLayout.addWidget(self.m00, 0, 0, 1, 1)
        self.m21 = QtWidgets.QLineEdit(self.tab)
        self.m21.setText("")
        self.m21.setObjectName("m21")
        self.gridLayout.addWidget(self.m21, 2, 1, 1, 1)
        self.m12 = QtWidgets.QLineEdit(self.tab)
        self.m12.setText("")
        self.m12.setObjectName("m12")
        self.gridLayout.addWidget(self.m12, 1, 2, 1, 1)
        self.m02 = QtWidgets.QLineEdit(self.tab)
        self.m02.setText("")
        self.m02.setObjectName("m02")
        self.gridLayout.addWidget(self.m02, 0, 2, 1, 1)
        self.m03 = QtWidgets.QLineEdit(self.tab)
        self.m03.setText("")
        self.m03.setObjectName("m03")
        self.gridLayout.addWidget(self.m03, 0, 3, 1, 1)
        self.m20 = QtWidgets.QLineEdit(self.tab)
        self.m20.setText("")
        self.m20.setObjectName("m20")
        self.gridLayout.addWidget(self.m20, 2, 0, 1, 1)
        self.m01 = QtWidgets.QLineEdit(self.tab)
        self.m01.setObjectName("m01")
        self.gridLayout.addWidget(self.m01, 0, 1, 1, 1)
        self.m11 = QtWidgets.QLineEdit(self.tab)
        self.m11.setObjectName("m11")
        self.gridLayout.addWidget(self.m11, 1, 1, 1, 1)
        self.m23 = QtWidgets.QLineEdit(self.tab)
        self.m23.setText("")
        self.m23.setObjectName("m23")
        self.gridLayout.addWidget(self.m23, 2, 3, 1, 1)
        self.m31 = QtWidgets.QLineEdit(self.tab)
        self.m31.setText("")
        self.m31.setObjectName("m31")
        self.gridLayout.addWidget(self.m31, 3, 1, 1, 1)
        self.m13 = QtWidgets.QLineEdit(self.tab)
        self.m13.setText("")
        self.m13.setObjectName("m13")
        self.gridLayout.addWidget(self.m13, 1, 3, 1, 1)
        self.m22 = QtWidgets.QLineEdit(self.tab)
        self.m22.setText("")
        self.m22.setObjectName("m22")
        self.gridLayout.addWidget(self.m22, 2, 2, 1, 1)
        self.m32 = QtWidgets.QLineEdit(self.tab)
        self.m32.setText("")
        self.m32.setObjectName("m32")
        self.gridLayout.addWidget(self.m32, 3, 2, 1, 1)
        self.m33 = QtWidgets.QLineEdit(self.tab)
        self.m33.setText("")
        self.m33.setObjectName("m33")
        self.gridLayout.addWidget(self.m33, 3, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_4.raise_()
        self.ds4.raise_()
        self.label_3.raise_()
        self.m30.raise_()
        self.ds2.raise_()
        self.m20.raise_()
        self.m01.raise_()
        self.label_2.raise_()
        self.m02.raise_()
        self.ds1.raise_()
        self.m10.raise_()
        self.m12.raise_()
        self.m00.raise_()
        self.ds3.raise_()
        self.m03.raise_()
        self.m11.raise_()
        self.m11.raise_()
        self.label_5.raise_()
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 145, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cha = QtWidgets.QLineEdit(self.tab1)
        self.cha.setObjectName("cha")
        self.gridLayout_2.addWidget(self.cha, 1, 1, 1, 1)
        self.chb = QtWidgets.QLineEdit(self.tab1)
        self.chb.setObjectName("chb")
        self.gridLayout_2.addWidget(self.chb, 1, 2, 1, 1)
        self.chc = QtWidgets.QLineEdit(self.tab1)
        self.chc.setEnabled(True)
        self.chc.setObjectName("chc")
        self.gridLayout_2.addWidget(self.chc, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)

        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.sol = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sol.setFont(font)
        self.sol.setObjectName("sol")
        self.horizontalLayout_2.addWidget(self.sol)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(235, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.pushButton.raise_()
        self.chc.raise_()
        self.label.raise_()
        self.chb.raise_()
        self.cha.raise_()
        self.pushButton.raise_()
        self.label_6.raise_()
        self.sol.raise_()
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Christoffel Symbols Calculator"))

        self.ds1.setText(_translate("TabWidget", "t"))
        self.ds2.setText(_translate("TabWidget", "r"))
        self.ds3.setText(_translate("TabWidget", "th"))
        self.ds4.setText(_translate("TabWidget", "fi"))


        
        self.label_3.setText(_translate("TabWidget", "Metric (start from the up-left corner):"))
        self.label_2.setText(_translate("TabWidget", "Order of the variables in the interval:"))
        self.label_4.setText(_translate("TabWidget", "Note: leave extra dimensions blank"))

        self.m00.setText(_translate("TabWidget", "-(1-2*G*M/r)"))
        self.m11.setText(_translate("TabWidget", "1/(1-2*G*M/r)"))
        self.m22.setText(_translate("TabWidget", "r**2"))
        self.m33.setText(_translate("TabWidget", "r**2*sin(th)**2"))

        self.label_5.setText(_translate("TabWidget", "Note: You can use the following symbolic constants: G, M, R, C1, C2, C3"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Inputs"))
        self.cha.setText(_translate("TabWidget", "r"))
        self.chb.setText(_translate("TabWidget", "fi"))
        self.chc.setText(_translate("TabWidget", "fi"))
        self.label.setText(_translate("TabWidget", "Γ"))
        self.pushButton.setText(_translate("TabWidget", "calculate"))
        self.label_6.setText(_translate("TabWidget", "Result:"))
        self.sol.setText(_translate("TabWidget", ""))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Calculations"))

    def calculate(self):

        ds = [self.ds1.text(), self.ds2.text(), self.ds3.text(), self.ds4.text()]
        g_mn = [[self.m00.text(), self.m01.text(), self.m02.text(), self.m03.text()], \
                [self.m10.text(), self.m11.text(), self.m12.text(), self.m13.text()], \
                [self.m20.text(), self.m21.text(), self.m22.text(), self.m23.text()], \
                [self.m30.text(), self.m31.text(), self.m32.text(), self.m33.text()], \
                ]
        abc = [self.cha.text(), self.chb.text(), self.chc.text()]
        result = str(christoffel(ds, g_mn, abc))
        self.sol.setText(result)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

