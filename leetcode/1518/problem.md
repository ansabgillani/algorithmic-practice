# Water Bottles

**Problem ID:** 1518  
**Difficulty:** Easy  

## Description
There are `numBottles` water bottles that are initially full of water. You can exchange `numExchange` empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers `numBottles` and `numExchange`, return **the maximum number of water bottles you can drink**.

## Examples

### Example 1
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_1_1875.png" style="width: 500px; height: 245px;" />
**Input:** numBottles = 9, numExchange = 3  
**Output:** 13  
**Explanation:** You can exchange 3 empty bottles to get 1 full water bottle.  
Number of water bottles you can drink: 9 + 3 + 1 = 13.


### Example 2
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_2_1875.png" style="width: 500px; height: 183px;" />
**Input:** numBottles = 15, numExchange = 4  
**Output:** 19  
**Explanation:** You can exchange 4 empty bottles to get 1 full water bottle.  
Number of water bottles you can drink: 15 + 3 + 1 = 19.


## Constraints
- `1 <= numBottles <= 100`
- `2 <= numExchange <= 100`

## Topic Tags
- Math
- Simulation