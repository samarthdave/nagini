// power(2,0) // 1
// power(2,2) // 4
// power(2,4) // 16

// power - implement Math.pow using recursion
// don't worry about negative bases or exponents
function power(num, pow) {
    if (pow === 0) {
        return 1;
    } else if (pow === 1) {
        return num;
    } else {
        return num * power(num, pow - 1);
    }
}

// factorial(4) // 24
// factorial(7) // 5040

// 4! = 4 * 3 * 2 * 1
function factorial(num) {
    // not technically correct but assume positive values
    if (num <= 1) return 1;

    return num * factorial(num - 1);
}

// productOfArray([1,2,3,10]) --> 60
//                 1 * 2 * 3 * 10 = 60
function productOfArray(arr) {
    if (arr.length === 0) {
        return 1;
    }

    return arr[0] * productOfArray(arr.slice(1));
}

// recursiveRange(6) --> 21
// 6 + 5 + 4 + 3 + 2 + 1 = 21
function recursiveRange(num) {
    if (num <= 0) {
        return 0;
    }

    return num + recursiveRange(num - 1);
}

// fib(35) --> 9227465
// 1,1,2,3,5,8 ...
function fib(num) {
    if (num <= 2) return 1;

    return fib(num - 2) + fib(num - 1);
}

function fibIterative(n) {
    if (n <= 1) return n;

    let fib0 = 0;
    let fib1 = 1;
    let sum = 0;
    for (let i = 2; i <= n; i++) {
        sum = fib0 + fib1;
        fib0 = fib1;
        fib1 = sum;
    }

    return sum;
}
