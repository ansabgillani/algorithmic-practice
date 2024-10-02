# Minimum Number of Days to Make m Bouquets

## Difficulty: 
Medium

## Description: 
You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden.

The garden consists of `n` flowers, where the `i-th` flower will bloom in the `bloomDay[i]` day and can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets return `-1`.

### Example 1:

- **Input:** `bloomDay = [1,10,3,10,2], m = 3, k = 1`
- **Output:** `3`
- **Explanation:** By the third day, we can make three bouquets.

### Example 2:

- **Input:** `bloomDay = [1,10,3,10,2], m = 3, k = 2`
- **Output:** `-1`
- **Explanation:** It's impossible to create the required number of bouquets with the given flowers and conditions.

### Example 3:

- **Input:** `bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3`
- **Output:** `12`
- **Explanation:** By day 12, we can make two bouquets.

### Constraints:
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`