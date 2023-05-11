| English | [简体中文](README.md) |

# [面试题 17.07. Baby Names LCCI](https://leetcode.cn/problems/baby-names-lcci)
 ### Description
<p>Each year, the government releases a list of the 10000 most common baby names and their frequencies (the number of babies with that name). The only problem with this is that some names have multiple spellings. For example,&quot;John&quot; and &#39;&#39;Jon&quot; are essentially the same name but would be listed separately in the list. Given two lists, one of names/frequencies and the other of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and Johnny are synonyms. (It is both transitive and symmetric.) In the final list, choose the name that are <strong>lexicographically smallest</strong> as the &quot;real&quot; name.</p>

<p><strong>Example: </strong></p>

<pre>
<strong>Input: </strong>names = [&quot;John(15)&quot;,&quot;Jon(12)&quot;,&quot;Chris(13)&quot;,&quot;Kris(4)&quot;,&quot;Christopher(19)&quot;], synonyms = [&quot;(Jon,John)&quot;,&quot;(John,Johnny)&quot;,&quot;(Chris,Kris)&quot;,&quot;(Chris,Christopher)&quot;]
<strong>Output: </strong>[&quot;John(27)&quot;,&quot;Chris(36)&quot;]</pre>

<p>Note:</p>

<ul>
	<li><code>names.length &lt;= 100000</code></li>
</ul>

**Related Topics**  [Depth-First Search](https://leetcode.cn/tag/depth-first-search) [Breadth-First Search](https://leetcode.cn/tag/breadth-first-search) [Union Find](https://leetcode.cn/tag/union-find) [Array](https://leetcode.cn/tag/array) [Hash Table](https://leetcode.cn/tag/hash-table) [String](https://leetcode.cn/tag/string) [Counting](https://leetcode.cn/tag/counting) 