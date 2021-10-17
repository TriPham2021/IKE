# This is a program to control the IKE with the VEX IQ Controller:
# - Left drive base: Joystick A
# - Right drive base: Joystick D
# - Waist: L up to go up and L down to go down
# - Grabbing arm: R up/down to close/open respectively


# IMPORT OBJECTS FROM LIBRARY
# ===========================

from vex import (
    Brain,
    Controller,
    Motor,
    Ports,
    BrakeType, FORWARD, REVERSE, PERCENT
)


# INITIALIZE ROBOT COMPONENTS
# ===========================

# init the Brain
brain = Brain()

# init the Controller
controller = Controller()
controller.set_deadband(3)   # if joystick position < 3%, then consider it 0%

# init the Motors
waist_motor = Motor(Ports.PORT11, True)   # reverse polarity
grabing_arm_motor = Motor(Ports.PORT5)
right_wheel_motor = Motor(Ports.PORT12, True)   # reverse polarity
left_wheel_motor = Motor(Ports.PORT1)


# FUNCTIONS
# =========

def control_drive_base():
    joystick_a_position = controller.axisA.position()
    if joystick_a_position != 0:
        left_wheel_motor.spin(FORWARD, joystick_a_position, PERCENT)
    # otherwise stop
    else:
        left_wheel_motor.stop(BrakeType.HOLD)

    joystick_d_position = controller.axisD.position()
    if joystick_d_position != 0:
        right_wheel_motor.spin(FORWARD, joystick_d_position, PERCENT)
    # otherwise stop
    else:
        right_wheel_motor.stop(BrakeType.HOLD)


def control_waist(speed=80):
    if controller.buttonLUp.pressing():
        waist_motor.spin(FORWARD, speed, PERCENT)

    elif controller.buttonLDown.pressing():
        waist_motor.spin(REVERSE, speed, PERCENT)

    else:
        waist_motor.stop(BrakeType.HOLD)


def control_grabbing_hands(speed=100):
    if controller.buttonRUp.pressing():
        grabing_arm_motor.spin(FORWARD, speed, PERCENT)

    elif controller.buttonRDown.pressing():
        grabing_arm_motor.spin(REVERSE, speed, PERCENT)

    else:
        grabing_arm_motor.stop(BrakeType.HOLD)


# MAIN PROGRAM LOOP
# =================

while True:
    control_drive_base()
    control_waist(50)
    control_grabbing_hands(80)
