// binary serach... a classic if there ever was one

// accepts a sorted array and looks for target
function binarySearch(sortedArr, target) {
    let left = 0,
        right = sortedArr.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (sortedArr[mid] === target) {
            return mid;
        }

        if (sortedArr[mid] > target) {
            right = mid - 1;
        } else {
            // arr[mid] < target
            left = mid + 1;
        }
    }

    return -1;
}

// Naive String Search
// find substring occurrences in larger string (case sensitive)
// pretty inefficient but that's why it's "naive"
// ex.
//     naiveSearch("haha Haha", "haha") --> 1
//     naiveSearch("Harold said haha in Hamburg", "haha") --> 1
function naiveSearch(long, short) {
    let matchCount = 0;
    // loop through both strings
    for (let i = 0; i < long.length; i++) {
        let matchLength = 0;
        // loop through smaller string
        for (let j = 0; j < short.length; j++) {
            // if they don't match then break; else increment
            if (long[i + j] !== short[j]) break;
            matchLength += 1;
        }
        // if we found the string, increment matchCount
        if (matchLength === short.length) matchCount += 1;
    }
    return matchCount;
}

naiveSearch("Harold said haha in Hamburg", "haha")
