
import utilityScript
import random

def mergeArr(arrA,arrB, inpArr):
    lenA = len(arrA)
    lenB = len(arrB)
    arrAPtr = arrBPtr = inpArrPtr = 0

    while arrAPtr < lenA and arrBPtr < lenB:
        if arrA[arrAPtr] < arrB[arrBPtr]:
            inpArr[inpArrPtr] = arrA[arrAPtr]
            arrAPtr += 1
        else:
            inpArr[inpArrPtr] = arrB[arrBPtr]
            arrBPtr += 1
        inpArrPtr += 1

    while arrAPtr < lenA:
        inpArr[inpArrPtr] = arrA[arrAPtr]
        arrAPtr += 1
        inpArrPtr += 1
    while arrBPtr < lenB:
        inpArr[inpArrPtr] = arrB[arrBPtr]
        arrBPtr += 1
        inpArrPtr += 1

def mergeSort(inpArr):
    if len(inpArr) == 1:
        return inpArr

    midPtr = len(inpArr)//2
    leftArr = inpArr[:midPtr]
    rightArr = inpArr[midPtr:]
    mergeSort(leftArr)
    mergeSort(rightArr)
    mergeArr(leftArr,rightArr, inpArr)

@utilityScript.getExecTime
def sortArray(inpArr):
    mergeSort(inpArr)
    return inpArr

if __name__ == "__main__":
    testArr = [random.randint(0, 5000) for _ in range(1000)]
    print(testArr)
    print(sortArray(testArr))