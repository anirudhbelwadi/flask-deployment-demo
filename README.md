# Demo for deploying flask app in <i><b style="color: blue">Python Anywhere</b></i>

## Initilize a Flask app <small>(here we use basic login authetication web app)</small>
- <a href="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/main.py">main.py</a>
- templates
    - <a href="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/templates/index.html">index.html</a>
    - <a href="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/templates/login.html">login.html</a>
- static/
    - assets/
        - img/
            - <a href="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/static/assets/img/back.jpg">back.png</a>

## Creating an account in Python Anywhere
- Head over to https://www.pythonanywhere.com/ and follow the below steps.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/1.getStarted1.png?raw=true">
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/2.getStarted2.png?raw=true">
- Fill all details for registraion.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/3.getStarted3.png?raw=true">

## Creating a web application in Python Anywhere
- Dashboard will open after registraion. Click on Web to view web apps page.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/4.creatingApp1.png?raw=true">
- Create a web app.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/5.creatingApp2.png?raw=true">
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/6.creatingApp3.png?raw=true">
- Select Flask Framework.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/7.creatingApp4.png?raw=true">
- Select Python Version
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/8.creatingApp5.png?raw=true">
- Enter path for flask file (Kept default here).
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/9.creatingApp6.png?raw=true">
- Check the default Flask application live on the link provided (<your_username>.pythonanywhere.com).
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/10.creatingApp7.png?raw=true">
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/11.creatingApp8.JPG?raw=true">

## Uploading custom files for deployment
- In the dashboard, click on files.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/12.uploadingFiles1.png?raw=true">
- File explorer will open. Click on <b>mysite/</b>.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/13.uploadingFiles2.png?raw=true">
- <b>mysite</b> folder will open. Click on <b>flask_app.py</b>.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/14.uploadingFiles3.png?raw=true">
- Contents of <b>flask_app.py</b> will be shown.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/15.uploadingFiles4.png?raw=true">
- Replace the existing contents with <a href="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/main.py">main.py</a>.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/16.uploadingFiles5.png?raw=true">
- Go back to file explorer in <b>mysite</b> folder and click on <b>Open Bash console here</b>.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/17.uploadingFiles6.png?raw=true">
- Scroll to the top of this webpage and click on <b>Code > copy HTTPS link</b>.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/18.uploadingFiles7.png?raw=true">
- Execute the following commands in the bash console.
- <code>ls</code><br>
- <code>git clone https://github.com/anirudhbelwadi/flask-deployment-demo.git</code><br>
- <code>rm '.\demo files\'</code><br>
- <code>cd flask-deployment-demo/app/</code><br>
- <code>rm main.py</code><br>
- <code>rm requirements.txt</code><br>
- <code>mv static/ ../../</code><br>
- <code>mv templates ../../</code><br>

<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/19.uploadingFiles8.png?raw=true">
- Go back to file explorer in <b>mysite</b> folder, confirm that <b>static</b> and <b>templates</b> folders are present and delete <b>flask-deployment-demo</b> folder.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/20.uploadingFiles9.png?raw=true">

## Verifying the deployment
- Go back to <b>Web</b> tab.
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/21.checkingDeployment1.png?raw=true">
- Click on <b>reload</b> to restart the server .
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/22.checkingDeployment2.png?raw=true">
- Use the same link to view the deployment (<your_username>.pythonanywhere.com).
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/23.checkingDeployment3.png?raw=true">
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/24.checkingDeployment4.png?raw=true">
<img src="https://github.com/anirudhbelwadi/flask-deployment-demo/blob/master/demo%20files/25.checkingDeployment5.png?raw=true">