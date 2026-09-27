# LeetCode 301 - Remove Invalid Parentheses

## Problem Statement

Given a string `s` containing parentheses and letters, remove the minimum number of invalid parentheses to make the string valid.

Return all possible valid strings.

## Example 1

### Input

```text
s = "()())()"
```

### Output

```text
["(())()", "()()()"]
```

## Example 2

### Input

```text
s = "(a)())()"
```

### Output

```text
["(a())()", "(a)()()"]
```

## Example 3

### Input

```text
s = ")("
```

### Output

```text
[""]
```

## Approach

Use **Breadth-First Search (BFS)** to remove the minimum number of invalid parentheses.

BFS checks all strings after removing one character before moving to strings that remove two characters. Therefore, the first valid strings found require the minimum number of removals.

## Algorithm

1. Start with the given string.
2. Check whether the string has valid parentheses.
3. If valid, add it to the result.
4. If not valid, remove one parenthesis at every possible position.
5. Store generated strings in a `visited` set to avoid duplicates.
6. Continue level by level using BFS.
7. Stop generating new strings once valid strings are found.

## Valid Parentheses Check

* Increase the count for `(`.
* Decrease the count for `)`.
* If the count becomes negative, the string is invalid.
* At the end, the count must be `0`.

## Time Complexity

`O(2^n × n)`

## Space Complexity

`O(2^n × n)`

## Key Concepts

* Breadth-First Search
* Queue
* Hash Set
* String Manipulation
* Parentheses Validation

## Language

Python

## LeetCode Details

* **Problem:** 301
* **Title:** Remove Invalid Parentheses
* **Difficulty:** Hard

## Author

**T. Nandhini **

GitHub: `242t605119-dotcom`
