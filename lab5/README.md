<h1>Purpose</h1>
<p>The goal of this lab is to introduce you to classes in Python, and to give you some practice writing them.</p>
<h1>Preparation</h1>
<p>Remind yourself about complex numbers. Read chapters 15 and 16 in the textbook.</p>
<h1>Assignment</h1>
<ol>
<li>Write a class<span> </span><code>Circle</code>, whose constructor takes a single argument, representing the radius. Put the class definition in a file called<span> </span><code>shapes.py</code>. We should be able to do
<blockquote><code>c = Circle(1.2)</code></blockquote>
</li>
<li>Write a member function, called<span> </span><code>area</code>, for the class that returns the area of the circle.  We should be able to do
<blockquote><code>a = c.area()</code></blockquote>
</li>
<li>Write a member function, called <code>diameter</code>, that returns the circle diameter. Write a member function, called <span style="font-family: monospace;"><span style="font-size: 13px;">perimeter</span></span> that returns the circumference of the circle.  We should be able to do
<blockquote><code>d = c.diameter()<br>p = c.perimeter()</code></blockquote>
</li>
<li>Write another class called <code>Rectangle</code> in the same file, that deals with rectangles.  The <code>Rectangle</code> constructor should accept two parameters: length and width, in that order.
<blockquote><code>r = Rectangle(3, 4)</code></blockquote>
Write an <code>area()</code> and <code>perimeter()</code> function for it.  You should be able to run these functions on the class just like in the example above.<br><br>
</li>
<li>Now we're going to write a class for complex numbers. Start by writing a class called<span> </span><code>Complex</code><span> </span>that takes two arguments, representing the real and imaginary parts of a complex number. Put the class definition in a file called<span> </span><code>complex.py</code>, and call the member variables<span> </span><code>re</code><span> </span>and<span> </span><code>im</code>. You should make these arguments optional, and default to something sensible if they are missing. Check that your code does the right thing in response to the following:
<blockquote><code>a = Complex(1.0, 2.3)    # 1 + 2.3i<br>b = Complex(2)           # 2 + 0i<br>c = Complex()            # 0 + 0i<br></code></blockquote>
</li>
<li>Implement the<span> </span><code>__str__()</code><span> </span>function, so that
<blockquote><code>a = Complex(1, 2)<br>b = Complex(1, -2)<br>print a<br>print b<br></code></blockquote>
works and prints out
<blockquote><code>(1 + 2i)<br>(1 - 2i)</code></blockquote>
</li>
</ol>
<h2>What to Hand In</h2>
<p>A zip or tar file of the two files you wrote.</p>
<h2>Grading</h2>
<ol>
<li>Basic Circle class: 1 point for working constructor, 1 point for checking arguments [2 points total]</li>
<li>Working functions: 1 point each [3 points total]</li>
<li>Basic Rectangle class: 1 point for working constructor, 1 point for 2 working functions [2 points total]</li>
<li>Complex class:
<ol>
<li>Working constructor: 1 for each case [3 points total]</li>
<li>__str__ works as described: 1 for simple case, 2 for more complex case [2 points total]</li>
</ol>
</li>
</ol>
<h2>Thoughts</h2>
<ol>
<li>Each of the functions should be a member function of the class.</li>
<li>Think about what member variables you need for each class, and how you're going to set them.  What do you need to remember for each class in order to calculate everything you need to know about it.<br><br>
</li>
<li>Don't forget that every class function needs a <code>self</code> argument, and that every class variable has to have <code>self.</code> prepended to it.<br><br>
</li>
<li>There's a built-in complex number class that you can import.  Don't use it.  Write this one from scratch.  However, you can use the built-in class to test yours.<br><br>
</li>
<li>Make sure you test your code.  We're going to use import to import your class definitions.  You might want to write an extra testing file that does this, and makes sure things work as expected.</li>
</ol>
