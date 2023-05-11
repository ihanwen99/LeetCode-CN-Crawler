| [English](README_EN.md) | 简体中文 |

# [1044. 最长重复子串](https://leetcode.cn/problems/longest-duplicate-substring)
<p>给你一个字符串 <code>s</code> ，考虑其所有 <em>重复子串</em> ：即&nbsp;<code>s</code> 的（连续）子串，在 <code>s</code> 中出现 2 次或更多次。这些出现之间可能存在重叠。</p>

<p>返回 <strong>任意一个</strong> 可能具有最长长度的重复子串。如果 <code>s</code> 不含重复子串，那么答案为 <code>""</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "banana"
<strong>输出：</strong>"ana"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd"
<strong>输出：</strong>""
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

**标签:**  [字符串](https://leetcode.cn/tag/string) [二分查找](https://leetcode.cn/tag/binary-search) [后缀数组](https://leetcode.cn/tag/suffix-array) [滑动窗口](https://leetcode.cn/tag/sliding-window) [哈希函数](https://leetcode.cn/tag/hash-function) [滚动哈希](https://leetcode.cn/tag/rolling-hash) 