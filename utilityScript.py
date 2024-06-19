
import time

def getExecTime(func):
    def wrapperFunc(*args, **kwargs):
        startTime = time.time()
        result = func(*args,**kwargs)
        endTime = time.time()
        print(f"Exec Time: {(endTime - startTime)*1000}")
        return result
    return wrapperFunc