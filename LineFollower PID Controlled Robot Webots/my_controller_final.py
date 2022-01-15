"""461_proj2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


last_error=I=D=P=error=0
kp = 1.6
ki = 0
kd = 0.3

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
time_step = 32
max_speed = 6

# initializing varibale for each of the hingejoint motor
wheel1 = robot.getDevice('wheel1')
wheel2 = robot.getDevice('wheel2')
wheel3 = robot.getDevice('wheel3')
wheel4 = robot.getDevice('wheel4')
#setting initial positions of robot wheels' to infinity
wheel1.setPosition(float('inf'))
wheel2.setPosition(float('inf'))
wheel3.setPosition(float('inf'))
wheel4.setPosition(float('inf'))
#setting initial positions of robot wheels' to zero
wheel1.setVelocity(0.0)
wheel2.setVelocity(0.0)
wheel3.setVelocity(0.0)
wheel4.setVelocity(0.0)
#initializing varibale for each of the Ir Sensor
right_ir = robot.getDevice('ds_right')
left_ir = robot.getDevice('ds_left')
mid_ir = robot.getDevice('ds_mid')

#initializing timestamp for each of the Ir Sensor
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
    #if IR sensor on the line it give value >=threshold
    #             off the line give value < threshold

    # Process sensor data here.
    
    #left=off right=off mid=on the line
    #no turn needed
    #all the wheel speed set to max 
    if left_ir_val < ir_val and right_ir_val < ir_val and mid_ir_val >= ir_val:
        error=0
        #wheel1.setVelocity(left_speed)
        #wheel2.setVelocity(right_speed)
        #wheel3.setVelocity(left_speed)
        #wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Forward')
        
     #left=off right=on mid=on the line   
     #small right turn needed
     #left wheels given max speed,right given zero speed
    if left_ir_val < ir_val and right_ir_val >= ir_val and mid_ir_val >= ir_val:
        error=-1
        #wheel1.setVelocity(left_speed)
        #wheel2.setVelocity(0)
        #wheel3.setVelocity(left_speed)
        #wheel4.setVelocity(0)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Right turn')
        
    #left=on right=off mid=on the line    
    #samall left turn needed
    #left wheels given zero speed,right given max speed
    if left_ir_val >= ir_val and right_ir_val < ir_val and mid_ir_val >= ir_val:
        error=1
        #wheel1.setVelocity(0)
        #wheel2.setVelocity(right_speed)
        #wheel3.setVelocity(0)
        #wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Left turn')
   
    #left=on right=off mid=off the line
    #big left turn needed
    #left wheels given zero speed,right given max speed
    if left_ir_val >= ir_val and right_ir_val < ir_val and mid_ir_val < ir_val:
        error=2
        #wheel1.setVelocity(0)
        #wheel2.setVelocity(right_speed)
        #wheel3.setVelocity(0)
        #wheel4.setVelocity(right_speed)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Left turn')
   
   
    #left=on right=off mid=off the line
    #big right turn needed
    #left wheels given max speed,right given zero speed
    if left_ir_val < ir_val and right_ir_val >= ir_val and mid_ir_val < ir_val:
        error=-2
        #wheel1.setVelocity(left_speed)
        #wheel2.setVelocity(0)
        #wheel3.setVelocity(left_speed)
        #wheel4.setVelocity(0)
        print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Right Turn')
        
        
        
    #if left_ir_val < ir_val and right_ir_val < ir_val and mid_ir_val < ir_val:
        #wheel1.setVelocity(left_speed)
        #wheel2.setVelocity(right_speed)
        #wheel3.setVelocity(left_speed)
        #wheel4.setVelocity(right_speed)
        #print(f'left: {left_ir_val} | mid: {mid_ir_val} | right:{right_ir_val} | Forward')
    P=error
    I=error+I
    D=error-last_error
    balance = int((kp *P)+(ki*I)+(kd*D))
    last_error = error 

    left_speed=max_speed-balance
    right_speed=max_speed+balance
    
    if left_speed>max_speed :
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(0)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(0)
        print('Right Turn')
    if right_speed>max_speed:
        wheel1.setVelocity(0)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(0)
        wheel4.setVelocity(right_speed)
        print('Left Turn')
    if left_speed<0:
        wheel1.setVelocity(0)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(0)
        wheel4.setVelocity(right_speed)
        print('Left Turn')
    if right_speed<0:
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(0)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(0)
        print('Right Turn')
    if right_speed == max_speed :
        wheel1.setVelocity(left_speed)
        wheel2.setVelocity(right_speed)
        wheel3.setVelocity(left_speed)
        wheel4.setVelocity(right_speed)
        print('Forward')
     
        
    
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
