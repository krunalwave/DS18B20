# DS18B20

Temperature Data From DS18B20 Sensors

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)


## Users having Rasbian with updated Linux kernel 3.18  need to edit boot config file to work with one wire sensors.
In terminal edit config file
    #sudo nano /boot/config.txt
And add,
  dtoverlay=w1-gpio,gpiopin=4
And save (Ctrl+X)
## Reading temperature using Terminal

## The one wire communication device kernel modules can be loaded by typing,
  sudo modprobe w1-gpio
  sudo modprobe w1-therm

## Point to the address of the temperature sensor,
  cd /sys/bus/w1/devices/28*

## Note: If more than one device is connected use cd /sys/bus/w1/devices/ and ls to list all the devices and cd address where address is the unique address of the device required. For eg.cd 28-00042d8165ff

## Display temperature,
  cat w1_slave
