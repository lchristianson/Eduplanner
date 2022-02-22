
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMenuBar, QGridLayout, QPushButton




class App(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("EduPlanner v0.12")
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 650
        #menu = QMenuBar()
        #self.setMenuBar(menu)
        #menu.addMenu("File")
        #menu.addMenu("Edit")
        #menu.addMenu("Help")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QGridLayout()
        for i in range(7):
            self.layout.addItem(QPushButton, 1, i)
        self.setLayout(self.layout)

        print("done with the constructor")

    
  
if __name__ == '__main__':
    import sys
    print("initialized the application.")
    app = QApplication(sys.argv)
    print("about to make an App object")
    ex = App()
    print("after the initialization of the App")
    ex.show()
    sys.exit(app.exec_())







