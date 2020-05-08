| English | [简体中文](README.md) |

# [30. Substring with Concatenation of All Words](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words)
 ### Description
<p>You are given a string, <strong>s</strong>, and a list of words, <strong>words</strong>, that are all of the same length. Find all starting indices of substring(s) in <strong>s</strong> that is a concatenation of each word in <strong>words</strong> exactly once and without any intervening characters.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>Output:</strong> <code>[0,9]</code>
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are &quot;barfoo&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;wordgoodgoodgoodbestword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
<strong>Output:</strong> <code>[]</code>
</pre>

**Related Topics**  [Hash Table](https://leetcode-cn.com/tag/hash-table) [Two Pointers](https://leetcode-cn.com/tag/two-pointers) [String](https://leetcode-cn.com/tag/string) 

### Similar Question
 - Hard:	[Minimum Window Substring](https://leetcode-cn.com/problems/minimum-window-substring) 
