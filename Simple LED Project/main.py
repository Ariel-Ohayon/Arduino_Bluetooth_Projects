import socket
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        
        self.grid = GridLayout()
        self.grid.cols = 2
        
        self.rows=4
        self.add_widget(Label(text="LED Bluetooth Application"))
        
        # Adding ON_Button
        self.ON_Button = Button(text="ON")
        self.ON_Button.bind(on_press = self.press_on)
        self.grid.add_widget(self.ON_Button)
        
        # Adding OFF_Button
        self.OFF_Button = Button(text="OFF")
        self.OFF_Button.bind(on_press = self.press_off)
        self.grid.add_widget(self.OFF_Button)
        
        self.Connect_Button = Button(text = "Connect")
        self.Connect_Button.bind(on_press = self.Connect)
        self.add_widget(self.Connect_Button)
        
        self.add_widget(self.grid)
        self.add_widget(Label(text = "LED State: "))
        
    def press_on(self,instance):
        print('Press On')
        self.sock.send('ON'.encode())
        
    def press_off(self,instance):
        print('Press Off')
        self.sock.send('OFF'.encode())
        
    def Connect(self,instance):
        print('Connetct to HC05')
        self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.sock.connect(("98:D3:81:F5:B6:E4", 1))
        print(self.sock)
        '''if(self.sock.stillconnected() is True):
            print('Connection Success')
        else:
            print('Connection failed')'''
        self.sock.send('1234'.encode('UTF-8'))
        
        
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()