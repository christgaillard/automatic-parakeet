#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main':
    
    app = QApplication(sys.argv)
    
    w = QWidget()
    w.resize(250,150)
    w.move(100,100)
    w.setWindowTitle('simple test')
    w.show()
    
    #now = QDateTime.currentDateTime()

    #print(now.toString(Qt.ISODate))
    #print(now.toString(Qt.DefaultLocaleLongDate))
    
    sys.exit(app.exec_())




