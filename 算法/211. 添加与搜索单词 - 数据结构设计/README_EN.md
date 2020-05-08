| English | [简体中文](README.md) |

# [211. Add and Search Word - Data structure design](https://leetcode-cn.com/problems/add-and-search-word-data-structure-design)
 ### Description
<p>Design a data structure that supports the following two operations:</p>

<pre>
void addWord(word)
bool search(word)
</pre>

<p>search(word) can search a literal word or a regular expression string containing only letters <code>a-z</code> or <code>.</code>. A <code>.</code> means it can represent any one letter.</p>

<p><strong>Example:</strong></p>

<pre>
addWord(&quot;bad&quot;)
addWord(&quot;dad&quot;)
addWord(&quot;mad&quot;)
search(&quot;pad&quot;) -&gt; false
search(&quot;bad&quot;) -&gt; true
search(&quot;.ad&quot;) -&gt; true
search(&quot;b..&quot;) -&gt; true
</pre>

<p><b>Note:</b><br />
You may assume that all words are consist of lowercase letters <code>a-z</code>.</p>

**Related Topics	**[Design](https://leetcode-cn.com/tag/design) [Trie](https://leetcode-cn.com/tag/trie) [Backtracking](https://leetcode-cn.com/tag/backtracking) 

### Similar Questions
 - Medium:	[Implement Trie (Prefix Tree)](https://leetcode-cn.com/problems/implement-trie-prefix-tree) 
 - Hard:	[Prefix and Suffix Search](https://leetcode-cn.com/problems/prefix-and-suffix-search) 
