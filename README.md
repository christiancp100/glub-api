# Launch Project

1. Create a virtual env (call it venv)
2. Activate virtual env: <code>source venv/bin/activate</code>
3. Install dependencies: <code>pip install -r requirements.txt</code> 
4. Run the Database container in another terminal instance: <code>docker compose up</code>
5. <code>python manage.py migrate</code>
5. <code>python manage.py runserver</code>


# If the task requires any package installation

Before pushing any changes to the repository:
- <code>pip freeze > requirements.txt</code>
- <code>python manage.py test</code> --> <b>Tests must pass</b>

# Where do I create my apps?

In the apps directory
<code>cd apps</code>
<code>python manage.py startapp <app_name></code>

# Open a Django Shell

<code>python manage.py shell</code>

Then you can execute any python code and import the functions and classes implemented in the project scope

# Work with Git

<code>git checkout master</code>

<code>git pull</code>

<code>git checkout features/GLUB-XX</code>

When you´re done working:

<code>git status</code>

<code>git add .</code>

<code>git commit -m "Type her your message""</code>

<code>git push</code>