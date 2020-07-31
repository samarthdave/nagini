/////////////////////////////////////////////////
// collab9.go
//
// Your name:
// Your andrew id:
/////////////////////////////////////////////////

package main

import (
    "fmt"
)

/////////////////////////////////////////////////
// Helper functions
/////////////////////////////////////////////////

func assert(b bool) {
    if !b {
        panic("Assertion Error")
    }
}

func slicesEqual(a1, a2 []int) bool {
    if len(a1) != len(a2) {
        return false
    }
    for i := 0; i < len(a1); i += 1 {
        if a1[i] != a2[i] {
            return false
        }
    }
    return true
}

/////////////////////////////////////////////////
// Functions for you to write
/////////////////////////////////////////////////

// isEquilateralTriangle
func isEquilateralTriangle(a int, b int, c int) bool {
    return a == b && b == c
}

// carrylessAdd
/* Hint: You may find it useful to run int(math.Pow10(n)) to get an int
representing the nth power of 10. You could also write your own pow10 func */
func carrylessAdd(a int, b int) bool {
    return false
}

// inverseLookAndSay
// func inverseLookAndSay() {

// }

/////////////////////////////////////////////////
// Test Functions
////////////////////////////////////////////////

func testIsEquilateralTriangle() {
    fmt.Print("Testing isEquilateralTriangle()... ")
    assert(isEquilateralTriangle(1, 2, 3) == false)
    assert(isEquilateralTriangle(11, 11, 11) == true)
    assert(isEquilateralTriangle(1, 1, 3) == false)
    assert(isEquilateralTriangle(1, 3, 3) == false)
    assert(isEquilateralTriangle(1, 3, 1) == false)
    fmt.Println("Passed!")
}

func testCarrylessAdd() {
    fmt.Print("Testing carrylessAdd()...")
    assert(carrylessAdd(0, 0) == 0)
    assert(carrylessAdd(4, 5) == 9)
    assert(carrylessAdd(23, 57) == 70)
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(102, 108) == 200)
    assert(carrylessAdd(865, 23) == 888)
    fmt.Println("Passed!")
}

func testInverseLookAndSay() {
    fmt.Print("Testing inverseLookAndSay()...")
    assert(slicesEqual(
        inverseLookAndSay([][]int{}),
        []int{}))
    assert(slicesEqual(
        inverseLookAndSay([][]int{{1, 1}}),
        []int{1}))
    assert(slicesEqual(
        inverseLookAndSay([][]int{{3, 1}}),
        []int{1, 1, 1}))
    assert(slicesEqual(
        inverseLookAndSay([][]int{{1, 1}, {2, 2}, {3, 3}, {4, 4}}),
        []int{1, 2, 2, 3, 3, 3, 4, 4, 4, 4}))
    assert(slicesEqual(
        inverseLookAndSay([][]int{{2, 3}, {1, 8}, {3, -10}}),
        []int{3, 3, 8, -10, -10, -10}))
    fmt.Println("Passed!")
}

/////////////////////////////////////////////////
// collab9 Main
////////////////////////////////////////////////

func testAll() {
    testIsEquilateralTriangle()
    testCarrylessAdd()
    testInverseLookAndSay()
}

func main() {
    testAll()
}
