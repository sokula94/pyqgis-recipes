# -*- coding: utf-8 -*-
"""
/***************************************************************************
 plugin
                                 A QGIS plugin
 plugin
                              -------------------
        begin                : 2016-07-16
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Marta Pienkowska
        email                : martucha_p@wp.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
  def __init__(self): 	
    QDialog.__init__(self)
    self.setupUi()

  
  def setupUi(self):
    self.setFixedSize(400,400)
    self.setWindowTitle("plugin")
    self.vbox = QVBoxLayout()    	
    self.ok = QPushButton("ok")
    self.cancel = QPushButton("preview")
    self.ok.clicked.connect(self.doOk) 
    self.cancel.clicked.connect(self.doCancel) 
    self.reset = QPushButton("next")
    self.reset.clicked.connect(self.doReset) 
    self.label = QLabel("options")
    self.opt = QRadioButton("1st option")
    self.opt.clicked.connect(self.doOpt)
    self.opt2 = QRadioButton("2nd option")	
    self.opt2.clicked.connect(self.doOpt2)
    self.label2 = QLabel("indicator")
    self.indi = QCheckBox("1st indicator")
    self.indi.clicked.connect(self.doIndi)
    self.indi2 = QCheckBox("2nd indicator")
    self.indi2.clicked.connect(self.doIndi2)
    self.indi3 = QCheckBox("3rd indicator")
    self.indi3.clicked.connect(self.doIndi3)
    self.label3 = QLabel("set name")
    self.line_edit = QLineEdit()
    self.combo = QComboBox()
    self.combo.setEditable(True)
    self.label4 = QLabel("choose type")
    self.combo.addItems(".jpg .tiff .png .txt .xls".split())
    self.button = QPushButton("next type",self)
    self.button.clicked.connect(self.handleButton)
    
    self.hbox = QHBoxLayout()
    self.hbox.addStretch() 
    self.hbox.addWidget(self.cancel)
    self.hbox.addWidget(self.ok)
    self.vbox.addWidget(self.reset)
    self.vbox.addWidget(self.label)
    self.vbox.addWidget(self.opt)
    self.vbox.addWidget(self.opt2)
    self.vbox.addWidget(self.label2)
    self.vbox.addWidget(self.indi)
    self.vbox.addWidget(self.indi2)
    self.vbox.addWidget(self.indi3)
    self.vbox.addWidget(self.label3)
    self.vbox.addWidget(self.line_edit)
    self.vbox.addWidget(self.label4)
    self.vbox.addWidget(self.combo)
    self.vbox.addWidget(self.button)
    self.changeIndex()
    self.combo.activated.connect(self.handleActivated)

   
    self.changeIndex()
   
    
    self.vbox.addStretch()
    self.vbox.addLayout(self.hbox)
    self.setLayout(self.vbox)
    
  def doOk(self):
    self.close()
  def doReset(self):
    self.close()
  def doCancel(self):
    self.close()
  def doOpt(self):
    self.close()
  def doOpt2(self):
    self.close()
  def doIndi(self):
    self.close()
  def doIndi2(self):
    self.close()
  def doIndi3(self):
    self.close()
  def handleButton(self):
    self.combo.blockSignals(True)
    self.changeIndex()
    self.combo.blockSignals(False)
  def changeIndex(self):
      index = self.combo.currentIndex()
      if index < self.combo.count() - 1:
          self.combo.setCurrentIndex(index + 1)
      else:
          self.combo.setCurrentIndex(0)
  def handleActivated(self,text):
    print("handleActivated: %s" % text)
  def handleChanged(self,text):
    print("handlechanged: %s" % text)



