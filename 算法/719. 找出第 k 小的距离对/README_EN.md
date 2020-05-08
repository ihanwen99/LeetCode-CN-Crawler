| English | [简体中文](README.md) |

# [719. Find K-th Smallest Pair Distance](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance)
 ### Description
<p>Given an integer array, return the k-th smallest <b>distance</b> among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. </p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
nums = [1,3,1]
k = 1
<b>Output: 0</b> 
<b>Explanation:</b>
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>2 <= len(nums) <= 10000</code>.</li>
<li><code>0 <= nums[i] < 1000000</code>.</li>
<li><code>1 <= k <= len(nums) * (len(nums) - 1) / 2</code>.</li>
</ol>
</p>
**Related Topics	**[Heap](https://leetcode-cn.com/tag/heap) [Array](https://leetcode-cn.com/tag/array) [Binary Search](https://leetcode-cn.com/tag/binary-search) 

### Similar Questions
 - Medium:	[Find K Pairs with Smallest Sums](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums) 
 - Medium:	[Kth Smallest Element in a Sorted Matrix](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) 
 - Medium:	[Find K Closest Elements](https://leetcode-cn.com/problems/find-k-closest-elements) 
 - Hard:	[Kth Smallest Number in Multiplication Table](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table) 
 - Hard:	[K-th Smallest Prime Fraction](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction) 
