# Simple LED Project

This project has a simple Arduino sketch that read data from UART communication protocol and according to the data it change the state of the LED.<br>
The project also contain a basic python script (main.py) based on kivy GUI that open a bluetooth socket and according to the button that press<br>
it sends to the arduino through bluetooth the LED state that user choose in the GUI.<br><br>

My target is to run the python script on smartphone with android OS, unfortanately it doesn't work on android.<br>
The python script tested on Windows OS only, and it work well.<br>
<b>Note:</b> The address of the bluetooth device need to be take care on the python script.
