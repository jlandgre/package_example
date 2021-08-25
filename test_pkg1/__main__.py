#Import the main() function from the testmain.py driver file
from testmain import main

#__name__ will be '__main__' whenever this file is run either directly or from zsh shell command
print('Finished importing testmain.py main(): __name__', __name__)

#Call the driver function in testmain.py
main()