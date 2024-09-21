### Follow this guide to setup the environment
---
#### External dependencies
- `pip install Flask` - Docs - https://flask.palletsprojects.com/en/3.0.x/
- `pip install requests` - Requests Library - https://requests.readthedocs.io/en/latest/
- sqlite3 docs - https://docs.python.org/3/library/sqlite3.html
- https://www.fruityvice.com/

#### Install browser plugins

Install the JSON formatter extension for chrome (or lookup for other browsers)
https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa

#### Run
- Open terminal
- `cd src` or make sure the terminal is in the src directory
- `python -m flask run` to run the server
- CTRL-C or CTRL-Z to stop the server

#### Git
- Fork this repository to create your own version/copy of the repo.
- `git clone <your repository link> <folder name, example, FruitRest>`
This will provide you with a working git repo clone of this project.
- Make changes
- `git add .` To add all changes to stage
- `git status` - To view the status
- `git commit -m "Commit message"` To make a commit to the repo.
- `git push origin`

Show history
- `git log` To show the git commit history. You can press `q` to quit out of the history.

If you want to delete some changes from your local branch/your computer repo.
- `git reset --hard HEAD~1` - Here `1` is the number of commits that you want to rollback/delete. **BE CAREFUL: THIS WILL DELETE ALL THE CHANGES IN THE LAST 1 COMMIT**
- `git reset --soft HEAD~1` - This will only "uncommit" and bring back the changes to your stage.

If you want to delete some changes from your remote/github repo.
- Reset hard in your local branch
- `git push origin --force` - To force delete the changes