function maxSubarraySum(arr, num) {
    if (num > arr.length) {
        return null;
    }

    let firstSum = 0;

    for (let i = 0; i < num; i++) {
        firstSum += arr[i];
    }

    let maxSum = firstSum;
    let tempSum = maxSum;
    for (let g = num; g < arr.length; g++) {
        tempSum = tempSum + arr[g] - arr[g - num];
        maxSum = Math.max(maxSum, tempSum);
    }

    return maxSum;
}