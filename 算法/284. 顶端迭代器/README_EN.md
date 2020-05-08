| English | [简体中文](README.md) |

# [284. Peeking Iterator](https://leetcode-cn.com/problems/peeking-iterator)
 ### Description
<p>Given an Iterator class interface with methods: <code>next()</code> and <code>hasNext()</code>, design and implement a PeekingIterator that support the <code>peek()</code> operation -- it essentially peek() at the element that will be returned by the next call to next().</p>

<p><strong>Example:</strong></p>

<pre>
Assume that the iterator is initialized to the beginning of the list: <strong><code>[1,2,3]</code></strong>.

Call <strong><code>next()</code></strong> gets you <strong>1</strong>, the first element in the list.
Now you call <strong><code>peek()</code></strong> and it returns <strong>2</strong>, the next element. Calling <strong><code>next()</code></strong> after that <i><b>still</b></i> return <strong>2</strong>. 
You call <strong><code>next()</code></strong> the final time and it returns <strong>3</strong>, the last element. 
Calling <strong><code>hasNext()</code></strong> after that should return <strong>false</strong>.
</pre>

<p><b>Follow up</b>: How would you extend your design to be generic and work with all types, not just integer?</p>

**Related Topic**  [Design](https://leetcode-cn.com/tag/design) 

### Similar Questions
 - Medium:	[Binary Search Tree Iterator](https://leetcode-cn.com/problems/binary-search-tree-iterator) 
 - Medium:	[Flatten 2D Vector](https://leetcode-cn.com/problems/flatten-2d-vector) 
 - Medium:	[Zigzag Iterator](https://leetcode-cn.com/problems/zigzag-iterator) 
