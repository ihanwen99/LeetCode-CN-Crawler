| English | [简体中文](README.md) |

# [606. Construct String from Binary Tree](https://leetcode-cn.com/problems/construct-string-from-binary-tree)
 ### Description
<p>You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.</p>

<p>The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

<b>Output:</b> "1(2(4))(3)"
<br/><b>Explanation:</b> Originallay it needs to be "1(2(4)())(3()())", <br/>but you need to omit all the unnecessary empty parenthesis pairs. <br/>And it will be "1(2(4))(3)".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

<b>Output:</b> "1(2()(4))(3)"
<br/><b>Explanation:</b> Almost the same as the first example, <br/>except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
</pre>
</p>
**Related Topics	**[Tree](https://leetcode-cn.com/tag/tree) [String](https://leetcode-cn.com/tag/string) 

### Similar Questions
 - Medium:	[Construct Binary Tree from String](https://leetcode-cn.com/problems/construct-binary-tree-from-string) 
 - Medium:	[Find Duplicate Subtrees](https://leetcode-cn.com/problems/find-duplicate-subtrees) 
