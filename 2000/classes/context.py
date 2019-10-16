class ContextShifting():
    def __init__(self):
        self.zname = 'init.name'
    
    def __enter__(self): # with block
        self.zname = 'with.enter.name'
    
    def __exit__(self, ex_type, ex_value, traceback):
        self.zname = 'with.exit.name'
    
    def name(self):
        return self.zname

x = ContextShifting()

# Base -- init.name
print('pre:\t', x.name())

#Block entry/exit is normal
if True:
    print('block:\t', x.name())

# Activate __enter__ via 'with' context
try:
    with x:
        print('with:\t', x.name()) # enter block
    print('exitblock:\t', x.name()) # exit block

finally:
    print('finally:\t', x.name()) # exit block

print('post:\t', x.name()) # should be back to normal
