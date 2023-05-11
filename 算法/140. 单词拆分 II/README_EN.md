| English | [简体中文](README.md) |

# [140. Word Break II](https://leetcode.cn/problems/word-break-ii)
 ### Description
<p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, add spaces in <code>s</code> to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in <strong>any order</strong>.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsanddog&quot;, wordDict = [&quot;cat&quot;,&quot;cats&quot;,&quot;and&quot;,&quot;sand&quot;,&quot;dog&quot;]
<strong>Output:</strong> [&quot;cats and dog&quot;,&quot;cat sand dog&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pineapplepenapple&quot;, wordDict = [&quot;apple&quot;,&quot;pen&quot;,&quot;applepen&quot;,&quot;pine&quot;,&quot;pineapple&quot;]
<strong>Output:</strong> [&quot;pine apple pen apple&quot;,&quot;pineapple pen apple&quot;,&quot;pine applepen apple&quot;]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;,&quot;dog&quot;,&quot;sand&quot;,&quot;and&quot;,&quot;cat&quot;]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 10</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
	<li>Input is generated in a way that the length of the answer doesn&#39;t exceed&nbsp;10<sup>5</sup>.</li>
</ul>

**Related Topics**  [Trie](https://leetcode.cn/tag/trie) [Memoization](https://leetcode.cn/tag/memoization) [Array](https://leetcode.cn/tag/array) [Hash Table](https://leetcode.cn/tag/hash-table) [String](https://leetcode.cn/tag/string) [Dynamic Programming](https://leetcode.cn/tag/dynamic-programming) [Backtracking](https://leetcode.cn/tag/backtracking) 

### Similar Questions
