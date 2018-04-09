<h2>Purpose</h2>
<p>The goal of this lab is to give you more practice with writing Python code that deals with files and large data sets.  In particular, you should use the files <a class="instructure_file_link instructure_scribd_file" title="war_and_peace.txt" href="/courses/1659540/files/69851666/download?verifier=opDvg9UcZiarotv3rwxEMkTGteTpshQyPCpQKgrY&amp;wrap=1">war_and_peace.txt</a> and <a class="instructure_file_link instructure_scribd_file" title="words.txt" href="/courses/1659540/files/69851665/download?verifier=L61BpLkimegppukb0CTDnoScibaTNWXxFc0Z7eiS&amp;wrap=1">words.txt</a> for this lab.</p>
<h2>Assignment</h2>
<ol>
<li>Write some code that takes two command-line arguments, and prints them out.  We haven't talked about this before, but you might find <a href="http://www.pythonforbeginners.com/system/python-sys-argv">this page</a> useful.  Make your code idiot-proof by checking that the code is passed exactly two arguments, and exit with some helpful text if this isn't the case. Put your code in a file called <code>compare.py</code>, and verify that it has a behavior like this:
<blockquote><code>python compare.py foo bar<br>foo<br>bar</code></blockquote>
</li>
<li>Now, modify your code to take two filenames, and print out the number of words in each of the files.  We'll leave the choice of data structures up to you, but you should report the total number of words in each file.
<blockquote><code>python compare.py war_and_peace.txt words.txt<br>war_and_peace.txt:<br>  234 words<br>words.txt:<br>  432 words</code></blockquote>
</li>
<li>Modify your code to also print out the number of unique words for each file.  For the purposes of this lab, "a" and "A" are considered to be the same word (ie, you should be case insensitive).  There is a hard way to do this, and an easy way.  You should read about <a href="https://docs.python.org/2/library/functions.html#func-set">set()</a> before you implement this.  Also, words should contain no punctuation.
<blockquote><code>python compare.py war_and_peace.txt words.txt<br>war_and_peace.txt:<br>  234 words<br>  unique: 12<br>words.txt:<br>  432 words<br>  unique: 15</code></blockquote>
</li>
<li>Modify your code to also print out the number of words in each file that are not in the other, and the number of words that are in both files.
<blockquote><code>python compare.py war_and_peace.txt words.txt<br>war_and_peace.txt:<br>  234 words<br>  unique: 12<br>words.txt:<br>  432 words<br>  unique: 15<br>Only war_and_peace.txt: 54<br>Only words.txt: 44<br>Both files: 54</code></blockquote>
</li>
</ol>
<h2>What to Hand In</h2>
<p>A single file, called <code>compare.py</code> that outputs the information above in the exact same format as this file. Pay attention to new lines and spaces. Obviously, the numbers will be different.  Note that we might run your code on different files; the filenames you print should be the ones we give you.</p>
<h2>Grading</h2>
<ol>
<li>Command line arguments work (1 point) and guard against bad inputs (1 point).  [2 points total]</li>
<li>Files read into code correctly (1 point), correct number of words (1 point), and check to make sure the file exists (1 point).  [3 points total]</li>
<li>Case insensitive (1 point), punctuation removed (1 point) and correct number of unique words (1 point).  [3 points total]</li>
<li>Correct values for three classes of words (1 point each).  [3 points total]</li>
<li>Code runs in under 10 seconds.  [1 point]</li>
</ol>
