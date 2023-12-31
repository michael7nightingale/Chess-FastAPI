from functools import partial

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChessboardWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 682)
        self.main_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(125, 125, 125, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.b5 = QtWidgets.QLabel(parent=self.frame_2)
        self.b5.mousePressEvent = partial(self.click_figure, cell=self.b5)
        self.b5.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 3, 2, 1, 1)
        self.f7 = QtWidgets.QLabel(parent=self.frame_2)
        self.f7.mousePressEvent = partial(self.click_figure, cell=self.f7)
        self.f7.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.f7.setText("")
        self.f7.setObjectName("f7")
        self.gridLayout.addWidget(self.f7, 1, 7, 1, 1)
        self.e7 = QtWidgets.QLabel(parent=self.frame_2)
        self.e7.mousePressEvent = partial(self.click_figure, cell=self.e7)
        self.e7.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.e7.setText("")
        self.e7.setObjectName("e7")
        self.gridLayout.addWidget(self.e7, 1, 6, 1, 1)
        self.a7 = QtWidgets.QLabel(parent=self.frame_2)
        self.a7.mousePressEvent = partial(self.click_figure, cell=self.a7)
        self.a7.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.a7.setText("")
        self.a7.setObjectName("a7")
        self.gridLayout.addWidget(self.a7, 1, 1, 1, 1)
        self.g8 = QtWidgets.QLabel(parent=self.frame_2)
        self.g8.mousePressEvent = partial(self.click_figure, cell=self.g8)
        self.g8.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.g8.setText("")
        self.g8.setObjectName("g8")
        self.gridLayout.addWidget(self.g8, 0, 8, 1, 1)
        self.g4 = QtWidgets.QLabel(parent=self.frame_2)
        self.g4.mousePressEvent = partial(self.click_figure, cell=self.g4)
        self.g4.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.g4.setText("")
        self.g4.setObjectName("g4")
        self.gridLayout.addWidget(self.g4, 4, 8, 1, 1)
        self.e4 = QtWidgets.QLabel(parent=self.frame_2)
        self.e4.mousePressEvent = partial(self.click_figure, cell=self.e4)
        self.e4.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.e4.setText("")
        self.e4.setObjectName("e4")
        self.gridLayout.addWidget(self.e4, 4, 6, 1, 1)
        self.f4 = QtWidgets.QLabel(parent=self.frame_2)
        self.f4.mousePressEvent = partial(self.click_figure, cell=self.f4)
        self.f4.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.gridLayout.addWidget(self.f4, 4, 7, 1, 1)
        self.a8 = QtWidgets.QLabel(parent=self.frame_2)
        self.a8.mousePressEvent = partial(self.click_figure, cell=self.a8)
        self.a8.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.a8.setText("")
        self.a8.setObjectName("a8")
        self.gridLayout.addWidget(self.a8, 0, 1, 1, 1)
        self.f5 = QtWidgets.QLabel(parent=self.frame_2)
        self.f5.mousePressEvent = partial(self.click_figure, cell=self.f5)
        self.f5.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.f5.setText("")
        self.f5.setObjectName("f5")
        self.gridLayout.addWidget(self.f5, 3, 7, 1, 1)
        self.g5 = QtWidgets.QLabel(parent=self.frame_2)
        self.g5.mousePressEvent = partial(self.click_figure, cell=self.g5)
        self.g5.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.g5.setText("")
        self.g5.setObjectName("g5")
        self.gridLayout.addWidget(self.g5, 3, 8, 1, 1)
        self.d4 = QtWidgets.QLabel(parent=self.frame_2)
        self.d4.mousePressEvent = partial(self.click_figure, cell=self.d4)
        self.d4.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.gridLayout.addWidget(self.d4, 4, 4, 1, 1)
        self.h4 = QtWidgets.QLabel(parent=self.frame_2)
        self.h4.mousePressEvent = partial(self.click_figure, cell=self.h4)
        self.h4.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.h4.setText("")
        self.h4.setObjectName("h4")
        self.gridLayout.addWidget(self.h4, 4, 10, 1, 1)
        self.b7 = QtWidgets.QLabel(parent=self.frame_2)
        self.b7.mousePressEvent = partial(self.click_figure, cell=self.b7)
        self.b7.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 1, 2, 1, 1)
        self.c7 = QtWidgets.QLabel(parent=self.frame_2)
        self.c7.mousePressEvent = partial(self.click_figure, cell=self.c7)
        self.c7.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.c7.setText("")
        self.c7.setObjectName("c7")
        self.gridLayout.addWidget(self.c7, 1, 3, 1, 1)
        self.a5 = QtWidgets.QLabel(parent=self.frame_2)
        self.a5.mousePressEvent = partial(self.click_figure, cell=self.a5)
        self.a5.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.a5.setText("")
        self.a5.setObjectName("a5")
        self.gridLayout.addWidget(self.a5, 3, 1, 1, 1)
        self.a6 = QtWidgets.QLabel(parent=self.frame_2)
        self.a6.mousePressEvent = partial(self.click_figure, cell=self.a6)
        self.a6.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.a6.setText("")
        self.a6.setObjectName("a6")
        self.gridLayout.addWidget(self.a6, 2, 1, 1, 1)
        self.f8 = QtWidgets.QLabel(parent=self.frame_2)
        self.f8.mousePressEvent = partial(self.click_figure, cell=self.f8)
        self.f8.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.f8.setText("")
        self.f8.setObjectName("f8")
        self.gridLayout.addWidget(self.f8, 0, 7, 1, 1)
        self.c8 = QtWidgets.QLabel(parent=self.frame_2)
        self.c8.mousePressEvent = partial(self.click_figure, cell=self.c8)
        self.c8.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.c8.setText("")
        self.c8.setObjectName("c8")
        self.gridLayout.addWidget(self.c8, 0, 3, 1, 1)
        self.b6 = QtWidgets.QLabel(parent=self.frame_2)
        self.b6.mousePressEvent = partial(self.click_figure, cell=self.b6)
        self.b6.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 2, 2, 1, 1)
        self.b8 = QtWidgets.QLabel(parent=self.frame_2)
        self.b8.mousePressEvent = partial(self.click_figure, cell=self.b8)
        self.b8.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 0, 2, 1, 1)
        self.h5 = QtWidgets.QLabel(parent=self.frame_2)
        self.h5.mousePressEvent = partial(self.click_figure, cell=self.h5)
        self.h5.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.h5.setText("")
        self.h5.setObjectName("h5")
        self.gridLayout.addWidget(self.h5, 3, 10, 1, 1)
        self.e5 = QtWidgets.QLabel(parent=self.frame_2)
        self.e5.mousePressEvent = partial(self.click_figure, cell=self.e5)
        self.e5.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.e5.setText("")
        self.e5.setObjectName("e5")
        self.gridLayout.addWidget(self.e5, 3, 6, 1, 1)
        self.d8 = QtWidgets.QLabel(parent=self.frame_2)
        self.d8.mousePressEvent = partial(self.click_figure, cell=self.d8)
        self.d8.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.d8.setText("")
        self.d8.setObjectName("d8")
        self.gridLayout.addWidget(self.d8, 0, 4, 1, 1)
        self.h8 = QtWidgets.QLabel(parent=self.frame_2)
        self.h8.mousePressEvent = partial(self.click_figure, cell=self.h8)
        self.h8.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.h8.setText("")
        self.h8.setObjectName("h8")
        self.gridLayout.addWidget(self.h8, 0, 10, 1, 1)
        self.e8 = QtWidgets.QLabel(parent=self.frame_2)
        self.e8.mousePressEvent = partial(self.click_figure, cell=self.e8)
        self.e8.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.e8.setText("")
        self.e8.setObjectName("e8")
        self.gridLayout.addWidget(self.e8, 0, 6, 1, 1)
        self.d7 = QtWidgets.QLabel(parent=self.frame_2)
        self.d7.mousePressEvent = partial(self.click_figure, cell=self.d7)
        self.d7.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.d7.setText("")
        self.d7.setObjectName("d7")
        self.gridLayout.addWidget(self.d7, 1, 4, 1, 1)
        self.g7 = QtWidgets.QLabel(parent=self.frame_2)
        self.g7.mousePressEvent = partial(self.click_figure, cell=self.g7)
        self.g7.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.g7.setText("")
        self.g7.setObjectName("g7")
        self.gridLayout.addWidget(self.g7, 1, 8, 1, 1)
        self.h7 = QtWidgets.QLabel(parent=self.frame_2)
        self.h7.mousePressEvent = partial(self.click_figure, cell=self.h7)
        self.h7.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.h7.setText("")
        self.h7.setObjectName("h7")
        self.gridLayout.addWidget(self.h7, 1, 10, 1, 1)
        self.c5 = QtWidgets.QLabel(parent=self.frame_2)
        self.c5.mousePressEvent = partial(self.click_figure, cell=self.c5)
        self.c5.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.gridLayout.addWidget(self.c5, 3, 3, 1, 1)
        self.f6 = QtWidgets.QLabel(parent=self.frame_2)
        self.f6.mousePressEvent = partial(self.click_figure, cell=self.f6)
        self.f6.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.f6.setText("")
        self.f6.setObjectName("f6")
        self.gridLayout.addWidget(self.f6, 2, 7, 1, 1)
        self.h6 = QtWidgets.QLabel(parent=self.frame_2)
        self.h6.mousePressEvent = partial(self.click_figure, cell=self.h6)
        self.h6.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.h6.setText("")
        self.h6.setObjectName("h6")
        self.gridLayout.addWidget(self.h6, 2, 10, 1, 1)
        self.c6 = QtWidgets.QLabel(parent=self.frame_2)
        self.c6.mousePressEvent = partial(self.click_figure, cell=self.c6)
        self.c6.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.c6.setText("")
        self.c6.setObjectName("c6")
        self.gridLayout.addWidget(self.c6, 2, 3, 1, 1)
        self.e6 = QtWidgets.QLabel(parent=self.frame_2)
        self.e6.mousePressEvent = partial(self.click_figure, cell=self.e6)
        self.e6.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.e6.setText("")
        self.e6.setObjectName("e6")
        self.gridLayout.addWidget(self.e6, 2, 6, 1, 1)
        self.g6 = QtWidgets.QLabel(parent=self.frame_2)
        self.g6.mousePressEvent = partial(self.click_figure, cell=self.g6)
        self.g6.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.g6.setText("")
        self.g6.setObjectName("g6")
        self.gridLayout.addWidget(self.g6, 2, 8, 1, 1)
        self.d6 = QtWidgets.QLabel(parent=self.frame_2)
        self.d6.mousePressEvent = partial(self.click_figure, cell=self.d6)
        self.d6.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.d6.setText("")
        self.d6.setObjectName("d6")
        self.gridLayout.addWidget(self.d6, 2, 4, 1, 1)
        self.a4 = QtWidgets.QLabel(parent=self.frame_2)
        self.a4.mousePressEvent = partial(self.click_figure, cell=self.a4)
        self.a4.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.gridLayout.addWidget(self.a4, 4, 1, 1, 1)
        self.c4 = QtWidgets.QLabel(parent=self.frame_2)
        self.c4.mousePressEvent = partial(self.click_figure, cell=self.c4)
        self.c4.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.gridLayout.addWidget(self.c4, 4, 3, 1, 1)
        self.d5 = QtWidgets.QLabel(parent=self.frame_2)
        self.d5.mousePressEvent = partial(self.click_figure, cell=self.d5)
        self.d5.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.d5.setText("")
        self.d5.setObjectName("d5")
        self.gridLayout.addWidget(self.d5, 3, 4, 1, 1)
        self.b3 = QtWidgets.QLabel(parent=self.frame_2)
        self.b3.mousePressEvent = partial(self.click_figure, cell=self.b3)
        self.b3.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 5, 2, 1, 1)
        self.d3 = QtWidgets.QLabel(parent=self.frame_2)
        self.d3.mousePressEvent = partial(self.click_figure, cell=self.d3)
        self.d3.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.d3.setText("")
        self.d3.setObjectName("d3")
        self.gridLayout.addWidget(self.d3, 5, 4, 1, 1)
        self.a3 = QtWidgets.QLabel(parent=self.frame_2)
        self.a3.mousePressEvent = partial(self.click_figure, cell=self.a3)
        self.a3.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.a3.setText("")
        self.a3.setObjectName("a3")
        self.gridLayout.addWidget(self.a3, 5, 1, 1, 1)
        self.c3 = QtWidgets.QLabel(parent=self.frame_2)
        self.c3.mousePressEvent = partial(self.click_figure, cell=self.c3)
        self.c3.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.c3.setText("")
        self.c3.setObjectName("c3")
        self.gridLayout.addWidget(self.c3, 5, 3, 1, 1)
        self.f3 = QtWidgets.QLabel(parent=self.frame_2)
        self.f3.mousePressEvent = partial(self.click_figure, cell=self.f3)
        self.f3.setStyleSheet("background-color: rgb(125, 125, 125); font: 12 30pt 'DejaVu Sans Light'")
        self.f3.setText("")
        self.f3.setObjectName("f3")
        self.gridLayout.addWidget(self.f3, 5, 7, 1, 1)
        self.e3 = QtWidgets.QLabel(parent=self.frame_2)
        self.e3.mousePressEvent = partial(self.click_figure, cell=self.e3)
        self.e3.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.e3.setText("")
        self.e3.setObjectName("e3")
        self.gridLayout.addWidget(self.e3, 5, 6, 1, 1)
        self.b4 = QtWidgets.QLabel(parent=self.frame_2)
        self.b4.mousePressEvent = partial(self.click_figure, cell=self.b4)
        self.b4.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 4, 2, 1, 1)
        self.a2 = QtWidgets.QLabel(parent=self.frame_2)
        self.a2.mousePressEvent = partial(self.click_figure, cell=self.a2)
        self.a2.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.a2.setText("")
        self.a2.setObjectName("a2")
        self.gridLayout.addWidget(self.a2, 6, 1, 1, 1)
        self.g3 = QtWidgets.QLabel(parent=self.frame_2)
        self.g3.mousePressEvent = partial(self.click_figure, cell=self.g3)
        self.g3.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.g3.setText("")
        self.g3.setObjectName("g3")
        self.gridLayout.addWidget(self.g3, 5, 8, 1, 1)
        self.h3 = QtWidgets.QLabel(parent=self.frame_2)
        self.h3.mousePressEvent = partial(self.click_figure, cell=self.h3)
        self.h3.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.h3.setText("")
        self.h3.setObjectName("h3")
        self.gridLayout.addWidget(self.h3, 5, 10, 1, 1)
        self.c2 = QtWidgets.QLabel(parent=self.frame_2)
        self.c2.mousePressEvent = partial(self.click_figure, cell=self.c2)
        self.c2.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.c2.setText("")
        self.c2.setObjectName("c2")
        self.gridLayout.addWidget(self.c2, 6, 3, 1, 1)
        self.b2 = QtWidgets.QLabel(parent=self.frame_2)
        self.b2.mousePressEvent = partial(self.click_figure, cell=self.b2)
        self.b2.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 6, 2, 1, 1)
        self.e2 = QtWidgets.QLabel(parent=self.frame_2)
        self.e2.mousePressEvent = partial(self.click_figure, cell=self.e2)
        self.e2.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.e2.setText("")
        self.e2.setObjectName("e2")
        self.gridLayout.addWidget(self.e2, 6, 6, 1, 1)
        self.d2 = QtWidgets.QLabel(parent=self.frame_2)
        self.d2.mousePressEvent = partial(self.click_figure, cell=self.d2)
        self.d2.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.d2.setText("")
        self.d2.setObjectName("d2")
        self.gridLayout.addWidget(self.d2, 6, 4, 1, 1)
        self.f2 = QtWidgets.QLabel(parent=self.frame_2)
        self.f2.mousePressEvent = partial(self.click_figure, cell=self.f2)
        self.f2.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.f2.setText("")
        self.f2.setObjectName("f2")
        self.gridLayout.addWidget(self.f2, 6, 7, 1, 1)
        self.h2 = QtWidgets.QLabel(parent=self.frame_2)
        self.h2.mousePressEvent = partial(self.click_figure, cell=self.h2)
        self.h2.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.h2.setText("")
        self.h2.setObjectName("h2")
        self.gridLayout.addWidget(self.h2, 6, 10, 1, 1)
        self.a1 = QtWidgets.QLabel(parent=self.frame_2)
        self.a1.mousePressEvent = partial(self.click_figure, cell=self.a1)
        self.a1.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.a1.setText("")
        self.a1.setObjectName("a1")
        self.gridLayout.addWidget(self.a1, 7, 1, 1, 1)
        self.c1 = QtWidgets.QLabel(parent=self.frame_2)
        self.c1.mousePressEvent = partial(self.click_figure, cell=self.c1)
        self.c1.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.c1.setText("")
        self.c1.setObjectName("c1")
        self.gridLayout.addWidget(self.c1, 7, 3, 1, 1)
        self.d1 = QtWidgets.QLabel(parent=self.frame_2)
        self.d1.mousePressEvent = partial(self.click_figure, cell=self.d1)
        self.d1.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.d1.setText("")
        self.d1.setObjectName("d1")
        self.gridLayout.addWidget(self.d1, 7, 4, 1, 1)
        self.g2 = QtWidgets.QLabel(parent=self.frame_2)
        self.g2.mousePressEvent = partial(self.click_figure, cell=self.g2)
        self.g2.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.g2.setText("")
        self.g2.setObjectName("g2")
        self.gridLayout.addWidget(self.g2, 6, 8, 1, 1)
        self.h1 = QtWidgets.QLabel(parent=self.frame_2)
        self.h1.mousePressEvent = partial(self.click_figure, cell=self.h1)
        self.h1.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.h1.setText("")
        self.h1.setObjectName("h1")
        self.gridLayout.addWidget(self.h1, 7, 10, 1, 1)
        self.b1 = QtWidgets.QLabel(parent=self.frame_2)
        self.b1.mousePressEvent = partial(self.click_figure, cell=self.b1)
        self.b1.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 7, 2, 1, 1)
        self.e1 = QtWidgets.QLabel(parent=self.frame_2)
        self.e1.mousePressEvent = partial(self.click_figure, cell=self.e1)
        self.e1.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.e1.setText("")
        self.e1.setObjectName("e1")
        self.gridLayout.addWidget(self.e1, 7, 6, 1, 1)
        self.f1 = QtWidgets.QLabel(parent=self.frame_2)
        self.f1.mousePressEvent = partial(self.click_figure, cell=self.f1)
        self.f1.setStyleSheet("background-color: rgb(125, 125, 125);font: 12 30pt 'DejaVu Sans Light'")
        self.f1.setText("")
        self.f1.setObjectName("f1")
        self.gridLayout.addWidget(self.f1, 7, 7, 1, 1)
        self.a_label = QtWidgets.QLabel(parent=self.frame_2)
        self.a_label.mousePressEvent = partial(self.click_figure, cell=self.a_label)
        self.a_label.setStyleSheet("")
        self.a_label.setObjectName("a_label")
        self.gridLayout.addWidget(self.a_label, 8, 1, 1, 1)
        self.g1 = QtWidgets.QLabel(parent=self.frame_2)
        self.g1.mousePressEvent = partial(self.click_figure, cell=self.g1)
        self.g1.setStyleSheet("background-color: rgb(255, 255, 255);font: 12 30pt 'DejaVu Sans Light'")
        self.g1.setText("")
        self.g1.setObjectName("g1")
        self.gridLayout.addWidget(self.g1, 7, 8, 1, 1)
        self.c_label = QtWidgets.QLabel(parent=self.frame_2)
        self.c_label.mousePressEvent = partial(self.click_figure, cell=self.c_label)
        self.c_label.setStyleSheet("")
        self.c_label.setObjectName("c_label")
        self.gridLayout.addWidget(self.c_label, 8, 3, 1, 1)
        self.b_label = QtWidgets.QLabel(parent=self.frame_2)
        self.b_label.mousePressEvent = partial(self.click_figure, cell=self.b_label)
        self.b_label.setStyleSheet("")
        self.b_label.setObjectName("b_label")
        self.gridLayout.addWidget(self.b_label, 8, 2, 1, 1)
        self.e_label = QtWidgets.QLabel(parent=self.frame_2)
        self.e_label.mousePressEvent = partial(self.click_figure, cell=self.e_label)
        self.e_label.setStyleSheet("")
        self.e_label.setObjectName("e_label")
        self.gridLayout.addWidget(self.e_label, 8, 6, 1, 1)
        self.f_label = QtWidgets.QLabel(parent=self.frame_2)
        self.f_label.mousePressEvent = partial(self.click_figure, cell=self.f_label)
        self.f_label.setStyleSheet("")
        self.f_label.setObjectName("f_label")
        self.gridLayout.addWidget(self.f_label, 8, 7, 1, 1)
        self.d_label = QtWidgets.QLabel(parent=self.frame_2)
        self.d_label.mousePressEvent = partial(self.click_figure, cell=self.d_label)
        self.d_label.setStyleSheet("")
        self.d_label.setObjectName("d_label")
        self.gridLayout.addWidget(self.d_label, 8, 4, 1, 1)
        self.g_label = QtWidgets.QLabel(parent=self.frame_2)
        self.g_label.mousePressEvent = partial(self.click_figure, cell=self.g_label)
        self.g_label.setStyleSheet("")
        self.g_label.setObjectName("g_label")
        self.gridLayout.addWidget(self.g_label, 8, 8, 1, 1)
        self._1_label = QtWidgets.QLabel(parent=self.frame_2)
        self._1_label.mousePressEvent = partial(self.click_figure, cell=self._1_label)
        self._1_label.setStyleSheet("")
        self._1_label.setObjectName("_1_label")
        self.gridLayout.addWidget(self._1_label, 7, 0, 1, 1)
        self.h_label = QtWidgets.QLabel(parent=self.frame_2)
        self.h_label.mousePressEvent = partial(self.click_figure, cell=self.h_label)
        self.h_label.setStyleSheet("")
        self.h_label.setObjectName("h_label")
        self.gridLayout.addWidget(self.h_label, 8, 10, 1, 1)
        self._3_label = QtWidgets.QLabel(parent=self.frame_2)
        self._3_label.mousePressEvent = partial(self.click_figure, cell=self._3_label)
        self._3_label.setStyleSheet("")
        self._3_label.setObjectName("_3_label")
        self.gridLayout.addWidget(self._3_label, 5, 0, 1, 1)
        self._4_label = QtWidgets.QLabel(parent=self.frame_2)
        self._4_label.mousePressEvent = partial(self.click_figure, cell=self._4_label)
        self._4_label.setStyleSheet("")
        self._4_label.setObjectName("_4_label")
        self.gridLayout.addWidget(self._4_label, 4, 0, 1, 1)
        self._2_label = QtWidgets.QLabel(parent=self.frame_2)
        self._2_label.mousePressEvent = partial(self.click_figure, cell=self._2_label)
        self._2_label.setStyleSheet("")
        self._2_label.setObjectName("_2_label")
        self.gridLayout.addWidget(self._2_label, 6, 0, 1, 1)
        self._5_label = QtWidgets.QLabel(parent=self.frame_2)
        self._5_label.mousePressEvent = partial(self.click_figure, cell=self._5_label)
        self._5_label.setStyleSheet("")
        self._5_label.setObjectName("_5_label")
        self.gridLayout.addWidget(self._5_label, 3, 0, 1, 1)
        self._7_label = QtWidgets.QLabel(parent=self.frame_2)
        self._7_label.mousePressEvent = partial(self.click_figure, cell=self._7_label)
        self._7_label.setStyleSheet("")
        self._7_label.setObjectName("_7_label")
        self.gridLayout.addWidget(self._7_label, 1, 0, 1, 1)
        self._6_label = QtWidgets.QLabel(parent=self.frame_2)
        self._6_label.mousePressEvent = partial(self.click_figure, cell=self._6_label)
        self._6_label.setStyleSheet("")
        self._6_label.setObjectName("_6_label")
        self.gridLayout.addWidget(self._6_label, 2, 0, 1, 1)
        self._8_label = QtWidgets.QLabel(parent=self.frame_2)
        self._8_label.mousePressEvent = partial(self.click_figure, cell=self._8_label)
        self._8_label.setStyleSheet("")
        self._8_label.setObjectName("_8_label")
        self.gridLayout.addWidget(self._8_label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 102, 97))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.you_color_label = QtWidgets.QLabel(parent=self.frame_3)
        self.you_color_label.setGeometry(QtCore.QRect(130, 10, 102, 97))
        self.you_color_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.you_color_label.setObjectName("you_color_label")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.enemy_label = QtWidgets.QLabel(parent=self.frame_5)
        self.enemy_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.enemy_label.setObjectName("enemy_label")
        self.horizontalLayout_3.addWidget(self.enemy_label)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_6)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.move_color_label = QtWidgets.QLabel(parent=self.frame_6)
        self.move_color_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.move_color_label.setObjectName("move_color_label")
        self.horizontalLayout_2.addWidget(self.move_color_label)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.moves_list = QtWidgets.QListWidget(parent=self.frame_7)
        self.moves_list.setGeometry(QtCore.QRect(10, 20, 200, 192))
        self.moves_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.moves_list.setObjectName("moves_list")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click_figure(self, event, cell):
        return self.main_window.chessboard_window.click_figure(event, cell)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.a_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">a</span></p></body></html>"))
        self.c_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">c</span></p></body></html>"))
        self.b_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">b</span></p></body></html>"))
        self.e_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">e</span></p></body></html>"))
        self.f_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">f</span></p></body></html>"))
        self.d_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">d</span></p></body></html>"))
        self.g_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">g</span></p></body></html>"))
        self._1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">1</span></p></body></html>"))
        self.h_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">h</span></p></body></html>"))
        self._3_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">3</span></p></body></html>"))
        self._4_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">4</span></p></body></html>"))
        self._2_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">2</span></p></body></html>"))
        self._5_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">5</span></p></body></html>"))
        self._7_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">7</span></p></body></html>"))
        self._6_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">6</span></p></body></html>"))
        self._8_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">8</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Ваш цвет:"))
        self.you_color_label.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Противник:"))
        self.enemy_label.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Ход:"))
        self.move_color_label.setText(_translate("MainWindow", "..."))
