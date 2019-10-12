class firstClass:
    def __init__(self, parm1, parm2, parm3):
        self.parm1 = parm1
        self.parm2 = parm2
        self.parm3 = parm3

    def firstMethod(self):
        print(self.parm2 + '\n') 
    
c = firstClass(1, 'second', True)

print(c.parm1)
print(c.parm3)
c.firstMethod()

#Use the pass keyword when you do not want to add any other properties or methods to the class.
class childClass(firstClass):
#   pass
"""
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
"""
    def __init__(self, parm1, parm2, parm3):
        # firstClass.__init__(self, parm1, parm2, parm3)
        """Python also has a super() function that will make the child class inherit all the methods and properties from its parent"""
        super.__init__(self, parm1, parm2, parm3)
        # Add new properties
        self.graduationyear = 2019
"""
If you add a method in the child class with the same name as a 
function in the parent class, the inheritance of the parent method will be overridden.
"""

d = childClass(111,'hahaS',333)

d.firstMethod()