
import utilityScript
import random

@utilityScript.getExecTime
def bubbleSort(inpArr):
    arrLen = len(inpArr)
    while arrLen > 0:
        for idx in range(arrLen-1):
            if inpArr[idx] > inpArr[idx+1]:
                inpArr[idx+1],inpArr[idx] = inpArr[idx],inpArr[idx+1]
        arrLen -= 1
    return inpArr


if __name__ == "__main__":

    # testArr = [29,35,8,7,22,5,9,44,64,82,66,21,47,61]
    testArr = [random.random() for _ in range(1000)]

    outArr = bubbleSort(testArr)
    print(outArr)