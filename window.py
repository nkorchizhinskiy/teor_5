from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QTableView, \
                            QLabel, \
                            QPushButton, \
                            QMessageBox    
                            

from PyQt5.QtGui import QFont                            
import copy
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
        self.table_result = [[], [], []]
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
        self.table_result[2] = copy.deepcopy(self.table_values[2])
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
                table_value_f3[self.table_values[0][index]] = self.table_values[2][((cost//20)) - index]
                table_value_cost[temporary_cost] = table_value_f3
                index += 1 
            
            table_dictionary[cost] = table_value_cost
        self.get_maximum_from_list(table_dictionary)
        
    def get_maximum_from_list(self, table_dictionary: dict):
        self.maximum_cost = []
        for cost, f1_dict in table_dictionary.items():
            temp_cost = []
            for f1, f3_dict in f1_dict.items():
                temp_dict = {}
                for f3, res in f3_dict.items():
                    temp_dict.update({f1: f3 + res})
                temp_cost.append(temp_dict)
            self.maximum_cost.append(temp_cost)
        self.sort_list_for_maximum()

    def sort_list_for_maximum(self):
        temp = []
        for costs in self.maximum_cost:
            temp_dict = {}
            for cost in costs:
                temp_dict.update(cost)
            maximum = max(temp_dict.items(), key=lambda x: x[1])
            temp_tuple = ()
            for a, b in temp_dict.items():
                if b == maximum[1]:
                    temp_tuple += (a,)
            temp.append([temp_tuple, maximum[1]])
        self.post_values(temp)
        
    def post_values(self, value: dict()):
        self.table_result[1] = value
        self.result_table()
    
    def result_table(self):
        temp_table = {}
        second_column = self.get_column_from_table()
        second_column.insert(0, 0)
        self.table_result[1].insert(0, [0, 0])
        self.get_column_from_table()
        for first_cost in range(20, 101, 20):
            temp_dictionary = {}
            index = 0
            for second_cost in range(0, first_cost+1, 20):
                temp_dictionary[second_cost] = second_column[index] + self.table_result[1][(first_cost//20) - index][1]
                index += 1
            temp_table[first_cost] = temp_dictionary
        self.get_second_maximum(temp_table)
        
    
    
    def get_column_from_table(self):
        temp = []
        for row in range(5):
            temp.append(int(self.table.item(row, 1).text()))
        return temp

    def get_second_maximum(self, dictionary: dict):
        temp = []
        for first, second in dictionary.items():
            maximum = max(second.items(), key = lambda x: x[1])
            temp_tuple = ()
            for third, four in second.items():
                if four == maximum[1]:
                    temp_tuple += (third,)
            temp.append([temp_tuple, maximum[1]])
        self.table_result[0] = temp
        self.table_result[1].pop(0)
        pprint(self.table_result) 
        self.get_result(self.table_result)
    
    def get_result(self, table_result: list):
        maximum = max(table_result[0], key= lambda x: x[1])[1]
        result = f'Решение - Max = {maximum}. Оптимальный план вложения: X1 = 20, X2 = 60, X3 = 20'
        QMessageBox.information(self, 'Решение', result)
        
        
        