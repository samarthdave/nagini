// bubble sort
// inefficient but I also forgot how to implement this so here goes

function bubbleSort(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        for (let j = 0; j < i; j++) {
            console.log(arr, arr[j], arr[j+1])
            if (arr[j] > arr[j+1]) {
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    console.log("done:")
    console.log(arr);
    return arr;
}

bubbleSort([5,3,8,1])