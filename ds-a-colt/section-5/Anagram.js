function validAnagram(str1, str2) {
    if (str1.length !== str2.length) {
        return false;
    }

    let arr1hash = {};
    for (let i = 0; i < str1.length; i++) {
        let char = str1.charAt(i);
        arr1hash[char] = (arr1hash[char] || 0) + 1;
    }

    for (let i = 0; i < str2.length; i++) {
        let char = str2.charAt(i);
        arr1hash[char] = (arr1hash[char] || 0) - 1;
    }

    for (let key in arr1hash) {
        if (arr1hash[key] !== 0) {
            return false;
        }
    }

    return true;

}