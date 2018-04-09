<h2>Preparation</h2>
<p>Make sure your code from the previous lab works.  If it doesn't then grab a copy of our reference solution from the Files section of Canvas.  You should write test code for all of the code you write for this lab.  This test code can build on the example we give below.  We will use our own similar testing harness when we evaluate your code.</p>
<h2>Assignment</h2>
<ol>
<li>Ensure we can get at the real and imaginary components of your Complex class like this:
<blockquote><code>c = Complex(1.2, 3.4)<br>print c.im<br>print c.re</code></blockquote>
</li>
<li>Implement addition, such that the following works:
<blockquote><code>a = Complex(1, 2)<br>b = Complex(3, 4)<br>print a + b<br>print a + 1<br>print 1 + a<br></code></blockquote>
and prints out<br>
<blockquote><code>(4 + 6i)<br>(2 + 2i)<br>(2 + 2i)<br></code></blockquote>
Once you have addition working, implement subtraction. This should look a lot like addition.<br><br>
</li>
<li>Now, implement multiplication and division. Verify that everything works as expected.<br><br>
</li>
<li>Finally, implement negation and the complex conjugate:<br>
<blockquote><code>a = Complex(1, 2)<br>print -a<br>print ~a<br></code></blockquote>
should print out<br>
<blockquote><code>(-1 - 2i)<br>(1 - 2i)</code></blockquote>
</li>
<li>OK. Let's use your new class. Write a new function, in a file called roots.py, that calculates the roots of a quadratic function. You should call it like this:
<blockquote><code>roots(1, 2, 3)     # This is x^2 + 2x + 3<br></code></blockquote>
<p>and it should return a list of all of the roots of the function. Sometimes these will be real numbers, sometimes they will be complex.  You should return a tuple containing all the roots you find.</p>
</li>
</ol>
<h2>Grading</h2>
<p>We will grade your code for giving the same results as the built-in complex class.  If you use the built-in class in your implementation of Complex, then you'll get zero points for the whole assignment.  You can, however, use it in your testing code.  We will test your code with something like this: <a class="instructure_file_link instructure_scribd_file" title="complex-test.py" href="/courses/1659540/files/70020802/download?verifier=NyCPa8l8mUAcoYxwv6ASSR4ltBNbEhNBj0LyTILU&amp;wrap=1" data-api-endpoint="https://oregonstate.instructure.com/api/v1/courses/1659540/files/70020802" data-api-returntype="File">complex-test.py</a></p>
<ol>
<li>Testing code for all cases.  [1 point total]</li>
<li>Addition works: two complex numbers (1 point); one complex and one integer or float (1 point); one integer or float and one complex number (1 point).  [3 points total]</li>
<li>Subtraction works for all three cases (like addition).  [1 point total]</li>
<li>Multiplication works for all three cases (like addition).  [1 point total]</li>
<li>Division works for all three cases (like addition).  [1 point total]</li>
<li>Negation works.  [1 point total]</li>
<li>Complex conjugate works.  [1 point total]</li>
<li>Quadratic roots calcuated correctly: two real roots (1 point); one root (1 point); two complex roots (1 point).  [3 points total)</li>
</ol>
<h2>What to Hand In</h2>
<p>A zip or tar file of your code: complex.py, roots.py, and any testing code.</p>
