
import utilityScript
import random

def insertionSort(inpArr):
    arrLen = len(inpArr)

    for idx in range(1, arrLen):
        tIdx = idx
        while inpArr[tIdx] < inpArr[tIdx-1] and tIdx >= 1:
            inpArr[tIdx],inpArr[tIdx - 1] = inpArr[tIdx-1],inpArr[tIdx]
            tIdx -= 1

@utilityScript.getExecTime
def sortArray(inpArr):
    insertionSort(inpArr)
    return inpArr

if __name__ == "__main__":
    testArr = [random.randint(0, 5000) for _ in range(1000)]
    print(testArr)
    print(sortArray(testArr))