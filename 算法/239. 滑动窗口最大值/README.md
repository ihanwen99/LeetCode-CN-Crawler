| [English](README_EN.md) | 简体中文 |

# [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum)
 ### 题目描述
<p>给定一个数组 <em>nums</em>，有一个大小为&nbsp;<em>k&nbsp;</em>的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 <em>k</em>&nbsp;个数字。滑动窗口每次只向右移动一位。</p>

<p>返回滑动窗口中的最大值。</p>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你能在线性时间复杂度内解决此题吗？</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>, 和 <em>k</em> = 3
<strong>输出: </strong><code>[3,3,5,5,6,7] 
<strong>解释: 
</strong></code>
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7       <strong>5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>-10^4&nbsp;&lt;= nums[i]&nbsp;&lt;= 10^4</code></li>
	<li><code>1 &lt;= k&nbsp;&lt;= nums.length</code></li>
</ul>

**标签:**  [堆](https://leetcode-cn.com/tag/heap) [None](https://leetcode-cn.com/tag/sliding-window) 
 ### 相似题目
- 困难:	[最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring) 
- 简单:	[最小栈](https://leetcode-cn.com/problems/min-stack) 
- 中等:	[至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters) 
- 困难:	[粉刷房子 II](https://leetcode-cn.com/problems/paint-house-ii) 
