import os

from mcu_control.msg._ThermistorTemps import ThermistorTemps
from mcu_control.msg._Voltage import Voltage
from PyQt5 import QtCore, QtGui, QtWidgets


class Queue(object):
    def __init__(self, queue_size: int):
        self.queue_size: int = queue_size
        self.queue: list = []

    def get_list(self) -> list:
        return self.queue

    def clear(self):
        self.queue.clear()

    def append(self, data):
        if len(self.queue) < self.queue_size:
            self.queue.append(data)
        else:
            self.queue.pop(0)
            self.queue.append(data)


# This is currently a place holder for the Stream component
class Stream(QtWidgets.QWidget):
    def __init__(self, width: float, height: float, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.width = width
        self.height = height
        self.parent = parent

    def setup(self):
        self.stream_screen = QtWidgets.QLabel(self.parent)
        self.stream_screen.setGeometry(
            QtCore.QRect(
                0.63 * self.width,
                self.height / 15,
                7 * self.width / 24,
                0.44 * self.height,
            )
        )
        self.stream_screen.setStyleSheet("background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);")
        self.stream_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.stream_screen.setObjectName("stream_screen")


class Header(QtWidgets.QWidget):
    def __init__(self, width: float, height: float, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.width = width
        self.height = height
        self.parent = parent
        self.temps = (0, 0, 0)
        self.voltage = 0

    def update_temps(self, data: ThermistorTemps):
        degree = "\N{DEGREE SIGN}"
        self.temps = tuple(str(data).split()[1::2])
        self.temp1_label.setText(f"{self.temps[0]} {degree}C")
        self.temp2_label.setText(f"{self.temps[1]} {degree}C")
        self.temp3_label.setText(f"{self.temps[2]} {degree}C")

    def update_voltage(self, data: Voltage):
        self.voltage = data.data
        self.voltage_label.setText(f"{self.voltage} V")

    def setup(self):
        sc_logo = QtWidgets.QLabel(self.parent)

        sc_logo.setGeometry(
            QtCore.QRect(
                self.width / 48,
                self.height / 90,
                self.width / 21.33,
                self.height / 21.6,
            )
        )
        sc_logo.setText(
            f'<a style="text-decoration: none" href="http://spaceconcordia.ca"><img src="{os.path.join(os.path.dirname(__file__), "../resource/sclogo_header.png")}"/></a>'
        )
        sc_logo.setOpenExternalLinks(True)
        sc_logo.setObjectName("sc_logo")

        widget = QtWidgets.QWidget(self.parent)
        widget.setGeometry(
            QtCore.QRect(
                self.width / 1.63,
                self.height / 108,
                self.width / 10.66,
                self.height / 18,
            )
        )
        widget.setObjectName("widget")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(widget)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        battery_logo = QtWidgets.QLabel(widget)
        battery_logo.setGeometry(
            QtCore.QRect(
                self.width / 48,
                self.height / 54,
                3 * self.width / 64,
                self.height / 21.6,
            )
        )
        battery_logo.setText("")
        battery_logo.setObjectName("battery_logo")
        horizontalLayout_2.addWidget(battery_logo)
        self.voltage_label = QtWidgets.QLabel(widget)
        self.voltage_label.setText("- V")
        self.voltage_label.setObjectName("voltage_label")
        horizontalLayout_2.addWidget(self.voltage_label)

        layoutWidget_2 = QtWidgets.QWidget(self.parent)
        layoutWidget_2.setGeometry(
            QtCore.QRect(
                self.width / 1.37,
                self.height / 108,
                self.width / 5.19,
                self.height / 18,
            )
        )
        layoutWidget_2.setObjectName("layoutWidget_2")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(layoutWidget_2)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        temp_logo = QtWidgets.QLabel(layoutWidget_2)
        temp_logo.setGeometry(
            QtCore.QRect(
                self.width / 48,
                self.height / 54,
                3 * self.width / 64,
                self.height / 21.6,
            )
        )
        temp_logo.setText("")
        temp_logo.setObjectName("temp_logo")
        horizontalLayout_3.addWidget(temp_logo)
        self.temp1_label = QtWidgets.QLabel(layoutWidget_2)
        degree = "\N{DEGREE SIGN}"  # degree sign code
        self.temp1_label.setText(f"- {degree}C")
        self.temp1_label.setObjectName("temp1_label")
        horizontalLayout_3.addWidget(self.temp1_label)
        self.temp2_label = QtWidgets.QLabel(layoutWidget_2)
        self.temp2_label.setText(f"- {degree}C")
        self.temp2_label.setObjectName("temp2_label")
        horizontalLayout_3.addWidget(self.temp2_label)
        self.temp3_label = QtWidgets.QLabel(layoutWidget_2)
        self.temp3_label.setText(f"- {degree}C")
        self.temp3_label.setObjectName("temp3_label")
        horizontalLayout_3.addWidget(self.temp3_label)

        temp_logo.setPixmap(
            QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "../resource/therm_icon.png"))
        )
        battery_logo.setPixmap(
            QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "../resource/battery_icon.png"))
        )
