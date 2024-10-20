# Parsing a Boolean Expression

**Problem ID:** 1106

**Difficulty:** Hard

## Content
A **boolean expression** is an expression that evaluates to either `true` or `false`. It can be in one of the following shapes:

- `'t'` that evaluates to `true`.
- `'f'` that evaluates to `false`.
- `'!(subExpr)'` that evaluates to **the logical NOT** of the inner expression `subExpr`.
- `&(subExpr1, subExpr2, ..., subExprn)` that evaluates to **the logical AND** of the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.
- `|(subExpr1, subExpr2, ..., subExprn)` that evaluates to **the logical OR** of the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.

Given a string `expression` that represents a **boolean expression**, return _the evaluation of that expression_.

It is **guaranteed** that the given expression is valid and follows the given rules.

&nbsp;

**Example 1:**

<pre>
<strong>Input:</strong> expression = "&amp;(|(f))"
<strong>Output:</strong> false
<strong>Explanation:</strong> 
First, evaluate |(f) --&gt; f. The expression is now "&amp;(f)".
Then, evaluate &amp;(f) --&gt; f. The expression is now "f".
Finally, return false.
</pre>

**Example 2:**

<pre>
<strong>Input:</strong> expression = "|(f,f,f,t)"
<strong>Output:</strong> true
<strong>Explanation:</strong> The evaluation of (false OR false OR false OR true) is true.
</pre>

**Example 3:**

<pre>
<strong>Input:</strong> expression = "!(&amp;(f,t))"
<strong>Output:</strong> true
<strong>Explanation:</strong> 
First, evaluate &amp;(f,t) --&gt; (false AND true) --&gt; false --&gt; f. The expression is now "!(f)".
Then, evaluate !(f) --&gt; NOT false --&gt; true. We return true.
</pre>

&nbsp;

**Constraints:**

- `1 <= expression.length <= 2 * 10^4`
- `expression[i]` is one following characters: `'('`, `')'`, `'&amp;'`, `'|'`, `'!'`, `'t'`, `'f'`, and `','`.

## Topic Tags
String, Stack, Recursion