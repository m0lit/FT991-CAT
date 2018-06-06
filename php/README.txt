Setup and Configuration
-----------------------
1. Download and install latest Raspian iamge from www.raspberrypi.org

2. Update the RaspberryPi to the latest version using the commands below and then reboot:
	sudo apt-get update
	sudo apt-get upgrade

3. Go into raspi-config and enable enable SSH, note down your local IP address

4. Install Apache2 and PHP using the folowing commands:
	sudo apt-get install apache2
	sudo apt-get install php

5. Install python pip and pyserial
	sudo apt-get install python-pip
	sudo apt-get install python-serial or sudo python pip pyserial

6. Make a directory under /home/pi called dev and sub folders called python and php as below:
	/home/pi/dev/python
	/home/pi/dev/php

7. Make a symbolic link to the www folder as below:
	sudo ln -s /home/pi/dev/php /var/www/html/cat

8. Modify the sudoers file, using sudo nano /etc/sudoers, to allow www to execute code, edit /etc/sudoers and at the end of the file add the following:
	www.-data ALL=NOPASSWORD :ALL

9. Copy the python script into the python folder

10. Copy the html and php code into the php folder 

11. Modify the HTML code and change the IP address to the IP address of your RaspberryPi

12. Test by opening a web page on a device like an iPad/laptop or using the RaspberryPi in a web browser:
	http://192.168.1.100/cat/index.html

