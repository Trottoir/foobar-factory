# Global counter for multithread
COUNT = 2
        
def get_counter():
    global COUNT
    COUNT = COUNT+1
    return COUNT