<h1>ScamBlogs by Team SCAM </h1>

<h3>Roster</h3>
<b>Sascha Gordon Zolov</b> - Login/Logout Functionality + Cookies + Creating new accounts <br>
<b>Margie Cao</b> - Creating new blogs/CSS <br>
<b>Sasha (Alex) Murokh</b> - Sqlite, working with the database <br>
<b>Caden Khuu</b> - Editing existing Blogs/Entries and CSS <br>

![SCAM Team Flag](https://github.com/user-attachments/assets/f505d0ac-46e9-4463-9c51-749a009e859f)

<h3>Project Description</h3>
<p>Our website will act as a public live feed of blog posts <br>  
<b></b>User Features</b> <br>
- Users will be able to create accounts and log in <br>
- Users can view other blog posts without being logged in <br>
- Only logged-in users will be able to create blogs <br>
- Logged-in users can edit previous blogs <br>
- Blogs will be displayed chronologically, with more recent posts at the top <br>
- Logged in users can switch between a page with only their own blogs and a page with all of the blogs on the site <br>
<b>Site Features</b> <br>
 - Blog posts will be stores in an SQLite database <br>
 - A table will be dedicated to storing user IDs and passwords. <br>
 - Each logged-in user will be have an individual table containing their blogs; the file will begin blank and grow by row as the user creates new blogs <br>
 - Each blog is given a table containing a column of entries and a column of texts, with each entry corresponding to each block of text. Similar to the above method, this file will begin blank and grow by row as entries are added.  <br>
Blogs will be public and can be viewed by all members of the site, regardless of whether or not a given user is logged in. <br>
<h3>Install Guide</h3> </p>
<p> Clone the repository in the terminal, run: <br> 
  $ git clone git@github.com:SaschaGZ/Scam__PM_alexanderg311_sasham48_margiec3_cadenk4.git <br>
</p>

<h3>Launch Codes</h3>
<p> 
    1. Make a virtual environment, run: <br>
  $ python3 -m venv [name] <br> <br>
    2. Activate the virtual environment, run: <br>
  $ . [name]/bin/activate <br> <br>
    3. Go into the cloned repository, run: <br> 
  $ cd /PATH/TO/Scam__PM_alexanderg311_sasham48_margiec3_cadenk4 <br> <br>
    4. Install the required packages in your cloned repository, run: <br>
  $ pip install -r requirements.txt <br> <br>
    5. Launch the application, run: <br> 
  $ python3 app/__init__.py <br> <br>
    6. Open the local host link: <br>
  http://127.0.0.1:5000/

  When done using the virtual environment, run: <br>
  $ deactivate  
