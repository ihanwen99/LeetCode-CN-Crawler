| English | [简体中文](README.md) |

# [917. Reverse Only Letters](https://leetcode.cn/problems/reverse-only-letters)
 ### Description
<p>Given a string <code>s</code>, reverse the string according to the following rules:</p>

<ul>
	<li>All the characters that are not English letters remain in the same position.</li>
	<li>All the English letters (lowercase or uppercase) should be reversed.</li>
</ul>

<p>Return <code>s</code><em> after reversing it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ab-cd"
<strong>Output:</strong> "dc-ba"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a-bC-dEf-ghIj"
<strong>Output:</strong> "j-Ih-gfE-dCba"
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "Test1ng-Leet=code-Q!"
<strong>Output:</strong> "Qedo1ct-eeLg=ntse-T!"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of characters with ASCII values in the range <code>[33, 122]</code>.</li>
	<li><code>s</code> does not contain <code>&#39;\&quot;&#39;</code> or <code>&#39;\\&#39;</code>.</li>
</ul>

**Related Topics**  [Two Pointers](https://leetcode.cn/tag/two-pointers) [String](https://leetcode.cn/tag/string) 