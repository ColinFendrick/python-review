#! usr/bin/env python3

from collections import OrderedDict
import sys
bog = OrderedDict(foo='bar', foo2='net')
print(dir(sys.modules))
for line in sys.modules:
    print(line)

print(sys.path)
