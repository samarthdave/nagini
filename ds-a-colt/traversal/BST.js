class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }
    insert(value) {
        let newNode = new Node(value);
        if (this.root === null) {
            this.root = newNode;
            return this;
        }
        let current = this.root;
        while (true) {
            if (value === current.value) return undefined;
            if (value < current.value) {
                if (current.left === null) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if (current.right === null) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }
    find(value) {
        if (this.root === null) return false;
        let current = this.root,
            found = false;
        while (current && !found) {
            if (value < current.value) {
                current = current.left;
            } else if (value > current.value) {
                current = current.right;
            } else {
                found = true;
            }
        }
        if (!found) return undefined;
        return current;
    }
    contains(value) {
        if (this.root === null) return false;
        let current = this.root,
            found = false;
        while (current && !found) {
            if (value < current.value) {
                current = current.left;
            } else if (value > current.value) {
                current = current.right;
            } else {
                return true;
            }
        }
        return false;
    }
    BFS() {
        // check if empty
        if (this.root === null) return [];

        let queue = [];
        let result = [];
        // not empty, add head to queue
        queue.push(this.root);

        while (queue.length !== 0) {
            // take first item from queue
            let current = queue.shift();
            result.push(current.value);

            // if first item has children, add them to queue
            if (current.left) queue.push(current.left);
            if (current.right) queue.push(current.right);
        }

        return result;
    }

    DFS_PreOrder() {
        if (this.root === null) return [];
        let result = [];

        function traverse(node) {
            result.push(node.value);
            // go left & right
            if (node.left) traverse(node.left, result);
            if (node.right) traverse(node.right, result);
        }
        traverse(this.root);
        return result;
    }

    DFS_PostOrder() {
        if (this.root === null) return [];
        let result = [];

        function traverse(node) {
            // go left & right
            if (node.left) traverse(node.left, result);
            if (node.right) traverse(node.right, result);
            result.push(node.value);
        }
        traverse(this.root);
        return result;
    }
}

let tree = new BinarySearchTree();
tree.insert(10);
tree.insert(6);
tree.insert(15);
tree.insert(3);
tree.insert(8);
tree.insert(20);

//         10
//     6       15
//  3    8         20

let result = tree.DFS_PostOrder();
// should be [3,8,6,20,15,10]
console.log(result);

// let treeTest = [10, 6, 15, 3, 8, 20];
// console.log(treeTest.unshift())
// console.log(treeTest)
