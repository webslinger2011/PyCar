import curses
import RPi.GPIO as GPIO
import time
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
                GPIO.output(19,True)
                print "UP" 
                #print ("\n")
                time.sleep(0.05)
                GPIO.output(19,False)
            elif char == curses.KEY_DOWN:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                GPIO.output(19,True)
                print "DOWN"
                time.sleep(0.05)
                GPIO.output(19,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                GPIO.output(19,True)
                print "RIGHT"
                time.sleep(0.05)
                GPIO.output(19,False)
            elif char == curses.KEY_LEFT:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                GPIO.output(19,True)
                print "LEFT"
                time.sleep(0.05)
                GPIO.output(19,False)
            elif char == 10:
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(19,False)
                print "STOP"
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
