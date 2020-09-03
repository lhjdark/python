from gui5 import HelloButton


class MyButton(HelloButton):
    def callback(self):
        print('Igoring press')
        self.quit()


if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop()
