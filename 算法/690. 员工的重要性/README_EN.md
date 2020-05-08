| English | [简体中文](README.md) |

# [690. Employee Importance](https://leetcode-cn.com/problems/employee-importance)
 ### Description
<p>You are given a data structure of employee information, which includes the employee&#39;s <b>unique id</b>, his <b>importance value</b> and his <b>direct</b> subordinates&#39; id.</p>

<p>For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is <b>not direct</b>.</p>

<p>Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
<b>Output:</b> 11
<b>Explanation:</b>
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>One employee has at most one <b>direct</b> leader and may have several subordinates.</li>
	<li>The maximum number of employees won&#39;t exceed 2000.</li>
</ol>

<p>&nbsp;</p>

**Related Topics	**[Depth-first Search](https://leetcode-cn.com/tag/depth-first-search) [Breadth-first Search](https://leetcode-cn.com/tag/breadth-first-search) [Hash Table](https://leetcode-cn.com/tag/hash-table) 

### Similar Question
 - Easy:	[Nested List Weight Sum](https://leetcode-cn.com/problems/nested-list-weight-sum) 
