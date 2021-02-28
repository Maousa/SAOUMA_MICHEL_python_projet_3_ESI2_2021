import sys
from PySide6.QtGui import *
from PySide6 import QtWidgets
import currency_converter

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseurs des devises")
        self.currency = currency_converter.CurrencyConverter()
        self.resize(320,150)
        self.interface()
        self.css()
        self.valeurs_default()
        self.connection()
        
    def interface(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
        
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    def css(self):
        self.setStyleSheet("""
           background-color: "black";
           color: "white"             
        """)
        
        self.btn_inverser.setStyleSheet("""
            background-color: "white";
            color: "black"
        """)
           
    def valeurs_default(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.currency.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.currency.currencies)))
        #mettre l'euro en default
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        #montant 
        self.spn_montant.setRange(1, 1000000000)
        self.spn_montantConverti.setRange(1, 1000000000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)

    def connection(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser)
    
    def compute(self):
        #recuperation des devises
        devise1 = self.cbb_devisesFrom.currentText()
        devise2 = self.cbb_devisesTo.currentText()
        #montants de la devise
        mnt = self.spn_montant.value()
        #conversion
        conversion = self.currency.convert(mnt,devise1,devise2)
        #mettre dans la valeur convertie
        self.spn_montantConverti.setValue(conversion)
    
    def inverser(self):
        devise1 = self.cbb_devisesFrom.currentText()
        devise2 = self.cbb_devisesTo.currentText()
        
        self.cbb_devisesFrom.setCurrentText(devise2)
        self.cbb_devisesTo.setCurrentText(devise1)
        
        self.compute()
        

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

#print("test")