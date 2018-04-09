<h2>Purpose</h2>
<p>The goal of this homework is to give you some experience in dealing with external programs that calculate things for you, and in how to wrap them up in Python so that you don't have to think about them when you're using them.</p>
<h2>Assignment</h2>
<ol>
<li>Grab a copy of the executable of our simulator from the Files area of Canvas.  There are three versions, one for each major operating system.  You run this from the command line like this:
<blockquote><code>simulator waypoints 10</code></blockquote>
where <code>simulator</code> is the name of the executable, <code>waypoints</code> is the name of waypoints file, and <code>10</code> is the problem number.  Make sure you can run this code with the supplied waypoints file on your computer.<br><br>
</li>
<li>Write a class, called <code>Simulator</code>, that encapsulates this piece of code.  The class should be initialized with the problem instance number, and have a single function associated with it called <code>evaluate</code> that evaluates a list of waypoints:
<blockquote><code>w = [(-10, 10), (0, 2), (10, 10]<br>s = Simulator(10)<br>print s.evaluate(w)</code></blockquote>
The function should return the evaluation from the external code, as a floating point number.<br><br>
</li>
<li>Write some code that evaluates the most basic set of waypoints <code>[(-10, -10), (10, 10)]</code>, and then finds another list of waypoints that is better (has a lower cost).  Your code should store this better set of waypoints in a file called <code>better_waypoints</code>.</li>
</ol>
<h2>Thoughts</h2>
<ol>
<li>There's a lot of stuff we're leaving up to you in this homework.  It should follow the general form of the examples we went over in class.<br><br>
</li>
<li>The simulator uses the waypoints you supply and simulates a robot moving through a hostile world, with radiation sources in it.  The simulation will add up to total dose of radiation that the robot is exposed to as a drives from waypoint to waypoint, and will print this out when it ends.  More radiation is bad, less is good.  You don't know where the radiation sources are, but they are fixed for each problem instance.  You can specify the problem instance with the second command line argument, which should be an integer.  The radiation sources will be in the same place every time if the problem instance number is the same.  Pick one and fix it for testing. <br><br>
</li>
<li>The waypoint file has two numbers per line, corresponding to the x and y waypoint coordinates.  Your first waypoint should be (-10, -10) and your final one should be (10, 10).  There is no limit to the number of waypoints you can have.<br><br>
</li>
<li>Your evaluation function should take the list of waypoints (as a list of tuples), write it out to a waypoints file (in the correct format), call the external program (with the correct arguments), harvest the output, extract the cost, and return this value.  You should do each of these things in turn, and verify that they're doing the right thing before moving on to the next.<br><br>
</li>
<li>We asked you to come up with a better set of waypoints.  <em>Any</em> better set is fine for this homework.  We'll get to a more advanced optimzer next time.</li>
</ol>
<h2>What to Hand In</h2>
<p>A file called simulator.py with your code in it.  We'll import this file and run your code.  If we run the file as an executable, it should take an instance number on the command line, and output the file described in part 3 of the assignment.</p>
<h2>Grading</h2>
<p>There is a total of 10 points available fo this homework.</p>
<ol>
<li>Class correctly writes out a waypoints file. [3 points total]</li>
<li>Successfully runs external simulator. [3 points total]</li>
<li>Successfully harvests results of exteral simulator.  [3 points total]</li>
<li>Can use the simulator to come up with a better (lower cost) path.  [1 points total]</li>
</ol>
