| [English](README_EN.md) | 简体中文 |

# [659. 分割数组为连续子序列](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences)
 ### 题目描述
<p>输入一个按升序排序的整数数组（可能包含重复数字），你需要将它们分割成几个子序列，其中每个子序列至少包含三个连续整数。返回你是否能做出这样的分割？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,3,4,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,3,4,4,5,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,4,4,5]
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>输入的数组长度范围为 [1, 10000]</li>
</ol>

<p>&nbsp;</p>

**标签:**  [堆](https://leetcode-cn.com/tag/heap) [贪心算法](https://leetcode-cn.com/tag/greedy) 
 ### 相似题目
- 中等:	[前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements) 
