# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets
from tables import Arm_table
from useful import Log_browser, Stream


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, width, height, parent=None):
        super().__init__(parent=parent)
        self.width = width
        self.height = height
        self.parent = parent

    def setupUi(self, MainWindow):
        self.arm_table = Arm_table(self.width, self.height, self.parent)
        self.arm_table.setup()

        self.log_browser = Log_browser(self.width, self.height, self.parent)
        self.log_browser.setup()

        self.claw_controls_label = QtWidgets.QLabel(self.parent)
        self.claw_controls_label.setGeometry(
            QtCore.QRect(self.width / 14.77, self.height * 0.75,
                         self.width / 19.2, self.height / 60))
        self.claw_controls_label.setObjectName("claw_controls_label")
        self.arm_controls_label = QtWidgets.QLabel(self.parent)
        self.arm_controls_label.setGeometry(
            QtCore.QRect(self.width / 4.8, 0.75 * self.height,
                         self.width / 19.2, self.height / 60))
        self.arm_controls_label.setObjectName("arm_controls_label")
        self.command_listener_button = QtWidgets.QCheckBox(self.parent)
        self.command_listener_button.setGeometry(
            QtCore.QRect(self.width / 21.33, self.height / 2.4,
                         self.width / 12, self.height / 54))
        self.command_listener_button.setObjectName("command_listener_button")
        self.manual_controls_button = QtWidgets.QCheckBox(self.parent)
        self.manual_controls_button.setGeometry(
            QtCore.QRect(self.width / 5.5, self.height / 2.4,
                         self.width / 13.71, self.height / 54))
        self.manual_controls_button.setObjectName("manual_controls_button")
        self.arm_controls_widget = QtWidgets.QWidget(self.parent)
        self.arm_controls_widget.setGeometry(
            QtCore.QRect(self.width / 5.65, self.height / 2, self.width / 8,
                         self.height / 4.5))
        self.arm_controls_widget.setObjectName("arm_controls_widget")
        self.arm_down_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_down_button.setGeometry(
            QtCore.QRect(self.width / 24, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.arm_down_button.setObjectName("arm_down_button")
        self.arm_left_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_left_button.setGeometry(
            QtCore.QRect(0, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.arm_left_button.setObjectName("arm_left_button")
        self.arm_right_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_right_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.arm_right_button.setObjectName("arm_right_button")
        self.arm_up_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_up_button.setGeometry(
            QtCore.QRect(self.width / 24, 0, self.width / 24,
                         self.height / 13.5))
        self.arm_up_button.setObjectName("arm_up_button")
        self.arm_fwd_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_fwd_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 6.75, self.width / 24,
                         self.height / 13.5))
        self.arm_fwd_button.setObjectName("arm_fwd_button")
        self.arm_back_button = QtWidgets.QPushButton(self.arm_controls_widget)
        self.arm_back_button.setGeometry(
            QtCore.QRect(0, self.height / 6.75, self.width / 24,
                         self.height / 13.5))
        self.arm_back_button.setObjectName("arm_back_button")
        self.claw_controls_widget = QtWidgets.QWidget(self.parent)
        self.claw_controls_widget.setGeometry(
            QtCore.QRect(self.width / 32, self.height / 2, self.width / 8,
                         self.height / 4.5))
        self.claw_controls_widget.setObjectName("claw_controls_widget")
        self.claw_open_button = QtWidgets.QPushButton(
            self.claw_controls_widget)
        self.claw_open_button.setGeometry(
            QtCore.QRect(0, self.height / 6.75, self.width / 24,
                         self.height / 13.5))
        self.claw_open_button.setObjectName("claw_open_button")
        self.roll_left_button_2 = QtWidgets.QPushButton(
            self.claw_controls_widget)
        self.roll_left_button_2.setGeometry(
            QtCore.QRect(0, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.roll_left_button_2.setObjectName("roll_left_button_2")
        self.roll_left_button = QtWidgets.QPushButton(
            self.claw_controls_widget)
        self.roll_left_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.roll_left_button.setObjectName("roll_left_button")
        self.pitch_down_button = QtWidgets.QPushButton(
            self.claw_controls_widget)
        self.pitch_down_button.setGeometry(
            QtCore.QRect(self.width / 24, self.height / 13.5, self.width / 24,
                         self.height / 13.5))
        self.pitch_down_button.setObjectName("pitch_down_button")
        self.claw_close_button = QtWidgets.QPushButton(
            self.claw_controls_widget)
        self.claw_close_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 6.75, self.width / 24,
                         self.height / 13.5))
        self.claw_close_button.setObjectName("claw_close_button")
        self.pitch_up_button = QtWidgets.QPushButton(self.claw_controls_widget)
        self.pitch_up_button.setGeometry(
            QtCore.QRect(self.width / 24, 0, self.width / 24,
                         self.height / 13.5))
        self.pitch_up_button.setObjectName("pitch_up_button")
        self.manual_claw_controls = QtWidgets.QWidget(self.parent)
        self.manual_claw_controls.setGeometry(
            QtCore.QRect(self.width / 32, self.height / 1.93, self.width / 8,
                         self.height / 5.4))
        self.manual_claw_controls.setObjectName("manual_claw_controls")
        self.m3_elbow_down_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m3_elbow_down_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m3_elbow_down_button.setObjectName("m3_elbow_down_button")
        self.m2_shoulder_up_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m2_shoulder_up_button.setGeometry(
            QtCore.QRect(self.width / 24, 0, self.width / 24,
                         self.height / 10.8))
        self.m2_shoulder_up_button.setObjectName("m2_shoulder_up_button")
        self.m2_shoulder_down_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m2_shoulder_down_button.setGeometry(
            QtCore.QRect(self.width / 24, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m2_shoulder_down_button.setObjectName("m2_shoulder_down_button")
        self.m1_shoulder_left_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m1_shoulder_left_button.setGeometry(
            QtCore.QRect(0, 0, self.width / 24, self.height / 10.8))
        self.m1_shoulder_left_button.setObjectName("m1_shoulder_left_button")
        self.m1_shoulder_right_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m1_shoulder_right_button.setGeometry(
            QtCore.QRect(0, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m1_shoulder_right_button.setObjectName("m1_shoulder_right_button")
        self.m3_elbow_up_button = QtWidgets.QPushButton(
            self.manual_claw_controls)
        self.m3_elbow_up_button.setGeometry(
            QtCore.QRect(self.width / 12, 0, self.width / 24,
                         self.height / 10.8))
        self.m3_elbow_up_button.setObjectName("m3_elbow_up_button")
        self.manual_arm_controls = QtWidgets.QWidget(self.parent)
        self.manual_arm_controls.setGeometry(
            QtCore.QRect(self.width / 5.65, self.height / 1.93, self.width / 8,
                         self.height / 5.4))
        self.manual_arm_controls.setObjectName("manual_arm_controls")
        self.m6_claw_open_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m6_claw_open_button.setGeometry(
            QtCore.QRect(self.width / 12, 0, self.width / 24,
                         self.height / 10.8))
        self.m6_claw_open_button.setObjectName("m6_claw_open_button")
        self.m4_wrist_down_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m4_wrist_down_button.setGeometry(
            QtCore.QRect(0, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m4_wrist_down_button.setObjectName("m4_wrist_down_button")
        self.m6_claw_close_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m6_claw_close_button.setGeometry(
            QtCore.QRect(self.width / 12, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m6_claw_close_button.setObjectName("m6_claw_close_button")
        self.m4_wrist_up_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m4_wrist_up_button.setGeometry(
            QtCore.QRect(0, 0, self.width / 24, self.height / 10.8))
        self.m4_wrist_up_button.setObjectName("m4_wrist_up_button")
        self.m5_wrist_in_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m5_wrist_in_button.setGeometry(
            QtCore.QRect(self.width / 24, self.height / 10.8, self.width / 24,
                         self.height / 10.8))
        self.m5_wrist_in_button.setObjectName("m5_wrist_in_button")
        self.m5_wrist_out_button = QtWidgets.QPushButton(
            self.manual_arm_controls)
        self.m5_wrist_out_button.setGeometry(
            QtCore.QRect(self.width / 24, 0, self.width / 24,
                         self.height / 10.8))
        self.m5_wrist_out_button.setObjectName("m5_wrist_out_button")
        self.list_commands_button = QtWidgets.QPushButton(self.parent)
        self.list_commands_button.setGeometry(
            QtCore.QRect(self.width / 1.43, self.height / 1.86,
                         self.width / 12, self.height / 15.43))
        self.list_commands_button.setObjectName("list_commands_button")
        self.homing_button = QtWidgets.QPushButton(self.parent)
        self.homing_button.setGeometry(
            QtCore.QRect(self.width / 1.43, self.height / 1.46,
                         self.width / 12, self.height / 15.43))
        self.homing_button.setObjectName("homing_button")
        self.send_speed_multiplier_button = QtWidgets.QPushButton(self.parent)
        self.send_speed_multiplier_button.setGeometry(
            QtCore.QRect(4.75 * self.width / 6, self.height / 1.64,
                         self.width / 12, self.height / 15.43))
        self.send_speed_multiplier_button.setObjectName(
            "send_speed_multiplier_button")
        self.reset_angles_button = QtWidgets.QPushButton(self.parent)
        self.reset_angles_button.setGeometry(
            QtCore.QRect(4.75 * self.width / 6, self.height / 1.86,
                         self.width / 12, self.height / 15.43))
        self.reset_angles_button.setObjectName("reset_angles_button")
        self.stop_button = QtWidgets.QPushButton(self.parent)
        self.stop_button.setGeometry(
            QtCore.QRect(self.width / 1.43, self.height / 1.64,
                         self.width / 12, self.height / 15.43))
        self.stop_button.setObjectName("stop_button")
        self.speed_multiplier_input = QtWidgets.QDoubleSpinBox(self.parent)
        self.speed_multiplier_input.setGeometry(
            QtCore.QRect(5.3 * self.width / 6, self.height / 1.6,
                         self.width / 32, self.height / 27))
        self.stream_screen = Stream(self.width, self.height, self.parent)
        self.stream_screen.setup()
        self.speed_multiplier_input.setDecimals(1)
        self.speed_multiplier_input.setMaximum(5.0)
        self.speed_multiplier_input.setSingleStep(0.5)
        self.speed_multiplier_input.setProperty("value", 1.0)
        self.speed_multiplier_input.setObjectName("speed_multiplier_input")
        self.claw_controls_widget.raise_()
        self.arm_controls_widget.raise_()
        self.claw_controls_label.raise_()
        self.arm_controls_label.raise_()
        self.command_listener_button.raise_()
        self.manual_controls_button.raise_()
        self.manual_claw_controls.raise_()
        self.manual_arm_controls.raise_()
        self.list_commands_button.raise_()
        self.homing_button.raise_()
        self.send_speed_multiplier_button.raise_()
        self.reset_angles_button.raise_()
        self.stop_button.raise_()
        self.speed_multiplier_input.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.claw_controls_label.setText(
            _translate("MainWindow", "Claw Controls"))
        self.arm_controls_label.setText(
            _translate("MainWindow", "Arm Controls"))
        self.command_listener_button.setText(
            _translate("MainWindow", "Command Listener"))
        self.manual_controls_button.setText(
            _translate("MainWindow", "Manual Controls"))
        self.arm_down_button.setText(_translate("MainWindow", "Arm\n" "Down"))
        self.arm_left_button.setText(_translate("MainWindow", "Arm\n" "Left"))
        self.arm_right_button.setText(_translate("MainWindow", "Arm\n"
                                                 "Right"))
        self.arm_up_button.setText(_translate("MainWindow", "Arm\n" "Up"))
        self.arm_fwd_button.setText(_translate("MainWindow", "Arm\n" "Fwd"))
        self.arm_back_button.setText(_translate("MainWindow", "Arm\n" "Back"))
        self.claw_open_button.setText(_translate("MainWindow", "Claw\n"
                                                 "Open"))
        self.roll_left_button_2.setText(
            _translate("MainWindow", "Roll\n"
                       "Left"))
        self.roll_left_button.setText(
            _translate("MainWindow", "Roll\n"
                       "Right"))
        self.pitch_down_button.setText(
            _translate("MainWindow", "Pitch\n"
                       "Down"))
        self.claw_close_button.setText(
            _translate("MainWindow", "Claw\n"
                       "Close"))
        self.pitch_up_button.setText(_translate("MainWindow", "Pitch\n" "Up"))
        self.m3_elbow_down_button.setText(
            _translate("MainWindow", "Down\n"
                       "F"))
        self.m2_shoulder_up_button.setText(_translate("MainWindow", "Up\n"
                                                      "E"))
        self.m2_shoulder_down_button.setText(
            _translate("MainWindow", "Down\n"
                       "D"))
        self.m1_shoulder_left_button.setText(
            _translate("MainWindow", "Left\n"
                       "W"))
        self.m1_shoulder_right_button.setText(
            _translate("MainWindow", "Right\n"
                       "S"))
        self.m3_elbow_up_button.setText(_translate("MainWindow", "Up\n" "R"))
        self.m6_claw_open_button.setText(_translate("MainWindow", "Open\n"
                                                    "U"))
        self.m4_wrist_down_button.setText(
            _translate("MainWindow", "Down\n"
                       "G"))
        self.m6_claw_close_button.setText(
            _translate("MainWindow", "Close\n"
                       "J"))
        self.m4_wrist_up_button.setText(_translate("MainWindow", "Up\n" "T"))
        self.m5_wrist_in_button.setText(_translate("MainWindow", "In\n" "H"))
        self.m5_wrist_out_button.setText(_translate("MainWindow", "Out\n" "Y"))
        self.list_commands_button.setText(
            _translate("MainWindow", "List Commands (L)"))
        self.homing_button.setText(_translate("MainWindow", "Homing"))
        self.send_speed_multiplier_button.setText(
            _translate("MainWindow", "Send Speed\n"
                       "Multiplier"))
        self.reset_angles_button.setText(
            _translate("MainWindow", "Reset Angles (O)"))
        self.stop_button.setText(_translate("MainWindow", "STOP (Q)"))
