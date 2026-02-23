# Notes for Django

1. Create the folder for the project
2. Create the virtual environment (python -m venv venv)
3. Activate venv (MAC: source venv/bin/activate) (Windows: .\venv\Scripts\activate)
4. Install django (pip install django)
5. Upload dependencies into requirements file (pip freeze > requirements.txt)
6. Create django project (django-admin startproject config .)
7. Create gitignore file
Complete the structure of the project (create templates and static folders)
FInish the settings


Messages addressed to "meeting group chat" will also appear in the meeting group chat in Team Chat

Luis Renteria 9:24 PM
## Notes for creating repos
1. Make sure that all of your files are saved!
2. On the terminal (make sure you're on the right folder) execute the command: **git init**
3. If you need a gitignore file, make sure to create that file and set up that correctly. 
4. Add all of the files from your project by executing: **git add -A**
5. Save all of those in a single group (it's called commit): **git commit -m "DESCRIPTION OF WHAT YOU'RE UPLOADING"**
6. Create the main branch (the space where we are going to store all of the commits): **git branch -M main**
7. Add the remote to our project (the repo from github where we are going to communicate): **git remote add origin git@github.com:YOUR_GITHUB_USER/NAME_OF_YOUR_REPO.git**
8. OPTIONAL: if you want to verify to which repo it's linked **git remote -v**
9. Send everything to github (push the elements to the repo): **git push origin main**

Note: When the configuration is set, you can just add the new files, commit and push!