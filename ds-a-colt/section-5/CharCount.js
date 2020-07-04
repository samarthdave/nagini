function charCount(inputStr) {
    var myHash = {};

    var input = inputStr.toLowerCase();

    for (var i = 0; i < input.length; i++) {
        var char = input.charAt(i);

        if (!/[a-z0-9]/.test(char)) { continue; }

        if (char in myHash) {
            myHash[char] += 1;
        } else {
            myHash[char] = 1;
        }
    }

    return myHash;
}