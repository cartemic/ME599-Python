<h2>Purpose</h2>
<p>The goal of this homework is to get you to use some of the Python skills you've developed in the labs.  Unlike the labs, we're not going to tell you <em>how</em> to do things, just <em>what</em> to do.  You should apply the techniques and approaches we've talked about in class, and the things you've learned in the labs to answer the questions that we pose in the homework.</p>
<p>If you can find code on the Internet that solves parts of these problems, then that's fine.  Just make sure to cite your sources, and make sure that the code does what you think it does.  If you use code that's not part of Python, then you need to include this in your submission, otherwise we won't have it.  Also, if you install any additional Python modules, then tell us about this, so that we can install them too.</p>
<p>As with everything in the class, if you have any questions, or anything is unclear, then ask for clarification.</p>
<h2>Assignment</h2>
<ol>
<li>Grab a copy of <a class="instructure_file_link instructure_scribd_file" title="grades.csv" href="/courses/1659540/files/69803067/download?verifier=VwGv9GiEEIkUEcpcGHCaZHTae4DyaeuT1fYblR0z&amp;wrap=1">grades.csv</a>.  This is a file with anonymous grade data from a previous incarnation of ENGR 112.  We're going to ask you some questions about these data; you should write Python code to answer these questions.  You are not allowed to edit this file.  If you do, we will replace it with the original version when we grade your code.<br><br>
</li>
<li>What's the average final score in the class?  How many students are above average?  What about median score?  Your code should output information in (exactly) this format:
<blockquote><code>Average Score: 45.34<br>Above Average: 23.34%<br>Median Score: 23.31<br>Above Median: 65.34%<br></code></blockquote>
Two decimal places.  These example numbers are wrong (obviously).</li>
<li>What was the hardest assignment overall?  We'll call the hardest assignment the one with the lowest average score.  Remember that assignments are worth different amounts of points.  Assume that the lowest possible score is zero, and that someone always gets the maximum possible score.
<blockquote><code>Hardest Assignment: Blah</code></blockquote>
</li>
<li>What was the hardest Lab?  A lab is something with the word "lab" in the title of the column.
<blockquote><code>Hardest Lab: Blah</code></blockquote>
</li>
<li>
<p>If we assume the <a href="https://s3.amazonaws.com/screensteps_live/image_assets/assets/000/790/764/original/18963ceb-edd3-46ca-b16e-efa3755b2b9f.png">usual grading scheme</a>, How many students get each grade?</p>
<blockquote><code>A  12<br>A- 23<br>B+  32<br>...and so on<br></code></blockquote>
</li>
<li>How many students will complain to us about their grade?  A student will compain if they are within 0.5% of getting a higher grade.  Students will only complain about their grades if they want them to go up, not if they want them to go down.
<blockquote><code>23 students will complain about their grade.</code></blockquote>
</li>
<li>If we instead want only to assign A, B, C, D, and F, what are the grade cutoffs for each letter grade if we want 10% of students to get an A, 20% to get a B, 30% to get a C, 30% to get a D, and the rest to get an F?
<blockquote><code>A  95.34<br>B  54.43<br>C 34.34<br>D  12.23</code></blockquote>
</li>
</ol>
<h2>Grading</h2>
<ol>
<li>Reading in the CSV file correctly.  [1 point]</li>
<li>Calculating the 4 numbers correctly, 1 point each [4 points]</li>
<li>Correct assignment, 2 points [2 points]</li>
<li>Correct lab, 2 points [2 points]</li>
<li>Correct grade assignment, 2 points [2 points]</li>
<li>Correct number of complaints, 3 points [3 points]</li>
<li>Correct thresholds, 3 points [3 points]</li>
</ol>
<p>For a total of 17 points on offer.</p>
<h2>What to Hand In</h2>
<p>Zip or tar up your files and submit them on Canvas.  Include a file called README that tells us what additional stuff we need to include, and anything else we need to know about your code.  Your code should be in a file called hw1.py, which we will run.  If that file doesn't run, or is missing, then you don't get any points.</p>
<h2>Thoughts</h2>
<ol>
<li>There are no instructions on how to structure your code here.  That's on purpose.  You should encapsulate things in functions it makes sense.  One function (at least) per question is a reasonable starting place.  That way, it'll be easy for us to find the code we want to look at.<br><br>
</li>
<li>We will run your code on another CSV file that is similar to, but not the same as, the one we gave you.  If you calcuate the answers using some other method (in Excel, for example) and just have your code print them out, or hard-code the number of lines in the file, then you will lose points.  You should write your code to deal with files that are similar to the example, but with different values in their cells.</li>
</ol>
