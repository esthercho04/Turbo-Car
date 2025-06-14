import serial.tools.list_ports

#https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports

#list all available ports

#comports() list all the ports/USB connected to computer
ports=serial.tools.list_ports.comports()

#ports already defined list of connected devices.
for port in ports{
    print(f"Ports:{port.description}")
}

#example of output Name: COM 3 Description: Arduino


#write an if statement if this port is available run robot.py