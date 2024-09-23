# Extra Characters in a String

**Problem ID:** 2707

**Difficulty:** Medium

## Content
Given a `0-indexed` string `s` and a dictionary of words `dictionary`, break `s` into one or more **non-overlapping** substrings such that each substring is present in `dictionary`. Return the **minimum** number of extra characters left over if you break up `s` optimally.

## Examples

### Example 1
**Input:** s = "leetscode", dictionary = ["leet","code","leetcode"]
**Output:** 1
**Explanation:** Break `s` into two substrings: "leet" and "code". There is only one unused character (at index 4), so return 1.


### Example 2
**Input:** s = "sayhelloworld", dictionary = ["hello","world"]
**Output:** 3
**Explanation:** Break `s` into two substrings: "hello" and "world". The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, return 3.


## Constraints
- `1 <= s.length <= 50`
- `1 <= dictionary.length <= 50`
- `1 <= dictionary[i].length <= 50`
- `dictionary[i]` and `s` consist of only lowercase English letters
- `dictionary` contains distinct words

## Topic Tags
- Array
- Hash Table
- String
- Dynamic Programming
- Trie