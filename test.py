import time
class Test:
    def __init__(self):
        print("Object Initialization..")

    def __del__(self):
        print("Fulfilling LAst Wish and performing clean up activities..")
    
t1 = Test()
t1 = None
time.sleep(10)
print("End of application")

    
        
     
    
       