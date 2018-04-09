<h2>Purpose</h2>
<p>The main aim of this lab is to get you to write some simple optimization code, and to use some of the python skills you've learned up to this point.</p>
<h2>Assignment</h2>
<ol>
<li>Write a funtion, called <code>optimize_step</code>, the finds the largest value of a function, between a set of bounds when called like this:
<blockquote><code>x = optimize_step(f, bounds, n)</code></blockquote>
where <code>f</code> is the function, <code>bounds</code> is a tuple specifying the lower and upper bounds, and <code>n</code> is the number of steps. This function should start at the lower bound, and take n evenly-spaced evaluations of f, returning the x value of the largest one.<br><br>
</li>
<li>Write another function, <code>optimize_random</code> that takes the same arguments, but uses n random samples between the bounds.<br><br>
</li>
<li>Write a third function, <code>optimize_gradient(f, bounds, epsilon)</code>, that uses gradient ascent to find the largest value.  This function should pick some x value between the bounds, and follow the gradient of the function to the maximum.  Stop when you get close to the maximum (improvement after a single step is less than epsilon)<br><br>
</li>
<li>Compare the accuracy of your three functions and the Python optimization function we talked about in class, on a couple of different functions.  Graph the performance of the four approaches as a function of the number of function evaluations you make.  This is slightly trickier with part 3, but it is possible.<br><br>
</li>
<li>Write a final function, <code>optimize_md</code>, that optimizes a multidimensional function.  Given a function that looks like:<code>def f(x, y, z):</code> you should be able to call your function like this:<code>x = optimize_md(f, bounds)</code>.  The function should return a tuple corresponding the the maximal point.  In the 3D example here, what might be <code>(1.2, 2.2, 3.1)</code>.  The argument bounds should be a list of tuples, each tuple being the bounds along a single axis.  For example
<blockquote><code>def f(a, b, c, d):<br>  ... some code ...<br><br>print optimize_md(f, [(-1, 1), (-2, 2), (2, 4), (0, 2)])<br>(0.4, 1.3, 1, 1)</code></blockquote>
</li>
</ol>
<h2>Grading</h2>
<ol>
<li>Stepwise function works (1 point) and returns correct value (1 point).  [2 points total]</li>
<li>Random function works (1 point) and returns correct value (1 point). [2 points total]</li>
<li>Gradient function works (1 point), implements gradient correctly (1 point), stops correctly (1 point), and returns correct value (1 point).  [4 points total]</li>
<li>Code generates appropriate graphs.  [2 points total]</li>
<li>Multi-dimensional optimizer works (1 point) and returns correct value (1 point). [2 points total]</li>
</ol>
<h2>What to Turn In</h2>
<p>A single file, called <code>optimize.py</code> that, when run displays your graphs, and contains the functions described above.</p>
