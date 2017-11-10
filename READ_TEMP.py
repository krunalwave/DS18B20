#------------------ Reading Temperature Data from DS18B20 --------------------------#
#
# Users having Rasbian with updated Linux kernel 3.18  need to edit boot config file to work with one wire sensors.
# In terminal edit config file,
#   sudo nano /boot/config.txt
# And add,
#   dtoverlay=w1-gpio,gpiopin=4
# And save (Ctrl+X)
# Reading temperature using Terminal
#
# The one wire communication device kernel modules can be loaded by typing,
#   sudo modprobe w1-gpio
#   sudo modprobe w1-therm
#
# Point to the address of the temperature sensor,
#   cd /sys/bus/w1/devices/28*
#
# Note: If more than one device is connected use cd /sys/bus/w1/devices/ and ls to list all the devices and cd address where address is the unique address of the device required. For eg.cd 28-00042d8165ff
#
# Display temperature,
#   cat w1_slave
#
#--------------------------------------------------------------------------------------#

import os                                                  # import os module
import glob                                                # import glob module
import time                                                # import time module
# load one wire communication device kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'                          # point to the address
# find device with address starting from 28*
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'                  # store the details


def read_temp_raw():
    f = open(device_file, 'r')
    # read the device details
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':                   # ignore first line
        time.sleep(0.2)
        lines = read_temp_raw()
    # find temperature in the details
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        # convert to Celsius
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0                   # convert to Fahrenheit
        return temp_c, temp_f


while True:
    print(read_temp())                                      # Print temperature
    time.sleep(1)
