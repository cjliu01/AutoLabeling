from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ZoomWidget(QSpinBox):
    def __init__(self, value=100):
        super(ZoomWidget, self).__init__()
        self.setButtonSymbols(QAbstractSpinBox.NoButtons)  # 隐藏控件上的增加和减少按钮
        self.setRange(1, 500)
        self.setSuffix(" %")
        self.setValue(value)
        self.setToolTip("Zoom In/Out proportion")
        self.setStatusTip(self.toolTip())
        self.setAlignment(Qt.AlignCenter)

