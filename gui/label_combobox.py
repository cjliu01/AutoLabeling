from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox


class LabelComboBox(QWidget):
    def __init__(self, items):
        super(LabelComboBox, self).__init__()

        layout = QHBoxLayout()
        self.comboBox = QComboBox()
        self.items = items
        self.comboBox.addItems(self.items)

        layout.addWidget(self.comboBox)
        self.setLayout(layout)