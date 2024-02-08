from sense_hat import SenseHat
import datetime, time
import colorsys

# Initialize Sense HAT
sense = SenseHat()

# Function to convert HSV to RGB using colorsys
def hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

# Function to translate one range to another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

# Main loop
while True:
    # Get the current system time
    current_time = datetime.datetime.now()
    minute = current_time.minute
    second = current_time.second
    micro = current_time.microsecond

    # Convert the minute to a hue value
    hue = (minute % 60) / 60.0

    # Include seconds as a decimal for smoother fade
    hue += (second % 60) / 60.0 / 100

    # Use microseconds for breathing effect
    val = (micro % 1000000) / 1000000.0

    # Fade down on even numbered seconds, up on odd
    if (second % 2) == 0:
        val = translate(val,0,1,0.85,0.55)
    else:
        val = translate(val,0,1,0.55,0.85)

    # Convert HSV to RGB
    red, green, blue = hsv_to_rgb(hue, 1.0, val)

    # Debug
    #print("")
    #print("Hue: {} Val: {}".format(hue,val))
    #print("R: {} G: {}, B: {}".format(red, green, blue))

    # Set LED matrix color
    sense.clear((red, green, blue))

    # Refresh 10x per second
    time.sleep(0.1)

# Note: Press Ctrl+C to exit the loop and stop the script.

