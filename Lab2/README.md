<h2>Purpose</h2>
<p>The goal of this lab is to give you some more experience writing functions and trying to decompose problems in different ways.</p>
<h2>Preparation</h2>
<p>Create a new project called <code>lab2</code> and do all of your work in there.</p>
<h2>Assignment</h2>
<ol>
<li>Write a function called <code>sum_i</code> that takes a list of numbers as its argument, and returns the sum of all the numbers in the list.  You should calculate the sum using a<span> </span><code>for</code><span> </span>loop. Do not use the built-in<span> </span><code>sum</code><span> </span>function (although that's the right thing to do). Put this function in a file called<span> </span><code>sum.py</code>. We should be able to call this function with <code>s = sum_i(l)</code><br><br>
</li>
<li>Write another function in the<span> </span><code>sum.py</code><span> </span>file called<span> </span><code>sum_r</code><span> </span>that calculates the sum recursively. We should be able to call this function with <code>s = sum_r(l)</code><br><br>
</li>
<li>Write two functions, one recursive and the other iterative, that reverse the order of a list.  The functions should be called<span> </span><code>reverse_r</code><span> </span>and<span> </span><code>reverse_i</code>, take a list as an argument and return a list, and be in a file called<span> </span><code>reverse.py</code>. We should be able to call this function with <code>l2 = reverse_i(l1)</code><br><br>
</li>
<li>Do exercise 8 from chapter 6 in the book.  Call the function<span> </span><code>gcd</code><span> </span>and put it in<span> </span><code>gcd.py</code>.<br><br>
</li>
<li>Do exercise 5 from chapter 7 in the book.  Put the function in<span> </span><code>estimate_pi.py</code>.<br><br>
</li>
<li>Get a copy of <a class="instructure_file_link instructure_scribd_file" title="sensor.py" href="/courses/1659540/files/69694658/download?verifier=FhUbndXJeXMRtYKd8DvemVBxvxV4I0iMafXWi7TI&amp;wrap=1">sensor.py</a> and <a class="instructure_file_link instructure_scribd_file" title="null_filter.py" href="/courses/1659540/files/69694659/download?verifier=unZ2d266TgJa1QmN46IqgqIZcbozLN3RoAzJqNDe&amp;wrap=1">null_filter.py</a>. Read them, and make sure you understand what they're doing.  Write some code to generate a file of (simulated) sensor data by running null_filter.py, and have a look at it with your favorite plotting program. Notice that it's noisy. This is meant to simulate the (zero-mean gaussian) measurement noise of a sensor. Note that you should not edit either file; <code>import</code> them into your own code in another file.<br><br>
</li>
<li>Write a new filter, called <code>mean_filter</code> in<span> </span><code>filters.py </code>that replaces each sensor reading with the mean of itself and the readings on either side of itself. For example, if you have these measurements in the middle of the list<br><br>
<blockquote>10 13 13</blockquote>
then the middle reading would be replace by 12 (since (10 + 13 + 13) / 3 = 12). Generate two files, one for the data before filtering, and one for the filtered data. Plot both of these to make sure you're doing the right thing. We should be able to call your function with <code>l2 = mean_filter(l1)</code>
<ol></ol>
</li>
<li>
<p>Modify your code to have a variable filter width. Instead of a width of 3, add a parameter to the filter function that specifies the filter width.  This parameter must be positive and odd. Test this with a variety of widths, and see what it does to the data. We should be able to call your code with <code>l2 = mean_filter(l1, 5)</code></p>
</li>
<li>
<p>Write a variable-width median filter. This is like the mean filter that you just wrote, except that it replaces the values with the<span> </span><em>median</em><span> </span>of the values, rather than the mean. Write this filter in <code>filters.py</code>, and call it <code>median_filter</code></p>
</li>
</ol>
<h2>Grading</h2>
<p>One point for code that generates no errors.  One point for each of the six functions in the first five questions.  Two points for the mean function.  Two points for the variable-width mean function.  One point for the median function.</p>
<h2>Submission</h2>
<p> </p>
<p>Submit a single file with all of your code in it.  Zip or tar files are probably your best bets.</p>
<h2>Thoughts</h2>
<ol>
<li>You should write tests for all of the functions you write for this lab.  Write the tests before you write the code.  Put them after the <code>if __name__ ==
 '__main__':</code> line. We're going to import the functions from your files for automated testing and, if you don't put your tests after this line, then it might confuse our testing code (and you'll lose a point for "no errors")<br><br>
</li>
<li>Yes, we wrote the sum functions in class (more or less) last week.<br><br>
</li>
<li>There are number of ways to write the recursive function.  Any of them will do.<br><br>
</li>
<li>The null filter doesn't actually do anything to the sensor readings. It's really just to show you how you might write a filter for a list of sensor values. Don't worry if you don't understand the stuff in<span> </span><code>sensor.py</code>; we'll cover that in class soon. All you really need to know is that it generates a list of sensor measurements for a fictional sensor.<br><br>
</li>
<li>You might find this code useful, to associate list positions with values for the mean and median code:<br><br>
<blockquote><code>for i,datum in enumerate(data)<br>    print i, datum</code></blockquote>
<ol></ol>
</li>
<li>
<p>The data from the mean filter will have two fewer measurements than the original data set, because the mean of the first and last elements is not well-defined. Don't worry about this.</p>
</li>
<li>
<p><code>numpy</code><span> </span>contains a useful set of functions. Google knows about it.</p>
</li>
<li>We're not initially giving you a grading script for this lab, to encourage you to write you own tests.  When you're writing tests, you should make sure you have a source of the correct input/output pairs (either a built-in function, or something you've verified by hand), and should test your code against this known answer. For the sum functions, this is easy, since there's a built-in function that does the same thing.  For calculating pi, you could verify that you're close to it after the function is done.</li>
</ol>
