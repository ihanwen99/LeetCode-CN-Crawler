| [English](README_EN.md) | 简体中文 |

# [257. 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths)
<p>给你一个二叉树的根节点 <code>root</code> ，按 <strong>任意顺序</strong> ，返回所有从根节点到叶子节点的路径。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>
&nbsp;

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,null,5]
<strong>输出：</strong>["1-&gt;2-&gt;5","1-&gt;3"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>["1"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

**标签:**  [树](https://leetcode.cn/tag/tree) [深度优先搜索](https://leetcode.cn/tag/depth-first-search) [字符串](https://leetcode.cn/tag/string) [回溯](https://leetcode.cn/tag/backtracking) [二叉树](https://leetcode.cn/tag/binary-tree) 