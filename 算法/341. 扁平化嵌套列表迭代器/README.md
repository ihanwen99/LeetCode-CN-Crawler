| [English](README_EN.md) | 简体中文 |

# [341. 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator)
 ### 题目描述
<p>给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。</p>

<p>列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[[1,1],2,[1,1]]
<strong>输出: </strong>[1,1,2,1,1]
<strong>解释: </strong>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[1,[4,[6]]]
<strong>输出: </strong>[1,4,6]
<strong>解释: </strong>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>。
</pre>

**标签:	**[栈](https://leetcode-cn.com/tag/stack) [设计](https://leetcode-cn.com/tag/design) 
 ### 相似题目
- 中等:	[展开二维向量](https://leetcode-cn.com/problems/flatten-2d-vector) 
- 中等:	[锯齿迭代器](https://leetcode-cn.com/problems/zigzag-iterator) 
- 中等:	[迷你语法分析器](https://leetcode-cn.com/problems/mini-parser) 
- 中等:	[数组嵌套](https://leetcode-cn.com/problems/array-nesting) 
