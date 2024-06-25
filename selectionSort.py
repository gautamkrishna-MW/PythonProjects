
import utilityScript
import random

def selectionSort(inpArr):
    for idx in range(len(inpArr)):
        for subIdx in range(idx, len(inpArr)):
            if inpArr[idx] > inpArr[subIdx]:
                inpArr[idx], inpArr[subIdx] = inpArr[subIdx], inpArr[idx]

@utilityScript.getExecTime
def sortArray(inpArr):
    selectionSort(inpArr)
    return inpArr

if __name__ == "__main__":
    testArr = [random.randint(0, 5000) for _ in range(1000)]
    print(testArr)
    print(sortArray(testArr))