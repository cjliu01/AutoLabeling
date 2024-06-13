import sys

from gui.zoomWidget import ZoomWidget
from gui.label_combobox import LabelComboBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class Window:
    def __init__(self, classes_path=None):
        super().__init__()
        self.ui = uic.loadUi('gui/mainWindow.ui')
        self.ui.setWindowTitle("AutoLabel")

        self.zoom_widget = ZoomWidget()

        self.ui.toolBarVertical.addAction(self.ui.actionZoomIn)
        self.ui.toolBarVertical.addAction(self.ui.actionZoomOut)
        self.ui.toolBarVertical.addWidget(self.zoom_widget)
        self.zoom_widget.setValue(100)
        self.ui.toolBarVertical.addSeparator()
        self.ui.toolBarVertical.addAction(self.ui.actionAdjust)
        self.ui.toolBarVertical.addSeparator()

        self.labelHint = [
            "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck",
            "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
            "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra",
            "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
            "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove",
            "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
            "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
            "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
            "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
            "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
            "toothbrush"
        ]
        if classes_path is not None:
            self.labelHint = [str(line.strip()) for line in open(classes_path).readlines()]

        self.defaultLabel = self.labelHint[0]
        self.ui.labelComboBox = LabelComboBox(items=self.labelHint)
        self.ui.labelComboBox.comboBox.currentIndexChanged.connect(self.default_label_combo_selection_change)
        self.ui.toolBarVertical.addWidget(self.ui.labelComboBox)

        self.ui.toolBarVertical.addAction(self.ui.actionAnno)
        self.ui.toolBarVertical.addAction(self.ui.actionDelete)
        self.ui.toolBarVertical.addSeparator()

        self.ui.toolBarVertical.addAction(self.ui.actionModel)
        self.ui.toolBarVertical.addAction(self.ui.actionDetection)

    def show(self):
        self.ui.show()

    def default_label_combo_selection_change(self, index):
        self.dafaultLabel = self.labelHint[index]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    app.exec()
