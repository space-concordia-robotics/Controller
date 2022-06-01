from ui.arm_ui import Arm_Ui
from useful import emergency_stop, ping_odroid, ping_mcu
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence


class Arm(Arm_Ui):

    def __init__(self, width: float, height: float, parent=None):
        super().__init__(width=width, height=height, parent=parent)
        self.speed_multiplier = 1
        self.currents = (0, 0, 0, 0, 0, 0)
        self.commands = {
            'ctrl-p': "ping arm mcu",
            'alt-p': "ping odroid",
            'q': "emergency stop all motors",
            'o': "reset memorized angle values",
            'l': "view key commands",
            "Keys 'w' to 'u'": "move motors 1-6 forwards",
            "Keys 's' to 'j'": "move motors 1-6 backwards"
        }

    def list_commands(self):
        """This method appends this program's keyboard shortcuts
        to the UI's text browser """

        for command in self.commands:
            self.log_browser.append_to_browser(
                f"'{command}': '{self.commands[command]}'")
        self.log_browser.append_to_browser("\n")

    def display_currents(self, data):
        print(data)
        self.currents = tuple(data.effort)
        self.arm_table.display_currents(self.currents)

    def homing(self):
        print("homing")

    def reset_angles(self):
        print("reset angles")

    def send_speed_multiplier(self):
        self.speed_multiplier = self.speed_multiplier_input.value()

    def switch_controls(self):
        """Switches betwee manual controls (keyboard) and regular controls (mouse)"""

        if self.manual_controls_button.isChecked():
            self.manual_arm_controls.show()
            self.manual_claw_controls.show()
            self.arm_controls_widget.hide()
            self.claw_controls_widget.hide()
        else:
            self.manual_arm_controls.hide()
            self.manual_claw_controls.hide()
            self.arm_controls_widget.show()
            self.claw_controls_widget.show()

    def start_handling_clicks(self):
        """This method is for grouping all button click methods for 
        the Rover Arm Page"""

        self.switch_controls()
        self.manual_controls_button.toggled.connect(self.switch_controls)

        self.list_commands_button.clicked.connect(self.list_commands)
        self.stop_button.clicked.connect(lambda: emergency_stop("arm"))
        self.reset_angles_button.clicked.connect(self.reset_angles)
        self.homing_button.clicked.connect(self.homing)
        self.send_speed_multiplier_button.clicked.connect(
            self.send_speed_multiplier)

        self.ping_odroid_sequence = QShortcut(QKeySequence("Alt+P"), self)
        self.ping_odroid_sequence.activated.connect(lambda: ping_odroid("arm"))
        self.ping_mcu_sequence = QShortcut(QKeySequence("Ctrl+P"), self)
        self.ping_mcu_sequence.activated.connect(lambda: ping_mcu("arm"))
        self.emergency_stop_sequence = QShortcut(QKeySequence("Q"), self)
        self.emergency_stop_sequence.activated.connect(
            lambda: emergency_stop("arm"))

        self.return_sequence = QShortcut(QKeySequence("Return"), self)
        self.return_sequence.activated.connect(self.log_browser.run_command)

        self.list_commands_sequence = QShortcut(QKeySequence("L"), self)
        self.list_commands_sequence.activated.connect(self.list_commands)

        self.reset_angles_sequence = QShortcut(QKeySequence("O"), self)
        self.reset_angles_sequence.activated.connect(self.reset_angles)