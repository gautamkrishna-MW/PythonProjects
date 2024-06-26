
import utilityScript
import random

def bubbleSort(inpArr):
    arrLen = len(inpArr)
    while arrLen > 0:
        for idx in range(arrLen-1):
            if inpArr[idx] > inpArr[idx+1]:
                inpArr[idx+1],inpArr[idx] = inpArr[idx],inpArr[idx+1]
        arrLen -= 1

@utilityScript.getExecTime
def sortArray(inpArr):
    bubbleSort(inpArr)
    return inpArr

if __name__ == "__main__":
    testArr = [random.randint(0, 5000) for _ in range(1000)]
    print(testArr)
    print(sortArray(testArr))