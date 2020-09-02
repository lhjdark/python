class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in replacer.method')

class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
        print('\n provider....')
        x = Provider()
        x.delegate()