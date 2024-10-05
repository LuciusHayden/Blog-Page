from flask import Flask, redirect 
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def homepage():
  with open("homePage.html", "r") as f: 
    home = f.read()
  return home





@app.route('/01')
def blog01():
  number = "01"
  title = "Creating a blog website"
  entry = """ Today I created a very simple blog website using a mix of Python, CSS, and HTML. HTML and CSS are building blocks of the website leading to the asthetic of the website. Python is used in combination of Flask to fill up these spots used for text. Flask works with python to access the HTML and CSS and change the text. Because of this I can use the HTML and CSS to create a template which can be used to create a whole website with similar looking pages (some changes could easily be done) so a small website could be made in just 3 files, a CSS, a HTML, and a Python file. Attached is a image of my cat.
"""
  source = "static/images/cutecat.jpg"
  today = str(datetime.date.today()) 
  page = ""
  with open("template/blog.html", "r") as f: 
      page = f.read()
      page = page.replace("{number}", number) 
      page = page.replace("{title}", title) 
      page = page.replace("{entry}", entry) 
      page = page.replace("{today}", today)  
      page = page.replace("{source}", source)
  return page

  
@app.route('/02')
def blog02():
  number = "02"
  title = "Adding Blogs and Home Page"
  entry = """ Today I added a Home Page to make it easier to select a blog to look at. With this homepage (which is accesible from any blog page) you can select a blog to look at. This is easily accomplished by quickly throwing together a home page with minimal design, and adding links to the blogs. Additionally, adding new blogs is quite easy, just copy and paste a "template" and replace subroutine names and text. If this were a real website, the home page would definetly need to be more polished, but for a project its more than sufficent. Attached is a image of the majority of the code needed for the website. While its not a small amount, its by no means a lot. 
"""
  source = "static/images/blogwebsite.png"
  today = str(datetime.date.today()) 
  page = ""
  with open("template/blog.html", "r") as f: 
      page = f.read()
      page = page.replace("{number}", number) 
      page = page.replace("{title}", title) 
      page = page.replace("{entry}", entry) 
      page = page.replace("{today}", today)  
      page = page.replace("{source}", source)
  return page
app.run(host='0.0.0.0', port=81)