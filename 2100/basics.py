class Able:
    def say_hello(self):
        print('Hello from Able')

    def say_anything(self, val):
        print('Able saying %s' % val)


class Baker(Able):
    def say_hello(self):
        return super().say_hello()

    def say_anything(self, val):
        print('Baker overwriting and saying %s' % val)

baker = Baker()
baker.say_anything('something')
print('Is baker an instance of able?\t {}'.format(isinstance(baker, Able)))
