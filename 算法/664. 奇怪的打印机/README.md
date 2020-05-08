| [English](README_EN.md) | 简体中文 |

# [664. 奇怪的打印机](https://leetcode-cn.com/problems/strange-printer)
 ### 题目描述
<p>有台奇怪的打印机有以下两个特殊要求：</p>

<ol>
	<li>打印机每次只能打印同一个字符序列。</li>
	<li>每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。</li>
</ol>

<p>给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;aaabbb&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后打印 &quot;bbb&quot;。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;aba&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后在第二个位置打印 &quot;b&quot; 覆盖掉原来的字符 &#39;a&#39;。</pre>

<p><strong>提示</strong>: 输入字符串的长度不会超过 100。</p>

**标签:	**[深度优先搜索](https://leetcode-cn.com/tag/depth-first-search) [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 困难:	[移除盒子](https://leetcode-cn.com/problems/remove-boxes) 
