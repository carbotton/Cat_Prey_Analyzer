# smart_cat_door-main/override.py
from gpiozero import Button

# initial override state: False = no-override
let_in_flag = False

def _toggle():
    global let_in_flag
    let_in_flag = not let_in_flag
    print("LET_IN_FLAG is now", let_in_flag)

# wire yellow button on GPIO27
toggle_btn = Button(27, pull_up=True, bounce_time=0.2)
toggle_btn.when_pressed = _toggle

#if __name__ == "__main__":
#    print("Override service started—waiting for button presses on GPIO27")
#    # Blocks forever, handling button events
#    from signal import pause
#   pause()
