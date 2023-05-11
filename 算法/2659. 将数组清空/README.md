| [English](README_EN.md) | 简体中文 |

# [2659. 将数组清空](https://leetcode.cn/problems/make-array-empty)
<p>给你一个包含若干 <strong>互不相同</strong>&nbsp;整数的数组&nbsp;<code>nums</code>&nbsp;，你需要执行以下操作 <strong>直到</strong><strong>数组为空</strong>&nbsp;：</p>

<ul>
	<li>如果数组中第一个元素是当前数组中的 <strong>最小值</strong>&nbsp;，则删除它。</li>
	<li>否则，将第一个元素移动到数组的 <strong>末尾</strong>&nbsp;。</li>
</ul>

<p>请你返回需要多少个操作使<em>&nbsp;</em><code>nums</code><em>&nbsp;</em>为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,4,-1]
<b>输出：</b>5
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[4, -1, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[-1, 3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">4</td>
			<td style="border: 2px solid black; padding: 5px;">[4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">5</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,4,3]
<b>输出：</b>5
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[2, 4, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[4, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">4</td>
			<td style="border: 2px solid black; padding: 5px;">[4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">5</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3]
<b>输出：</b>3
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[2, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9&nbsp;</sup>&lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;中的元素 <strong>互不相同</strong>&nbsp;。</li>
</ul>

**标签:**  [贪心](https://leetcode.cn/tag/greedy) [树状数组](https://leetcode.cn/tag/binary-indexed-tree) [线段树](https://leetcode.cn/tag/segment-tree) [数组](https://leetcode.cn/tag/array) [二分查找](https://leetcode.cn/tag/binary-search) [有序集合](https://leetcode.cn/tag/ordered-set) [排序](https://leetcode.cn/tag/sorting) 