function same(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    var arr1hash = {};
    arr1.forEach((item) => {
        arr1hash[item] = (arr1hash[item] || 0) + 1;
    });

    var arr2hash = {};
    arr2.forEach((item) => {
        arr2hash[item] = (arr2hash[item] || 0) + 1;
    });

    for (key in arr1hash) {
        if (!(key**2 in arr2hash)) {
            return false;
        }

        if (arr2hash[key**2] !== arr1hash[key]) {
            return false;
        }
    }

    return true;
}

