# Sentence Similarity III

**Problem ID:** 1813

**Difficulty:** Medium

## Content
Given two strings `sentence1` and `sentence2`, each representing a sentence composed of words separated by a single space with no leading or trailing spaces, determine if they are similar. Two sentences are considered similar if one can insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal.

## Example 1
**Input:** `sentence1 = "My name is Haley", sentence2 = "My Haley"`
**Output:** `true`
**Explanation:** `sentence2` can be turned to `sentence1` by inserting "name is" between "My" and "Haley".

## Example 2
**Input:** `sentence1 = "of", sentence2 = "A lot of words"`
**Output:** `false`
**Explanation:** No single sentence can be inserted inside one of the sentences to make it equal to the other.

## Example 3
**Input:** `sentence1 = "Eating right now", sentence2 = "Eating"`
**Output:** `true`
**Explanation:** `sentence2` can be turned to `sentence1` by inserting "right now" at the end of the sentence.

## Constraints
- `1 <= sentence1.length, sentence2.length <= 100`
- Both `sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.
- Words in both sentences are separated by a single space.

## Topic Tags
Array, Two Pointers, String