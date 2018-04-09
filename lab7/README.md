<h2>Assignment</h2>
<ol>
<li>Write a function that will calculate and approximation of the definite integral of an arbitrary function using a Reimann sum.  The function should be in a file called<span> </span><code>integrate.py</code>, and look like this:
<blockquote><code>i = integrate(f, a, b)</code></blockquote>
This should return the definite integral of the function f, from a to b.  You should also give the function an optional argument that allows the caller to specify the number of the intervals used to calculate the integral:
<blockquote><code>i = integrate(f, a, b, 100)</code></blockquote>
</li>
<li>Write a second function that calculates the definite integral using Monte Carlo integration:
<blockquote><code>i = integrate_mc(f, a, b, (c, d), 1000)</code></blockquote>
Where f is the function, <span style="font-family: monospace;"><span style="font-size: 13px;">a</span></span> and <span style="font-family: monospace;"><span style="font-size: 13px;">b</span></span> are the bounds of the definite integral, <code>(c, d)</code> is a tuple such that <code>c</code> is lower than the lowest value of <code>f</code> over the interval [<code>a</code>, <code>b</code>] and <code>d</code> is larger than the largest value over the interval.  The last argument should be the number of Monte Carlo samples used in the approximation.<br><br>
</li>
<li>Pick a function and a definite integral range.  Calculate the definite integral by hand.  Plot the absolute error in the approximations of your two functions as a function of the number of intervals and the number of samples.<br><br>
</li>
<li>Write another function,<span> </span><code>approximate_pi(n)</code>, that approximates pi using Monte Carlo sampling.  The parameter n should specify the number of samples to use.  Use the technique we talked about in class: sample over the square that spans -1 to 1, and see what proportion of points lie within the unit circle, which has an area of pi.  The function should return the approximation.</li>
<li>
</li>
</ol>
<h2>Thoughts</h2>
<ol>
<li>You should use a<span> <a href="https://en.wikipedia.org/wiki/Riemann_sum">Riemann sum</a></span><span> </span>to calculate the definite integral in the first question. There are several flavors of this, and you're free to pick any of them.  We talked about this technique briefly in class.<br><br>
</li>
<li>You should use<span> </span><a href="https://en.wikipedia.org/wiki/Monte_Carlo_integration"><span>Monte Carlo integration</span></a><span> </span>for calculate the definite integral in the second question.  Again, there are several ways to do this, and you're free to pick the one you want. I'd advise starting with a simple one, using<span> </span><a href="https://en.wikipedia.org/wiki/Rejection_sampling"><span>rejection sampling</span></a>.  The basic idea of this is to generate a sample point within the bounding box of the area (using the <code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>).  Count the number of times that this point lies within the area. The proportion of points that end up inside then lets you calculate the area, based on the area of the bounding box.  We talked about this briefly in class.</li>
</ol>
<h1>Grading</h1>
<ol>
<li>An Riemann sum integration function that works (1 point), is robust to bad arguments (1 point), and returns the correct answer (2 points). [4 points total]</li>
<li>A Monte Carlo integration functiom that works (1 point), is robust to bad arguments (1 point), and returns the correct answer (2 points). [4 points total]</li>
<li>A graph with appropriate labels and title (1 point) that shows the convergence behavior of the two functions (1 point).  [2 points total]</li>
<li>A function that correctly approximates pi (2 points).  [2 points total]</li>
</ol>
<h2>What to Hand In</h2>
<p>Hand in a single file, called <code>integrate.py</code>, with all of your code in it.  We will import this file for our testing.  We should be able to generate your graphs by running the file as an executable.</p>
<h1>The Rules</h1>
<p>Everything you do for this lab should be your own work. Don't look up the answers on the web, or copy them from any other source. You can look up general information about Python on the web, but no copying code you find there. Read the code, close the browser, then write your own code.</p>
