# Lemonade Change

**Problem ID:** 860  
**Difficulty:** Easy  

## Content
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the i<sup>th</sup> customer pays, return true if you can provide every customer with the correct change, or false otherwise.

&nbsp;

**Example 1:**

Input: bills = [5,5,5,10,20]<br>
Output: true<br>
Explanation:<br>
From the first 3 customers, we collect three $5 bills in order.<br>
From the fourth customer, we collect a $10 bill and give back a $5.<br>
From the fifth customer, we give a $10 bill and a $5 bill.<br>
Since all customers got correct change, we output true.

&nbsp;

**Example 2:**

Input: bills = [5,5,10,10,20]<br>
Output: false<br>
Explanation:<br>
From the first two customers in order, we collect two $5 bills.<br>
For the next two customers in order, we collect a $10 bill and give back a $5 bill.<br>
For the last customer, we can not give the change of $15 back because we only have two $10 bills.<br>
Since not every customer received the correct change, the answer is false.

&nbsp;

**Constraints:**

- 1 <= bills.length <= 10<sup>5</sup><br>
- `bills[i]` is either 5, 10, or 20.

## Topic Tags
Array, Greedy