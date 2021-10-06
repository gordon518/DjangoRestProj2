# Special Feature
The original project is at https://github.com/gordon518/DjangoRestProj1, The original one follows official practise.
But there are some shortcoimgs for the official framework. First the ORM in this framework is ugly and low efficient. 
Second there are too many configurations need to do when using this framework, you need to config data model, serializers, permissions and urls.
Convention over configuration, we should get rid of config. Instead of using the ugly and low efficient ORM, 
it is better to directly use SQL to operate the database. What? You dislike SQL and not comfortable using SQL to operate database?
If so, why you still use relational database? You should use object-oriented database directly. 
Nowdays Mongodb is mature and strong after many years developed.

But there are still people who dislike object-oriented database, and like using object-orient to operate relational database. 
For these people i suggest to use SQLALchemy to replace Django ORM.

Ok, in this project we use SQL directly, and use a generic router to get rid of url configuration. 
By this way, this project realized zero-configuration!!!

# Run Guide for this project
1. Install Phthon-v3.7.9

2. Run the following commands to install libraries:
   ```
   pip install Django djangorestframework requests
   pip install markdown       # Markdown support for the browsable API.
   pip install django-filter  # Filtering support
   ```

3. Run "pip list" command to check the library version:
   ```
   Django              3.2.7
   django-filter       2.4.0
   djangorestframework 3.12.4
   ```

4. Git clone this project from https://github.com/gordon518/DjangoRestProj2

5. Run the command of "python manage.py runserver" to start the API server

6. Test with tools, Use chrome to test restful API, Install and use Chrome Extension:PostWoman Http Test.
   ```
   Test case 1, user register:
   URL: http://localhost:8000/api/register
   Method:Post
   Fotmat:Custom--application/json
   JSon: {"username":"ICELEE", "password":"mypass", "name":"icelee"}
   ```

   ```
   Test case 2, add blog, you will get error because you haven't logged in:
   URL: http://localhost:8000/api/blogs/
   Method:Post
   Fotmat:Custom--application/json
   JSon: {"title":"My first blog", "body":"Oh Ya, Nice"}
   ```

   ```
   Test case 3, user login:
   URL: http://localhost:8000/api/login/
   Method:Post
   Fotmat:Custom--application/json
   JSon: {"username":"ICELEE", "password":"mypass"}
   ```

   ```
   Test case 4, add blog, you will get succeeded this time:
   URL: http://localhost:8000/api/blogs/
   Method:Post
   Fotmat:Custom--application/json
   JSon: {"title":"My second blog", "body":"Oh Ya, Nice"}
   ```
