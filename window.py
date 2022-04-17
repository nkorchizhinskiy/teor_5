from msilib.schema import Font
from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QTableView, \
                            QLabel
from PyQt5.QtGui import QFont                            

class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.resize(600, 300)
        self.setWindowTitle('Распределение инвестиций')
        self.label_font = QFont('Times New Roman', 12)
        
        self.create_table()
        
    def create_table(self):
        def resize_cells(table_name: object):
            for row in range(5):
                self.table.setRowHeight(row, 28)
            for column in range(3):
                self.table.setColumnWidth(column, 70)
        self.table = QTableWidget(self)
        self.table.move(70, 50)
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        resize_cells(self.table)
        self.table.setHorizontalHeaderLabels(['F1(xi)', 'F2(xi)', 'F3(xi)'])
        self.table.setVerticalHeaderLabels(['20', '40', '60', '80', '100'])
        self.table.setFont(self.label_font)
        
