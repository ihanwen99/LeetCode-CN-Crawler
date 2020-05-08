| English | [简体中文](README.md) |

# [239. Sliding Window Maximum](https://leetcode-cn.com/problems/sliding-window-maximum)
 ### Description
<p>Given an array <em>nums</em>, there is a sliding window of size <em>k</em> which is moving from the very left of the array to the very right. You can only see the <em>k</em> numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.</p>

<p><strong>Follow up:</strong><br />
Could you solve it in linear time?</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>, and <em>k</em> = 3
<strong>Output: </strong><code>[3,3,5,5,6,7] 
<strong>Explanation: 
</strong></code>
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>-10^4&nbsp;&lt;= nums[i]&nbsp;&lt;= 10^4</code></li>
	<li><code>1 &lt;= k&nbsp;&lt;= nums.length</code></li>
</ul>

**Related Topics**  [Heap](https://leetcode-cn.com/tag/heap) [Sliding Window](https://leetcode-cn.com/tag/sliding-window) 

### Similar Questions
 - Hard:	[Minimum Window Substring](https://leetcode-cn.com/problems/minimum-window-substring) 
 - Easy:	[Min Stack](https://leetcode-cn.com/problems/min-stack) 
 - Medium:	[Longest Substring with At Most Two Distinct Characters](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters) 
 - Hard:	[Paint House II](https://leetcode-cn.com/problems/paint-house-ii) 
