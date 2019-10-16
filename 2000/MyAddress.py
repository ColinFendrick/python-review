def dumper(theme, zlist):
    print(theme)
    for ref in zlist:
        print('\tAddress:', hex(id(ref)), '\t{}'.format(ref))
    print('Collections:', hex(id(zlist)))

zData = ['One', 'Two', 'Three']
dumper('Original', zData)

cpDeep = list(zData) # This will create a new object (collections address is new)
# but the elements are simply pointers to the original list items
dumper('Deep-copy', cpDeep)

cpShallow = zData
dumper('Shallow-copy', cpShallow)

zData[0] = 'One' # Reassigning to the same value does not create a new pointer!
zData[1] = 'Five'
zData[2] = 'Six'
dumper('New-contents', zData) # This keeps the pointer to the original collection
# but each element is swapped with a new address
dumper('After-new-contents-shallow', cpShallow) # Since this is a pointer to the object, it will change to point to the new contents
dumper('After-new-contents-deep', cpDeep) # This is a new object, so this retains its contents and addresses, and keeps the original content pointers

zData = ['Seven', 'Eight', 'Nine'] # This creates an entirely new collection and address list
dumper('New-collection', zData)
