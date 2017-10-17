#============================================================================#
#==========================General Imports===================================#
#============================================================================#

import MySQLdb                  # Imports are for DB communication,
import time                     # general time functions, threading
import threading                # capabilities, and then the precompiled
from threading import Thread    # PWMDriver library for the pretty PWM
from PWMDriver import PWM       # hat that's sat on top of the MK.I
                                # automaton. 

#============================================================================#
#========================End General Imports=================================#
#============================================================================#
#========================Servo Initialisation================================#
#============================================================================#

def ServoInit():
    global init
    
    pwm = PWM(0x40) # Initialise the PWM device using the default address
                    # Note if you'd like more debug output you can instead run:
                    #pwm = PWM(0x40, debug=True)
                    
    servoMin = 150  # Servo Minimum PWM/4096
    servoMax = 600  # Servo Maximum PWM/4096
    servoMid = 442  # Servo Midpoint PWM/4096
                    
                    #Essentially, dont change these numbers, they've been
                    #calibrated specifically for the Talos MK.I Automaton.
    
    def setServoPulse(channel, pulse):
      pulseLength = 1000000                   # 1,000,000 us(micro-seconds)
                                              # per second. This is part of
                                              # the PWM calculations,
                                              # leave it well alone.
      
      pulseLength /= 60                       # 60 Hz
      pulseLength /= 4096                     # 12 bits of resolution
      pulse *= 1000
      pulse /= pulseLength
      pwm.setPWM(channel, 0, pulse)
    pwm.setPWMFreq(60)
    varDrivex = 350 # Only relevent for this small section, just a holding 
    init = 0        # value for the PWM.
    while init < 6:
        init = init + 0.4 
        varDrivex = varDrivex + 3       
        pwm.setPWM(0, 0, varDrivex)
        time.sleep(0.1)                 # This little section is the wiggle
                                        # I give to the ESC to wake it up,
                                        # it's actually super essential.
                                        # Should take about 1.5s (NO JOKE)
                                        
#============================================================================#
#======================End Servo Initialisation==============================#
#============================================================================#
#=============================Servo Setup====================================#
#============================================================================#
                                        
def ServoSetup():
    global varSteer     # General variable setup, global so it works
    global varDrive     # between threads.
    time.sleep(0.1)     # Nap to let the threads do their thing (Linux stuff)
    
    pwm = PWM(0x40)     # Initialise the PWM device using the default address
                        # Note if you'd like more debug output you can
                        # instead run:
                        # > pwm = PWM(0x40, debug=True) <
    servoMin = 150      # Servo Minimum PWM/4096
    servoMax = 600      # Servo Maximum PWM/4096
    servoMid = 442      # Servo Midpoint PWM/4096
                        # These have to be set again because for some reason
                        # they hate global definition.
                        
    def setServoPulse(channel, pulse):  # Same code as the jolt, just this
                                        # controls the main functionality.
      pulseLength = 1000000                   
      pulseLength /= 60
      pulseLength /= 4096
      pulse *= 1000
      pulse /= pulseLength
      pwm.setPWM(channel, 0, pulse)
    pwm.setPWMFreq(60)
    varSteer = servoMid         # Put the servos and ESC in a nice starting
    varDrive = servoMid         # position, without this the automaton would
    varDrivex = varDrive        # sometimes just run off on its own into a 
    varSteerx = varSteer        # wall.
    
    while True:                 # This saucy goodness is the handler for when
        if FWD == 1:            # to stop turning/accelerating.
            if varDrivex < 450 and varDrivex > 400 or varDrivex == 0:
                varDrivex = 415                
        if BCK == 1:            # Hopefully the variable names make things
            if varDrivex < 250 and varDrivex < 320 or varDrivex == 0:
                varDrivex = 355                   
        if LFT == 1:            # self explainatory. 
            if varSteerx < 550:
                varSteerx = 550   
        if RHT == 1:
            if varSteerx > 150 or varSteerx == 0:
                varSteerx = 150
        if LFT == 0 and RHT == 0 and (FWD == 1 or BCK ==1):
            varSteerx = 380      	
        if BRAKE == 2 and LFT == 0 and RHT == 0 and FWD == 0 and BCK == 0:
            varDrivex = 0   # If no keys are being "held" then this bit resets
            varSteerx = 0   # the servos to their neutral position.
        pwm.setPWM(0, 0, varDrivex)
        pwm.setPWM(1, 0, varSteerx)
        time.sleep(0.05)    # make the loop take a nap so we don't lock up the
        print varDrivex     # Pi, that wouldn't be very good..
        print varSteerx     # Promise I didn't end up doing that..
        
#============================================================================#
#==========================End Servo Setup===================================#
#============================================================================#
#===========================Reset Handler====================================#
#============================================================================#
        
def Reset():    # When the system gets started, you don't exactly want 
    try:        # things to be left in gear..
        
        db = MySQLdb.connect("localhost","root","pi","Talos" )
        sql = """UPDATE DriveMap SET FWD = 0, BCK = 0, LFT = 0, RHT = 0"""
        
        cursor = db.cursor()    # Excellent username and password choice. 
        cursor.execute(sql)     # This is just some basic DB transaction.
        db.commit()
        print "Reset called"
    except:
        db.rollback()           # Error catching 101
        print "Error: unable to fecth data"
    db.close()
    
#============================================================================#
#==========================End Reset Hander==================================#
#============================================================================#
#===================Database Communication Handler===========================#
#============================================================================#
    
def DBFetch():
    global FWD  # This lot pretty much asks the database if anything has
    global BCK  # been pressed and then reacts accordingly. Crude, but
    global LFT  # surprisingly effective. Though, this falls to pieces
    global RHT  # if the Pi gets hung up in traffic or some other process.
    global BRAKE
    while True:
        try:
            db = MySQLdb.connect("localhost","root","pi","Talos" )
            sql = "SELECT * FROM DriveMap"
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
               FWDx = row[0]
               FWD = FWDx
               BCKx = row[1]
               BCK = BCKx
               LFTx = row[2]
               LFT = LFTx
               RHTx = row[3]
               RHT = RHTx
               BRAKEx = row[4]
               BRAKE = BRAKEx
        except:
            print "Error: unable to fecth data"
        db.close()
        time.sleep(0.05)    # Nap time to avoid obliterating the CPU. Keeps
                            # things pseudo-realtime, while sparing the CPU
                            # from being minced.
                            
#============================================================================#
#====================End Database Connection Handler=========================#
#============================================================================#
#========================Main Functional Loop================================#
#============================================================================#
#============================================================================#
                            
                                # This is the last little bit of code,
                                # Pretty much takes the upper section and
print "Setting up servos..."    # reacts accordingly.
ServoInit()
time.sleep(2)                   # Nap time to let the boot loop do
                                # its thing.
print "Fetching data..."                                
Thread(target = DBFetch).start()    # Starts up the database communication
time.sleep(0.5)                     # thread, threads are used to allow for
varDrivex = 0                       # synchonous actions.
varSteerx = 0

print "Starting servo control..."   # Start waking up the servos and get
Thread(target = ServoSetup).start() # them to start using provided data
time.sleep(0.1)                     # from the database.

print "Setup complete!"             # Whole thing is done and running,
                                    # have fun. 

#============================================================================#
#====================COPYRIGHT TECHSMART SOLUTIONS @2017=====================#
#============================================================================#
