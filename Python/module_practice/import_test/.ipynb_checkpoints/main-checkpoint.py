#Jupyter lab requires to shut down and restart kernel to 
#reflect the modification of imported modules


#from module import class
from module import imported_class

instance1 = imported_class()
try:
    instance1.func1()
except Exception as excep:
    print(str(excep))
    
#Import module
import module

instance2 = module.imported_class()
try:
    instance2.func1()
except Exception as excep:
    print(str(excep))

    
#Directly call function inside class inside module    
try:
    module.imported_class.func1()
except Exception as excep:
    print(str(excep)) #Always Error


import package
from package import module
from package.sub_package import sub_module

#Import sub_module.py inside sub_package inside package
import package.sub_package.sub_module
