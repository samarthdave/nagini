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
// find substring occurrences in larger string
// pretty inefficient but that's why it's "naive"
// ex.
//     naiveSearch("Harold said haha in Hamburg", "haha")
function naiveSearch(long, short) {
    let matchCount = 0;
    // loop through both strings
    for (let i = 0; i < long.length; i++) {
        let matchLength = 0;
        // loop through smaller string
        for (let j = 0; j < short.length; j++) {
            if (long[i + j] === short[j]) {
                // we're good
                matchLength += 1;
            } else {
                break;
            }
        }
        // if we found the string, increment matchCount
        if (matchLength === short.length) {
            console.log(`${short} found in ${long}`);
            console.log(`at ${i}`);
            matchCount += 1;
        }
    }
    return matchLength;
}

const res = naiveSearch("Harold said haha in Hamburg", "haha");
console.log(res);
