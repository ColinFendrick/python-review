import sys
# print(sys.path)
for ref in sys.path:
    print(ref)

for zIndex, zNode in enumerate(sys.modules):
    print(zIndex, zNode)
