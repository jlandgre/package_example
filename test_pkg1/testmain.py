import testlib

def main():
    #Instantiate the class
    cl = testlib.TestClass('abc')
    print(cl.param)
    print(type(cl.df))

print('in testmain, __name__:', __name__)
if __name__ == '__main__':
    print('Running standalone from testmain.py')
    main()