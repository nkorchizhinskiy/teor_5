from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QTableView, \
                            QLabel, \
                            QPushButton
from PyQt5.QtGui import QFont                            
from pprint import pprint


class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setWindowTitle('Распределение инвестиций')
        self.label_font = QFont('Times New Roman', 12)
        self.push_button = QPushButton('Продолжить', self)
        self.push_button.move(500, 150)
        self.push_button.clicked.connect(self.get_table_values)
        self.create_table()
    
    def create_table(self) -> None:
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
     
    def get_table_values(self):
        self.table_values = []
        for column in range(3):
            temp_values_list = []
            for row in range(5):
                temp_values_list.append(int(self.table.item(row, column).text()))
            self.table_values.append(temp_values_list)
        self.table_values[0].insert(0, 0)
        self.table_values[2].insert(0, 0)
        self.write_in_table()
           
    def write_in_table(self): 
        table_dictionary = {}
        for cost in range(20, 101, 20):
            index = 0
            table_value_cost = {}
            for temporary_cost in range(0, cost+1, 20):
                table_value_f3 = {}
                print(f'{cost} - {temporary_cost} - {self.table_values[0][index]} - {self.table_values[2][((cost//20)) - index]}')
                table_value_f3[self.table_values[0][index]] = self.table_values[2][((cost//20)) - index]
                table_value_cost[temporary_cost] = table_value_f3
                index += 1 
            
            table_dictionary[cost] = table_value_cost
        pprint(table_dictionary)
        
    def get_maximum_from_list(self, ma):
        pass