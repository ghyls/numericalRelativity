# -*- coding: utf-8 -*-


from christ import christoffel
from riem import riemman
#import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):


    # font_0
    font_0 = QtGui.QFont()
    font_0.setFamily("Liberation Serif")
    font_0.setPointSize(20)

    font_1 = QtGui.QFont()
    font_1.setFamily("DejaVu Math TeX Gyre")
    font_1.setPointSize(15)

    font_2 = QtGui.QFont()
    font_2.setFamily("DejaVu Math TeX Gyre")
    font_2.setPointSize(60)

    font_3 = QtGui.QFont()
    font_3.setFamily("DejaVu Math TeX Gyre")
    font_3.setPointSize(18)

    def setupUi(self, TabWidget):

        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(776, 513)
        TabWidget.setWindowTitle("Numerical Relativity TOOLS")


        # Inputs Tab >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # set it up
        self.inputsTab = QtWidgets.QWidget()
        self.inputsTab.setObjectName("inputsTab")
        
        TabWidget.addTab(self.inputsTab, "")
        TabWidget.setTabText(TabWidget.indexOf(self.inputsTab), "Inputs")

        # define the grid
        self.tab0_grid_main = QtWidgets.QGridLayout(self.inputsTab)
        self.tab0_grid_main.setContentsMargins(0, 0, 0, 0)
        self.tab0_grid_main.setObjectName("tab0_grid_main")


        # Inputs for the interval
        # > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > 
        # horizontal layout for the inputs
        self.tab0_box_interval = QtWidgets.QHBoxLayout()
        self.tab0_box_interval.setObjectName("tab0_box_interval")

        self.ds1 = QtWidgets.QLineEdit(self.inputsTab)
        self.ds2 = QtWidgets.QLineEdit(self.inputsTab)
        self.ds3 = QtWidgets.QLineEdit(self.inputsTab)
        self.ds4 = QtWidgets.QLineEdit(self.inputsTab)

        self.ds1.setObjectName("ds1")
        self.ds2.setObjectName("ds2")
        self.ds3.setObjectName("ds3")
        self.ds4.setObjectName("ds4")

        self.tab0_box_interval.addWidget(self.ds1)
        self.tab0_box_interval.addWidget(self.ds2)
        self.tab0_box_interval.addWidget(self.ds3)
        self.tab0_box_interval.addWidget(self.ds4)

        self.ds1.setText("t")
        self.ds2.setText("r")
        self.ds3.setText("th")
        self.ds4.setText("fi")

        self.tab0_grid_main.addLayout(self.tab0_box_interval, 3, 0, 2, 3)
        # < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < 


        # main matrix 
        # > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > 
        self.m00 = QtWidgets.QLineEdit(self.inputsTab)
        self.m01 = QtWidgets.QLineEdit(self.inputsTab)
        self.m02 = QtWidgets.QLineEdit(self.inputsTab)
        self.m03 = QtWidgets.QLineEdit(self.inputsTab)

        self.m10 = QtWidgets.QLineEdit(self.inputsTab)
        self.m11 = QtWidgets.QLineEdit(self.inputsTab)
        self.m12 = QtWidgets.QLineEdit(self.inputsTab)
        self.m13 = QtWidgets.QLineEdit(self.inputsTab)

        self.m20 = QtWidgets.QLineEdit(self.inputsTab)
        self.m21 = QtWidgets.QLineEdit(self.inputsTab)                
        self.m22 = QtWidgets.QLineEdit(self.inputsTab)
        self.m23 = QtWidgets.QLineEdit(self.inputsTab)

        self.m30 = QtWidgets.QLineEdit(self.inputsTab)
        self.m31 = QtWidgets.QLineEdit(self.inputsTab)
        self.m32 = QtWidgets.QLineEdit(self.inputsTab)
        self.m33 = QtWidgets.QLineEdit(self.inputsTab)

        self.m00.setObjectName("m00")
        self.m01.setObjectName("m01")
        self.m02.setObjectName("m02")
        self.m03.setObjectName("m03")

        self.m10.setObjectName("m10")
        self.m11.setObjectName("m11")
        self.m12.setObjectName("m12")
        self.m13.setObjectName("m13")

        self.m20.setObjectName("m20")
        self.m21.setObjectName("m21")
        self.m22.setObjectName("m22")
        self.m23.setObjectName("m23")

        self.m30.setObjectName("m30")
        self.m31.setObjectName("m31")
        self.m32.setObjectName("m32")
        self.m33.setObjectName("m33")

        self.m00.setText("-(1-2*G*M/r)")
        self.m11.setText("1/(1-2*G*M/r)")
        self.m22.setText("r**2")
        self.m33.setText("r**2*sin(th)**2")

        # define the grid for the matrix and allocate the elements
        self.tab0_grid_matrix = QtWidgets.QGridLayout()
        self.tab0_grid_matrix.setObjectName("tab0_grid_matrix")
        self.tab0_grid_main.addLayout(self.tab0_grid_matrix, 6, 0, 1, 3)

        self.tab0_grid_matrix.addWidget(self.m00, 0, 0, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m01, 0, 1, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m02, 0, 2, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m03, 0, 3, 1, 1)

        self.tab0_grid_matrix.addWidget(self.m10, 1, 0, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m11, 1, 1, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m12, 1, 2, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m13, 1, 3, 1, 1)
        
        self.tab0_grid_matrix.addWidget(self.m20, 2, 0, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m21, 2, 1, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m22, 2, 2, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m23, 2, 3, 1, 1)
        
        self.tab0_grid_matrix.addWidget(self.m30, 3, 0, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m31, 3, 1, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m32, 3, 2, 1, 1)
        self.tab0_grid_matrix.addWidget(self.m33, 3, 3, 1, 1)
        # < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < 


        # Labels 
        # > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > 
        #copyright
        self.label_11 = QtWidgets.QLabel(self.inputsTab)
        self.label_11.setObjectName("label_11")

        self.tab0_grid_main.addWidget(self.label_11, 12, 2, 1, 1)
        self.label_11.setText("Copyright (c) 2019 Diego Valledor & Mario González, released under the MIT License ")
        self.label_11.raise_()

        # interval order
        self.label_2 = QtWidgets.QLabel(self.inputsTab)
        self.label_2.setObjectName("label_2")

        self.tab0_grid_main.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_2.setText("Order of the variables in the interval:")
        self.label_2.raise_()

        # extra dimensions
        self.label_4 = QtWidgets.QLabel(self.inputsTab)
        self.label_4.setObjectName("label_4")
        
        self.tab0_grid_main.addWidget(self.label_4, 8, 0, 1, 3)
        self.label_4.setText("Note: leave extra dimensions empty")
        self.label_4.raise_()

        # extra constants
        self.label_4 = QtWidgets.QLabel(self.inputsTab)
        self.label_4.setObjectName("label_4")
        
        self.tab0_grid_main.addWidget(self.label_4, 9, 0, 1, 3)
        self.label_4.setText("Note: Unknown symbols are treated as constants in the above matrix,\n"
                             "            Feel free to use as many as you want.")
        self.label_4.raise_()

        # Metric
        self.label_3 = QtWidgets.QLabel(self.inputsTab)
        self.label_3.setObjectName("label_3")

        self.tab0_grid_main.addWidget(self.label_3, 5, 0, 1, 2)
        self.label_3.setText("Metric (start from the upper left corner):")
        self.label_3.raise_()
        # < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < 


        # Spacers
        # > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > 

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tab0_grid_main.addItem(spacerItem1, 4, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tab0_grid_main.addItem(spacerItem, 12, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tab0_grid_main.addItem(spacerItem3, 9, 2, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tab0_grid_main.addItem(spacerItem4, 0, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tab0_grid_matrix.addItem(spacerItem2, 4, 1, 1, 1)


        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # inputsTab <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<





        # Cry Tab <<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.chTab = QtWidgets.QWidget()
        self.chTab.setObjectName("chTab")
        TabWidget.addTab(self.chTab, "")
        TabWidget.setTabText(TabWidget.indexOf(self.chTab),  "Christoffel symbols")


        # main grid
        self.chTab_grid_main = QtWidgets.QGridLayout(self.chTab)
        self.chTab_grid_main.setContentsMargins(0, 0, 0, 0)
        self.chTab_grid_main.setObjectName("chTab_grid_main")
        

        #>> verticalLayout_3
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #>>>> gridLayout_2
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        #>>>>>> label
        self.label = QtWidgets.QLabel(self.chTab)
        self.label.setFont(self.font_2)
        self.label.setObjectName("label")
        self.label.setText("Γ")

        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)
        #<<<<<< label

        #>>>>>> Ch parameters
        self.cha = QtWidgets.QLineEdit(self.chTab)
        self.cha.setObjectName("cha")
        self.cha.setText("r")

        self.chb = QtWidgets.QLineEdit(self.chTab)
        self.chb.setObjectName("chb")
        self.chb.setText("fi")

        self.chc = QtWidgets.QLineEdit(self.chTab)
        self.chc.setText("fi")
        self.chc.setObjectName("chc")
        self.chc.setEnabled(True)

        self.gridLayout_2.addWidget(self.cha, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.chb, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.chc, 0, 1, 1, 1)
        #<<<<<< Ch parameters

        self.verticalLayout_3.addLayout(self.gridLayout_2)
        #<<<< gridLayout_2

        #>>>> verticalLayout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #>>>>>> pushButton
        self.pushButton = QtWidgets.QPushButton(self.chTab)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton.setText("calculate")

        self.verticalLayout.addWidget(self.pushButton)
        #<<<<<< pushButton

        #>>>>>> chTab_hbox_result
        self.chTab_hbox_result = QtWidgets.QHBoxLayout()
        self.chTab_hbox_result.setObjectName("chTab_hbox_result")

        #>>>>>>>> label_6
        self.label_6 = QtWidgets.QLabel(self.chTab)
        self.label_6.setFont(self.font_3)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Result:")

        self.chTab_hbox_result.addWidget(self.label_6)
        #<<<<<<<< label_6

        #>>>>>>>> sol
        self.sol = QtWidgets.QLabel(self.chTab)
        
        self.sol.setFont(self.font_3)
        self.sol.setObjectName("sol")

        self.chTab_hbox_result.addWidget(self.sol)
        #<<<<<<<< sol

        self.verticalLayout.addLayout(self.chTab_hbox_result)
        #<<<<<< chTab_hbox_result

        self.verticalLayout_3.addLayout(self.verticalLayout)
        #<<<< verticalLayout

        self.chTab_grid_main.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        #<< verticalLayout_3

        #>> spacers
        spacerItem5 = QtWidgets.QSpacerItem(17, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem6 = QtWidgets.QSpacerItem(169, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem7 = QtWidgets.QSpacerItem(17, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem8 = QtWidgets.QSpacerItem(168, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.chTab_grid_main.addItem(spacerItem5, 0, 1, 1, 1)
        self.chTab_grid_main.addItem(spacerItem6, 1, 0, 1, 1)
        self.chTab_grid_main.addItem(spacerItem7, 2, 1, 1, 1)
        self.chTab_grid_main.addItem(spacerItem8, 1, 2, 1, 1)
        #<< spacers

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # Cry Tab <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



        # Rie Tab >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        TabWidget.addTab(self.tab_2, "")
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2),"Riemman tensor")

        # >> main grid
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")

        # >> >> gridLayout_7
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")

        # >> >> >> horizontalLayout_5
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # >> >> >> >> label_9
        self.label_9 = QtWidgets.QLabel(self.tab_2) 
        self.label_9.setFont(self.font_3)
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Result:")
        
        self.horizontalLayout_5.addWidget(self.label_9)
        # << << << << label_9

        # >> >> >> >> label_10
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setFont(self.font_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        # << << << << label_10

        self.gridLayout_7.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        # << << << horizontalLayout_5

        # >> >> >> horizontalLayout_4
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # >> >> >> >> label_8
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setFont(self.font_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("R")
        
        self.horizontalLayout_4.addWidget(self.label_8)
        # << << << << label_8

        # >> >> >> >> gridLayout_6
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        # >> >> >> >> >> Riemm Parameters
        self.ra = QtWidgets.QLineEdit(self.tab_2)
        self.rb = QtWidgets.QLineEdit(self.tab_2)
        self.rc = QtWidgets.QLineEdit(self.tab_2)
        self.rd = QtWidgets.QLineEdit(self.tab_2)

        self.ra.setEnabled(True)
        self.rb.setEnabled(True)
        self.rc.setEnabled(True)
        self.rd.setEnabled(True)
        
        self.ra.setObjectName("ra")
        self.rb.setObjectName("rb")
        self.rc.setObjectName("rc")
        self.rd.setObjectName("rd")

        self.rb.setText("r")
        self.ra.setText("t")
        self.rd.setText("r")
        self.rc.setText("t")

        self.ra.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rb.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rc.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rd.setMaximumSize(QtCore.QSize(30, 16777215))
        
        self.gridLayout_6.addWidget(self.ra, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.rb, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.rc, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.rd, 1, 3, 1, 1)
        # << << << << <<  Riemm Parameters

        # >> >> >> >> >> spacers
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 1, 4, 1, 1)
        # << << << << << spacers

        self.horizontalLayout_4.addLayout(self.gridLayout_6)
        # << << << << gridLayout_6

        # >> >> >> >> spacers
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        # << << << << spacers

        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        # << << << horizontalLayout_4

        # >> >> >> calculateR
        self.calculateR = QtWidgets.QPushButton(self.tab_2)
        self.calculateR.clicked.connect(self.riemmanCalc)
        self.calculateR.setObjectName("calculateR")
        self.calculateR.setText("calculate")

        self.gridLayout_7.addWidget(self.calculateR, 1, 0, 1, 1)
        # << << << calculateR

        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 1, 1, 1)
        # << << gridLayout_7

        # >> >> spacers
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.gridLayout_8.addItem(spacerItem9, 1, 0, 1, 1)
        self.gridLayout_8.addItem(spacerItem10, 1, 2, 1, 1)
        self.gridLayout_8.addItem(spacerItem11, 2, 1, 1, 1)
        self.gridLayout_8.addItem(spacerItem14, 0, 1, 1, 1)
        # << << spacers

        # << gridLayout_8

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # Rie Tab <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # Err Tab >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        TabWidget.addTab(self.tab_3, "")
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3),"Error log")

        # >> main grid
        self.tab3_grid_main = QtWidgets.QGridLayout(self.tab_3)
        self.tab3_grid_main.setContentsMargins(0, 0, 0, 0)
        self.tab3_grid_main.setObjectName("tab3_grid_main")

        # >> >>  tab3_vbox_0
        self.tab3_vbox_0 = QtWidgets.QVBoxLayout()
        self.tab3_vbox_0.setObjectName("tab3_vbox_0")

        # >> >> >> lab_status
        self.lab_status = QtWidgets.QLabel(self.tab_3) 
        self.lab_status.setFont(self.font_0)
        self.lab_status.setObjectName("lab_status")
        self.lab_status.setText("No errors so far :D")

        self.tab3_vbox_0.addWidget(self.lab_status)                        
        # << << << lab_status

        # >> >> >> lab_log
        self.lab_errMsg = QtWidgets.QLabel(self.tab_3) 
        self.lab_errMsg.setFont(self.font_1)
        self.lab_errMsg.setObjectName("lab_errMsg")
        self.lab_errMsg.setText("")

        self.tab3_vbox_0.addWidget(self.lab_errMsg)
        # << << << lab_log

        self.tab3_grid_main.addLayout(self.tab3_vbox_0, 2, 0, 1, 1)
        # << << tab3_vbox_0


        # Err Tab <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def handleErrors(self, target, subject, args = []):

        if subject == "syntaxError": 
            errMsg = "We have detected a syntax error in the element [" + str(args[0]) + \
            ", " + str(args[1]) + "] of the\nInput Matrix (first tab).\n" \
            "Remember to use proper python syntax!\n\n" \
            "If you need further help or you think you have found a bug,\n please sumbit the issue " \
            "to the devs on GITHUB_LINK."
            
            target.setText("error! (see the logs)")
            self.lab_status.setText("Syntax error!")
            self.lab_errMsg.setText(errMsg)


        elif subject == "matrixNonInv":
            errMsg = "The matrix that you entered has det == 0, and therefore is not\n" \
            "invertible. If you are trying to input a 3x3 matrix, leave the *last* dimension\n" \
            "empty. In case you're just trying to have fun with this,\n" \
            "I'd like to remind you that find the inverse of a 4x4 matrix is not easy,\n" \
            "even for me."

            target.setText("error! (see the logs)")
            self.lab_status.setText("Math error!")
            self.lab_errMsg.setText(errMsg)

        elif subject == "dimMismatch":
            errMsg = "You have entered a number of variables that does not match the\n" \
            "dimension of your metric. Please fix this :)"

            target.setText("error! (see the logs)")
            self.lab_status.setText("Silly error!")
            self.lab_errMsg.setText(errMsg)

        elif subject == "unknownVar":
            errMsg = "The variable \"" + args[0] + "\" that you have entered hasn't been declared\n" \
            "anywhere. Please either fix the typo or declare it in the first tab."

            target.setText("error! (see the logs)")
            self.lab_status.setText("Just fix it")
            self.lab_errMsg.setText(errMsg)

    def calculate(self):

        ds = [self.ds1.text(), self.ds2.text(), self.ds3.text(), self.ds4.text()]
        g_mn = [[self.m00.text(), self.m01.text(), self.m02.text(), self.m03.text()], \
                [self.m10.text(), self.m11.text(), self.m12.text(), self.m13.text()], \
                [self.m20.text(), self.m21.text(), self.m22.text(), self.m23.text()], \
                [self.m30.text(), self.m31.text(), self.m32.text(), self.m33.text()], \
                ]
        abc = [self.cha.text(), self.chb.text(), self.chc.text()]
        result = christoffel(ds, g_mn, abc)

        if result[0] == "syntaxError": 
            self.handleErrors(self.sol, "syntaxError", [result[1], result[2]])
        elif result[0] == "matrixNonInv":
            self.handleErrors(self.sol, "matrixNonInv")
        elif result[0] == "dimMismatch":
            self.handleErrors(self.sol, "dimMismatch")
        elif result[0] == "unknownVar":
            self.handleErrors(self.sol, "unknownVar", [result[1]])
        else:
            self.sol.setText(str(result[0]))
            self.lab_status.setText("No errors so far!")
            errMsg = "If you are reading this while getting actual errors, please\n"\
            "sumbit an issue to the devs on GITHUB_LINK, so they can fix it.\n"\
            "(or do it yourself and open a Pull Request on GitHub)"
            self.lab_errMsg.setText(errMsg)
    
    def riemmanCalc(self):

        ds = [self.ds1.text(), self.ds2.text(), self.ds3.text(), self.ds4.text()]
        g_mn = [[self.m00.text(), self.m01.text(), self.m02.text(), self.m03.text()], \
                [self.m10.text(), self.m11.text(), self.m12.text(), self.m13.text()], \
                [self.m20.text(), self.m21.text(), self.m22.text(), self.m23.text()], \
                [self.m30.text(), self.m31.text(), self.m32.text(), self.m33.text()], \
                ]
        abcd = [self.ra.text(), self.rb.text(), self.rc.text(), self.rd.text()]
        result = riemman(ds, g_mn, abcd)

        if result[0] == "syntaxError": 
            self.handleErrors(self.label_10, "syntaxError", [result[1], result[2]])
        elif result[0] == "matrixNonInv":
            self.handleErrors(self.label_10, "matrixNonInv")
        elif result[0] == "dimMismatch":
            self.handleErrors(self.label_10, "dimMismatch")
        elif result[0] == "unknownVar":
            self.handleErrors(self.label_10, "unknownVar", result[1])
        else:
            self.label_10.setText(str(result[0]))
            self.lab_status.setText("No errors so far!")
            errMsg = "If you are reading this while getting actual errors, please\n"\
            "sumbit an issue to the devs on GITHUB_LINK, so they can fix it.\n"\
            "(or do it yourself and open a Pull Request on GitHub)"
            self.lab_errMsg.setText(errMsg)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())



