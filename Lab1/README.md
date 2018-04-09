<h1>Purpose</h1>
<p><span>The main purpose of this lab is to give you some experience writing and testing functions in Python.  These functions might not be very exciting, but knowing how to write and test functions is a skill you'll use over and over again during your Python programming career.</span></p>
<h1> </h1>
<h1>Assignment</h1>
<ol>
<li>We're going to start by taking the code you wrote for calculating the volume of a cylinder and putting it into a function, so that you can reuse it.  Create a file called<span> </span><code>volumes.py</code>, and write a function called<span> </span><code>cylinder_volume</code><span> </span>that takes a radius and a height (in that order) and returns the volume of the corresponding cylinder.  In addition to the function, you should write some code to test that the function is returning the correct values. This can be done by printing the value returned by your function for arguments that you define. This code should go after the<span> </span><code>if __name__ == '__main__':</code>line (which the TAs will explain at the start of the lab).<br><br>
</li>
<li>Modify your code so that it deals correctly with arguments that are incorrect.  For volume calculations, this basically means negative values.  If you get bad function arguments, then the function should return<span> </span><code>None</code>. <br><br>
</li>
<li>Do the same for the torus code, putting it in the same file, in a function called torus_volume, which takes the major radius and minor radius (in that order) as arguments. The volume to use for the torus is the simple one (whatever pops up on google first).<span> </span><br><br>
</li>
<li>Write a function called<span> </span><code>close</code><span> </span>in a file<span> </span><code>close.py</code>, that takes three numbers as arguments.  It returns<span> </span><code>True</code><span> </span>if the absolute difference between the first two numbers is less than the third number.  For example<span> </span><code>close(1, 2, 0.5)</code><span> </span>would return<span> </span><code>False</code>, but<span> </span><code>close(1, 2, 3)</code><span> </span>would return<span> </span><code>True</code>.<br><br>
</li>
<li>Write a function called<span> </span><code>letter_count</code><span> </span>in a file<span> </span><code>words.py</code><span> </span>that takes two string arguments.  The first string is a bunch of text, and the second is a letter.  The function returns the number of occurrences of the letter in the text. Your function should be case insensitive, that is: halLway should return 2 for ('halLway','l') and ('halLway','L').</li>
</ol>
<h1><span>Grading</span></h1>
<p><span>You will be graded for showing the TA the following things.  Each of the following will get equal weight in your grade:</span></p>
<ol>
<li>
<p>A cylinder volume function that works on valid inputs.</p>
</li>
<li>
<p>A cylinder volume function that deals with invalid inputs appropriately.</p>
</li>
<li>
<p>A torus volume function that works on valid inputs.</p>
</li>
<li>
<p>A torus <span>volume function that deals with invalid inputs appropriately.</span></p>
</li>
<li>
<p><span></span>A working<span> </span><code>close</code><span> </span>function.</p>
</li>
<li>
<span>A working letter-counting function.</span> </li>
</ol>
<h1>What to Hand In</h1>
<p>Submit a zip or tar file of the code you write.  You don't need to submit any of the other files, just to ones that you wrote.</p>
<h1>Thoughts</h1>
<ol>
<li>You should the Python value of pi in this lab. Use either<span> </span><code>import math</code><span> </span>or<span> </span><code>from math import pi</code>.<br><br>
</li>
<li>We're going to be sticklers with grading for this lab.  If your code doesn't run, or gives the wrong answer, you'll end up getting zero points for it.  This might seem harsh, but we're trying to reinforce the importance of writing to a particular specification. <br><br>
</li>
<li>We haven't really talked about strings or for loops yet.  However, you should be able to work out the syntax from the following example function, which prints out the characters in a string, one per line.  You'll probably want to use a for loop in your answer to the last question.
<blockquote><code>def foo(t):<br>    for c in t:<br>        print c</code></blockquote>
</li>
<li>For all of the code you write for this lab, you should write your own testing code to try to make sure that the functions do the right thing.  We're going to talk more about writing testing code during lecture, but you should try to think of some test cases for each of your functions, and write code to make sure that they do the right thing. </li>
</ol>
<p>Everything you do for this lab should be your own work. Don't look up the answers on the web, or copy them from any other source. You can look up general information about Python on the web, but no copying code you find there. Read the code, close the browser, then write your own code.</p>
