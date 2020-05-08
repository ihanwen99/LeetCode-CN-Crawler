| [English](README_EN.md) | 简体中文 |

# [315. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self)
 ### 题目描述
<p>给定一个整数数组 <em>nums</em>，按要求返回一个新数组&nbsp;<em>counts</em>。数组 <em>counts</em> 有该性质： <code>counts[i]</code> 的值是&nbsp; <code>nums[i]</code> 右侧小于&nbsp;<code>nums[i]</code> 的元素的数量。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [5,2,6,1]
<strong>输出:</strong> <code>[2,1,1,0] 
<strong>解释:</strong></code>
5 的右侧有 <strong>2 </strong>个更小的元素 (2 和 1).
2 的右侧仅有 <strong>1 </strong>个更小的元素 (1).
6 的右侧有 <strong>1 </strong>个更小的元素 (1).
1 的右侧有 <strong>0 </strong>个更小的元素.
</pre>

**标签:	**[排序](https://leetcode-cn.com/tag/sort) [树状数组](https://leetcode-cn.com/tag/binary-indexed-tree) [线段树](https://leetcode-cn.com/tag/segment-tree) [二分查找](https://leetcode-cn.com/tag/binary-search) [分治算法](https://leetcode-cn.com/tag/divide-and-conquer) 
 ### 相似题目
- 困难:	[区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum) 
- 中等:	[根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height) 
- 困难:	[翻转对](https://leetcode-cn.com/problems/reverse-pairs) 
