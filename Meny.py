
from PyQt5.QtWidgets import *

app = QApplication([])
mainWin = QWidget()
mainWin.setWindowTitle("Ping-pong")
mainWin.resize(600,500)

app.setStyleSheet(
    """

    QPushButton{
        color: black;
        font-family: Monotype Corsiva;
        font-size: 18px;
        border-radius: 10px;
        background: #A4B5EB;
        border-color: black;
        border-height: 3px ; 
}

"""""
)




start = QPushButton("PLAY")


LINE = QVBoxLayout()
LINE.addWidget(start)



mainWin.setLayout(LINE)
mainWin.show()
app.exec_()