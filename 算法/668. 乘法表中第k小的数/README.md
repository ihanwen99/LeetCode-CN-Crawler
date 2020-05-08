| [English](README_EN.md) | 简体中文 |

# [668. 乘法表中第k小的数](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table)
 ### 题目描述
<p>几乎每一个人都用&nbsp;<a href="https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8">乘法表</a>。但是你能在乘法表中快速找到第<code>k</code>小的数字吗？</p>

<p>给定高度<code>m</code>&nbsp;、宽度<code>n</code> 的一张&nbsp;<code>m * n</code>的乘法表，以及正整数<code>k</code>，你需要返回表中第<code>k</code>&nbsp;小的数字。</p>

<p><strong>例&nbsp;1：</strong></p>

<pre>
<strong>输入:</strong> m = 3, n = 3, k = 5
<strong>输出:</strong> 3
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
</pre>

<p><strong>例 2：</strong></p>

<pre>
<strong>输入:</strong> m = 2, n = 3, k = 6
<strong>输出:</strong> 6
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>m</code> 和&nbsp;<code>n</code>&nbsp;的范围在 [1, 30000] 之间。</li>
	<li><code>k</code> 的范围在 [1, m * n] 之间。</li>
</ol>

**标签:	**[二分查找](https://leetcode-cn.com/tag/binary-search) 
 ### 相似题目
- 中等:	[有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) 
- 困难:	[找出第 k 小的距离对](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance) 
- 困难:	[第 K 个最小的素数分数](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction) 
