<h1>Purpose</h1>
<p>The goal of this lab is to introduce you to some of the plotting and graphing functions available in Python, and to give you some practice using them. We also want to get you started thinking about how long it takes to do things in Python, and how this time depends on how you implement your functions.</p>
<h1>Preparation</h1>
<p>Make sure you're familiar with the material from the previous labs.</p>
<h1>Assignment</h1>
<ol>
<li>There are a number of plotting and graphing libraries that are available in Python. We're going to focus on <span style="font-size: 13px;"><a href="https://matplotlib.org/tutorials/index.html"><span style="font-family: monospace;">matplotlib</span></a></span>, one of the most popular ones. Start off by working through the <span><a href="https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py"><code>pyplot</code></a> tutorial</span>. We're only going to scratch the surface of <code>pyplot</code> in this lab, but it's probably got most of the plotting and graphing functionality that you're likely to want (for most applications, at least).<br><br>
</li>
<li>Just to make sure that you know how to use<span> </span><code>pyplot</code>, plot a sine wave, from 0 to 4 pi. Make sure you get the x axis values right, and that you have a title and a axis labels. Your output should look like this (complete with labels):<br><br><img src="http://web.engr.oregonstate.edu/~smartw/me499/labs/lab3/sine.png" alt=""><br><br>
</li>
<li>Write a function that returns the sum of ten samples from a uniform distribution from 0 to 1. Run this function some number of times (say 10000), and store what it returns in a list. Finally, plot the values in this list as a histogram. The distribution should be normal, but the y values will not be from 0-1. Add a title and axes labels.<br><br>
</li>
<li>Look at the code in<span> <a class="instructure_file_link instructure_scribd_file" title="msd.py" href="/courses/1659540/files/69772217/download?verifier=z9zIfqsCjQ3vizZGSShurlkrQVxLbu3tUOoHFCNz&amp;wrap=1">msd.py</a></span>. This simulates a mass-spring-damper system, using the ODE integrator that is part of the<span> </span><code>scipy</code><span> </span>scientific python package. Don't worry if you can't completely understand what's going on right now, since the code involves a class and some fancy lamdba function stuff; we'll talk about it in class. For now, all you need to know is that you initialize the simulation with a line like:<br><br>
<blockquote><code>smd = MassSpringDamper(1.0, 2.0, 3.0)</code></blockquote>
where the three parameters are the mass, the spring constant, and the damping factor. Once you've done this, run the simulation with the<span> </span><code>simulate</code><span> </span>function, as shown in the example file. This will return the states that the system went through, and the corresponding timesteps (in <code>state</code><span> </span>and<span> </span><code>t</code><span> </span>variables, respectively). Take a look at these: state is a list, where each element is itself a list of length 2, representing the position and velocity of the mass at a given time. It doesn't matter what mass, spring constant, or damping factor you use, just as long as the plot makes sense (because I'm sure you remember how a spring-mass system works, right?).<br><br>Plot the displacement of the mass over time, using<span> </span><code>pyplot</code>.<br><br>
</li>
<li>Generate a plot of how long it takes to sort a lists of varying lengths with the built-in list<span> </span><code>sorted</code><span> </span>function. The numbers in the lists should be randomly generated. Show results for lists of length 1, 10, 100, 1,000, 10,000, 100,000, and 1,000,000.<br><br>Also plot the time taken to sum the elements of these arrays, using the<span> </span><code>sum</code><span> </span>function.  For both of these, make sure you count only the time taken to do the sorting, not the time taken to generate the lists.</li>
</ol>
<p> </p>
<h1>Grading</h1>
<p>There are 12 points available for this lab.  You should include a file called<span> </span><code>lab3.py</code>; that generates all of the graphs. Put the actual code for each part in it's own file(s), and<span> </span><code>import</code><span> </span>the important stuff into<span> </span><code>lab3.py</code><span> </span>and run it from there.</p>
<ol>
<li>Code that generates a sine curve graph like the one above. 1 point for a plot. 1 point for the right x axis values. 1 point for labels on both axes and a title. 1 point for having the graph frame fit snugly around the sine curve. [4 points total]<br><br>
</li>
<li>Code that generates a histogram (part 3 of this lab). 2 points for a valid histogram. 1 point for one what looks like a Normal distribution. 1 point for axis labels and a title. [4 points total]<br><br>
</li>
<li>Code that generates a plot of a simulated spring-mass-damper system. 1 point for a successful plot. 1 point for it looking right, with axis labels and a title. [2 points total]<br><br>
</li>
<li>A plot of times for<span> </span><code>sort</code><span> </span>and<span> </span><code>sum</code>. 1 point for getting the right plots. 1 point for writing down what the difference between the plots is, in the title. [2 points total]</li>
</ol>
<p> </p>
<h1>Thoughts</h1>
<ol>
<li>You might have to install some extra Python packages for this lab.  If you don't know how to do this, ask the TA in the lab session for help.<br><br>
</li>
<li>The function to return the sum of 10 samples should use the function<span> </span><code>random</code><span> </span>from the<span> </span><code>random</code><span> </span>package.<span> </span><code>from random import random</code><span> </span>will do what you want. Call the function 10 times, add up the values that it returns, and return this sum from the function. There are a bunch of ways to do this with Python; try to find one that's compact and elegant.<br><br>
</li>
<li>When showing the multiple histograms, vary the number of samples from the function you wrote, not the number of samples used to calculate the sum. Leave the original function the same, and only vary the number of times you call it and store the result.<br><br>
</li>
<li>To plot the displacement the mass, you're going to have to extract the displacements from the list of states returned by the simulation. A list comprehension might be helpful here.<br><br>
</li>
<li>For the last question, try to write as little code as possible. Use loops and functions as much as you can. Hint: there's a function in the math library called<span> </span><code>pow</code><span> </span>that calculates exponents.<span> </span><code>from math import pow</code><span> </span>will let you get to it. It returns a floating point number. If you want an integer, you can convince Python to convert with the<span> </span><code>int</code><span> </span>function.<br><br>
</li>
<li>Your times can be approximate, in the sense that you can have other stuff running on the computer and the garbage collector working.  The goal of this part of the lab is to show you how the times scale as the number of items in your list grows, not to get exact timing information.  Having said that, only time the actual sorting or summing of the code.  Don't include the time it takes to generate the code.</li>
</ol>
