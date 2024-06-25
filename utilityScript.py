
import time
import statistics


def getExecTime(func):
    def wrapperFunc(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        execTime = (endTime - startTime) * 1000
        print(f"Exec Time: {execTime}")
        return result
    return wrapperFunc