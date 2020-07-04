function countUniqueValues(arr1) {
    if (arr1.length == 0) {
        return 0;
    }

    let counter = 1;

    for (let i = 1; i < arr1.length; i++) {
        if (arr1[i] !== arr1[i-1]) {
            counter += 1;
        }
    }

    return counter;
}