# DS18B20

Temperature Data From DS18B20 Sensors

[![N|Solid](https://raw.githubusercontent.com/krunalwave/DS18B20/master/k.png)](krunalwave.github.io)


# Users having Rasbian with updated Linux kernel 3.18  need to edit boot config file to work with one wire sensors.

In terminal edit config file

```sh
$ sudo nano /boot/config.txt
```

And add,
  dtoverlay=w1-gpio,gpiopin=4
And save (Ctrl+X)

## Reading temperature using Terminal

## The one wire communication device kernel modules can be loaded by typing,

```sh
$ sudo modprobe w1-gpio
$ sudo modprobe w1-therm
```

## Point to the address of the temperature sensor,

```sh
 $ cd /sys/bus/w1/devices/28*
```

## Note: If more than one device is connected use cd /sys/bus/w1/devices/ and ls to list all the devices and cd address where address is the unique address of the device required. For eg.cd 28-00042d8165ff

## Display temperature,

```s
$ cat w1_slave
```
