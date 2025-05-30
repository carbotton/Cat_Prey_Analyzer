import time
import RPi.GPIO as GPIO

from cascade import prey_detected
import override  

from logger import get_logger
import sys, os
sys.path.append(os.path.join(os.getcwd(), 'Cat_Prey_Analyzer'))

# match test_solenoid.py wiring:
RELAY_PIN = 17  
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

LOCKED   = GPIO.HIGH
UNLOCKED = GPIO.LOW

log = get_logger("controller")

def lock():
    GPIO.output(RELAY_PIN, LOCKED)
    print("⛔ DOOR LOCKED (prey detected)")

def unlock():
    GPIO.output(RELAY_PIN, UNLOCKED)
    print("✅ DOOR UNLOCKED")

def main():
    det = PreyDetector()
    last_state = None

    try:
        while True:
            # 1) physical override always wins
            if override.let_in_flag:
                unlock()
                time.sleep(0.5)
                continue

            # 2) vision
            has_prey = prey_detected()

            # only change if state flipped
            if has_prey != last_state:
                if has_prey:
                    lock()
                else:
                    unlock()
                last_state = has_prey

            time.sleep(1.0)  # adjust your poll rate

    except KeyboardInterrupt:
        print("Shutting down…")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
