# Florida-Man
AI Script that creates Florida Man headlines based on existing data
<p>So basically this works by using Reddit's API to get Florida Man titles from the subreddit(r/floridaman), cleans up the data, puts it in a text file, and then the library "textgenrnn" makes generated Florida Man headlines. The titles are pretty bad though, so idk why this is a thing.</p>
<h4>To run:</h4>
<p>The following modules are needed:</p>
<ul>
  <li>json</li>
  <li>praw</li>
  <li>re</li>
  <li>textgenrnn(needs to be 1.5, not latest)</li>
</ul>
<br>
<p>1. Create a developer app in Reddit to gain API access, and then enter the details into users.json</p>
<p>2. Run the api.py script to populate the text file with titles</p>
<p>3. Run the floridaman.py script to generate headlines. These will be outputted into the command line or wherever you are running this.</p>
