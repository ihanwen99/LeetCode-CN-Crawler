| [English](README_EN.md) | 简体中文 |

# [424. 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement)
 ### 题目描述
<p>给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换&nbsp;<em>k&nbsp;</em>次。在执行上述操作后，找到包含重复字母的最长子串的长度。</p>

<p><strong>注意:</strong><br>
字符串长度 和 <em>k </em>不会超过&nbsp;10<sup>4</sup>。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
s = &quot;ABAB&quot;, k = 2

<strong>输出:</strong>
4

<strong>解释:</strong>
用两个&#39;A&#39;替换为两个&#39;B&#39;,反之亦然。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
s = &quot;AABABBA&quot;, k = 1

<strong>输出:</strong>
4

<strong>解释:</strong>
将中间的一个&#39;A&#39;替换为&#39;B&#39;,字符串变为 &quot;AABBBBA&quot;。
子串 &quot;BBBB&quot; 有最长重复字母, 答案为 4。
</pre>

**标签:	**[双指针](https://leetcode-cn.com/tag/two-pointers) [None](https://leetcode-cn.com/tag/sliding-window) 
 ### 相似题目
- 困难:	[至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters) 
- 中等:	[最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii) 
