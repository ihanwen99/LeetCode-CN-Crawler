| [English](README_EN.md) | 简体中文 |

# [1004. 最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii)
 ### 题目描述
<p>给定一个由若干 <code>0</code> 和 <code>1</code> 组成的数组&nbsp;<code>A</code>，我们最多可以将&nbsp;<code>K</code>&nbsp;个值从 0 变成 1 。</p>

<p>返回仅包含 1 的最长（连续）子数组的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
<strong>输出：</strong>6
<strong>解释： </strong>
[1,1,1,0,0,<strong>1</strong>,1,1,1,1,<strong>1</strong>]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
<strong>输出：</strong>10
<strong>解释：</strong>
[0,0,1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>0 &lt;= K &lt;= A.length</code></li>
	<li><code>A[i]</code> 为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;</li>
</ol>

**标签:	**[双指针](https://leetcode-cn.com/tag/two-pointers) [None](https://leetcode-cn.com/tag/sliding-window) 
 ### 相似题目
- 困难:	[至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters) 
- 中等:	[替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement) 
- 简单:	[最大连续1的个数](https://leetcode-cn.com/problems/max-consecutive-ones) 
- 中等:	[最大连续1的个数 II](https://leetcode-cn.com/problems/max-consecutive-ones-ii) 
