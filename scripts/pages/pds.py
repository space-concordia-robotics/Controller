from ui.pds_ui import Pds_Ui
from useful import emergency_stop, ping_odroid, ping_mcu
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence


class Pds(Pds_Ui):

    def __init__(self, width: float, height: float, parent=None):
        super().__init__(width=width, height=height, parent=parent)
        self.fan1_speed = 100.0
        self.fan2_speed = 100.0
        self.commands = {
            'ctrl-p': "ping rover mcu",
            'alt-p': "ping odroid",
            'q': "cut power to all motors",
            'l': "view key commands",
            'ctrl-shift-r': "turn on / off all motors"
        }

    def list_commands(self):
        """This method appends this program's keyboard shortcuts
        to the UI's text browser """

        for command in self.commands:
            self.log_browser.append_to_browser(
                f"'{command}': '{self.commands[command]}'")
        self.log_browser.append_to_browser("\n")

    def display_currents(self, data):
        self.currents = tuple(data.effort)
        self.controller_table.display_currents(self.currents)

    def reset_general_flags(self):
        print("reset gen flags")

    def reset_current_flags(self):
        print("reset curr flags")

    def set_fan_speed(self, fan_number: int):
        if fan_number == 1:
            self.fan1_speed = self.fan1_speed_input.value()
            self.fan1_speed_input.clearFocus()
        elif fan_number == 2:
            self.fan2_speed = self.fan2_speed_input.value()
            self.fan2_speed_input.clearFocus()
        print(self.fan1_speed, self.fan2_speed)

    def toggle_motor(self, index: int, state: bool = None):
        exec(f"print(self.motor{index}.isChecked())")

    def check_on_motors(self):
        return self.motor1.isChecked() or self.motor2.isChecked(
        ) or self.motor3.isChecked() or self.motor4.isChecked(
        ) or self.motor5.isChecked() or self.motor6.isChecked()

    def toggle_all_motors(self):
        if self.check_on_motors():
            for i in range(1, 7):
                exec(f"self.motor{i}.setChecked(False)")
        else:
            for i in range(1, 7):
                exec(f"self.motor{i}.setChecked(True)")

    def handle_return(self):
        if not self.fan1_speed_input.hasFocus(
        ) and not self.fan2_speed_input.hasFocus():
            self.log_browser.run_command()

    def start_handling_clicks(self):
        """This method is for grouping all button click methods for 
        the Rover PDS Page"""

        self.list_commands_button.clicked.connect(self.list_commands)
        self.stop_button.clicked.connect(lambda: emergency_stop("pds"))
        self.reset_current_flags_button.clicked.connect(
            self.reset_current_flags)
        self.reset_general_flags_button.clicked.connect(
            self.reset_general_flags)

        self.motor1.toggled.connect(
            lambda state: self.toggle_motor(1, bool(state)))
        self.motor2.toggled.connect(
            lambda state: self.toggle_motor(2, bool(state)))
        self.motor3.toggled.connect(
            lambda state: self.toggle_motor(3, bool(state)))
        self.motor4.toggled.connect(
            lambda state: self.toggle_motor(4, bool(state)))
        self.motor5.toggled.connect(
            lambda state: self.toggle_motor(5, bool(state)))
        self.motor6.toggled.connect(
            lambda state: self.toggle_motor(6, bool(state)))

        self.fan1_speed_input.editingFinished.connect(
            lambda: self.set_fan_speed(1))
        self.fan2_speed_input.editingFinished.connect(
            lambda: self.set_fan_speed(2))

        self.ping_odroid_sequence = QShortcut(QKeySequence("Alt+P"), self)
        self.ping_odroid_sequence.activated.connect(lambda: ping_odroid("pds"))
        self.ping_mcu_sequence = QShortcut(QKeySequence("Ctrl+P"), self)
        self.ping_mcu_sequence.activated.connect(lambda: ping_mcu("pds"))
        self.emergency_stop_sequence = QShortcut(QKeySequence("Q"), self)
        self.emergency_stop_sequence.activated.connect(
            lambda: emergency_stop("pds"))

        self.return_sequence = QShortcut(QKeySequence("Return"), self)
        self.return_sequence.activated.connect(self.log_browser.run_command)

        self.list_commands_sequence = QShortcut(QKeySequence("L"), self)
        self.list_commands_sequence.activated.connect(self.list_commands)

        self.toggle_all_motors_sequence = QShortcut(
            QKeySequence("Ctrl+Shift+R"), self)
        self.toggle_all_motors_sequence.activated.connect(
            self.toggle_all_motors)
