# Name: 
Minimum Add to Make Parentheses Valid

## Difficulty: 
Medium

## Description: 
A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or
- It can be written as <code>(A)</code>, where <code>A</code> is a valid string.

You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.

For example, if <code>s = &quot;()))&quot;</code>, you can insert an opening parenthesis to be <code>&quot;(<strong>(</strong>)))&quot;</code> or a closing parenthesis to be <code>&quot;())<strong>)</strong>)&quot;</code>.

Return the minimum number of moves required to make <code>s</code> valid.

### Example 1:

- **Input:** s = &quot;())&quot;
- **Output:** 1

### Example 2:

- **Input:** s = &quot;(((&quot;
- **Output:** 3

### Constraints:
- <code>1 &lt;= s.length &lt;= 1000</code>
- <code>s[i]</code> is either <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>.