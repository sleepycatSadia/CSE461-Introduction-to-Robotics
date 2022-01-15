"""461_proj2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
time_step = 32
max_speed = 5.28

# motor
wheel1 = robot.getDevice('wheel1')
wheel2 = robot.getDevice('wheel2')
wheel3 = robot.getDevice('wheel3')
wheel4 = robot.getDevice('wheel4')
wheel1.setPosition(float('inf'))
wheel2.setPosition(float('inf'))
wheel3.setPosition(float('inf'))
wheel4.setPosition(float('inf'))
wheel1.setVelocity(0.0)
wheel2.setVelocity(0.0)
wheel3.setVelocity(0.0)
wheel4.setVelocity(0.0)
# Ir Sensor
right_ir = robot.getDevice('ds_right')
left_ir = robot.getDevice('ds_left')
mid_ir = robot.getDevice('ds_mid')
right_ir.enable(time_step)
mid_ir.enable(time_step)
left_ir.enable(time_step)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()

    # print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val}')

    left_speed = max_speed
    right_speed = max_speed


    ir_val = 900
    # Process sensor data here.
    if left_ir_val < ir_val and right_ir_val < ir_val and mid_ir_val >= ir_val:
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Forward')
    if left_ir_val < ir_val and right_ir_val >= ir_val and mid_ir_val >= ir_val:
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(0)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(0)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Right turn')
    if left_ir_val >= ir_val and right_ir_val < ir_val and mid_ir_val >= ir_val:
        wheel1.setVelocity(0)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(0)
        wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Left turn')
    if left_ir_val >= ir_val and right_ir_val < ir_val and mid_ir_val < ir_val:
        wheel1.setVelocity(0)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(0)
        wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Left turn')
    if left_ir_val < ir_val and right_ir_val >= ir_val and mid_ir_val < ir_val:
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(0)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(0)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Right Turn')
    if left_ir_val < ir_val and right_ir_val < ir_val and mid_ir_val < ir_val:
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Forward')
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
