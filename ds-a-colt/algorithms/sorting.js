// bubble sort
// inefficient but I also forgot how to implement this so here goes

function bubbleSort(arr) {
    const swap = (target, index1, index2) => {
        // es2015 swap
        [target[index1], target[index2]] = [target[index2], target[index1]]
    }
    for (let i = arr.length - 1; i >= 0; i--) {
        for (let j = 0; j < i; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr, j, j+1)
            }
        }
    }
    return arr;
}

bubbleSort([5,3,8,1])