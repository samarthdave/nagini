// reverse('awesome') // 'emosewa'
// reverse('racecar') // 'racecar'

function reverse(input) {
    if (input.length <= 1) {
        return input;
    }

    return reverse(input.slice(1)) + input[0];
}

// exercising some big brain here
// jk, pretty intuitive

// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true

function isPalindrome(input) {
    if (input.length <= 1) return true;

    if (input[0] !== input[input.length - 1]) return false;

    return isPalindrome(input.slice(1, -1));
}

// const isOdd = val => val % 2 !== 0;
// someRecursive([1,2,3,4], isOdd) // true
// return true if any item returns true in callback
function someRecursive(arr, cb) {
    if (arr.length === 1) {
        return cb(arr[0]);
    }

    return (
        someRecursive(arr.slice(1, 2), cb) || someRecursive(arr.slice(1), cb)
    );
}

// flatten([1, 2, 3, [4, 5] ]) // [1, 2, 3, 4, 5]

function flatten(arr) {
    let newArr = [];

    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            newArr = newArr.concat(flatten(arr[i]));
        } else {
            newArr.push(arr[i]);
        }
    }

    return newArr;
}

function nestedEvenSum(inp, sum = 0) {
    for (var key in inp) {
        if (typeof inp[key] === "object") {
            sum += nestedEvenSum(inp[key]);
        } else if (typeof inp[key] === "number" && inp[key] % 2 === 0) {
            sum += inp[key];
        }
    }
    return sum;
}
