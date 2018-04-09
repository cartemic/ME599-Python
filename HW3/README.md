<h2>Assignment</h2>
<ol>
<li>Make sure that your code from homework 2 is working as expected, or use ours (in the Homework 3 section of Files).  Then, make sure that our testing harness (in the file tester.py) is doing the right thing.  It should all work with the files that are there, but you should verify that it works with your code.  Please don't change tester.py, since we will be using our own version of this code.  If you can't make things work by modifying your own code, then let us know.</li>
<li>Write a function, called optimize, and put it in a file called optimize.py.  This function should find the set of waypoints with the lowest possible cost.  The function should have the same structure as the one in our example code, with a while loop that terminates when the done() function returns True.  This will let us test this more easily with our own code.</li>
</ol>
<h2>Thoughts</h2>
<ol>
<li>For this lab, all waypoints should be on the playing board, between (-10, 10) and (10, 10).  Any waypoints outside of this range will result in zero points for that solution.<br><br>
</li>
<li>You're welcome (and actually encouraged) to try any tricks you like to get better results out of our code.  You shouldn't try to pick apart the executable that does the simulation, since we want you to treat that as a blob of code that you have no insight into.  However, other tricks, like parallelizing your code, are fair game.  We will evaluate your code on a workstation-class computer, and you can assume that it has more than one core available for use.<br><br>
</li>
<li>You will be able to get (close to) full points for this homework by coming up with a solution that is better than our reference solution (from the Files section of Canvas).  We will give you one point for simply submitting this reference solution with everything working as expected.<br><br>
</li>
<li>We should be able to run your code from our computer.  This means that you cannot have any hard-coded absolute pathnames (/home/smartw/src, /tmp, or similar).  You can assume that the simulators are in the same directory as tester.py.</li>
</ol>
<h2>Grading</h2>
<p>You can get one point for simply handing in the code that we gave you, making sure things run as expected.  Grading after that will depend on how well you perform the optimization, relative to our reference solutions.  Doing as well as the basic reference solution on Canvas will get you 1 point.  Doing better will get you more points.  Your grade will be determined by the following graph:</p>
<p><img src="/courses/1659540/files/70270954/preview?verifier=2WEbSiKCKlzFW7zRVZDcLVWSQH1mmmXjQoUC9SXH" alt="Screenshot from 2018-03-12 16-27-09.png" width="640" height="542"></p>
<p>If you do no better than the basic reference solution (0) you get one point.  If you do as well as the best reference solution (which we will release shortly), then you get close to 12 points.  If you get about 60% of the way from the basic solution to the best reference, then you get 10 points (full points for the lab).</p>
<h2>What to Turn In</h2>
<p>A single file, called optimizer.py, with a function called optimize in it.  This should run without problems in our testing code.  Tell us in the comments if you need us to install anything exotic.</p>
