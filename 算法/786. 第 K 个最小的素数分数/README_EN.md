| English | [简体中文](README.md) |

# [786. K-th Smallest Prime Fraction](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction)
 ### Description
<p>A sorted list <code>A</code> contains 1, plus some number of primes.&nbsp; Then, for every p &lt; q in the list, we consider the fraction p/q.</p>

<p>What is the <code>K</code>-th smallest fraction considered?&nbsp; Return your answer as an array of ints, where <code>answer[0] = p</code> and <code>answer[1] = q</code>.</p>

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> A = [1, 2, 3, 5], K = 3
<strong>Output:</strong> [2, 5]
<strong>Explanation:</strong>
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

<strong>Input:</strong> A = [1, 7], K = 1
<strong>Output:</strong> [1, 7]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code> will have length between <code>2</code> and <code>2000</code>.</li>
	<li>Each <code>A[i]</code> will be between <code>1</code> and <code>30000</code>.</li>
	<li><code>K</code> will be between <code>1</code> and <code>A.length * (A.length - 1) / 2</code>.</li>
</ul>
**Related Topics	**[Heap](https://leetcode-cn.com/tag/heap) [Binary Search](https://leetcode-cn.com/tag/binary-search) 

### Similar Questions
 - Medium:	[Kth Smallest Element in a Sorted Matrix](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) 
 - Hard:	[Kth Smallest Number in Multiplication Table](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table) 
 - Hard:	[Find K-th Smallest Pair Distance](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance) 
