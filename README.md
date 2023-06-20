# 2023-devsecops-example Example Project
This project is intended for use as a model to play with some more
DevSecOps principles in a practical way. 

## Overview
This exercise will take you through setting up a simple DevSecOps pipeline
for a Python project. The example Python project is a simple client that
interacts with the OpenWeatherMap API. The project contains some limited
tests. 

In the course of this exercise, you will set up your own copy of the 
repo to build in TravisCI, using pytest to perform automated testing
and coverage analysis, SonarCloud to perform security scanning and
reporting, and Coveralls.io to provide coverage reporting. 

After setting up the pipeline, there are some opportunities to improve
the project's performance in the pipeline. 

## Instructions
### Prerequisites
* Python 3.7+ (tested against 3.9)
* Python virtual environment module (I use `virtualenv` (`pip3 install virtualenv`))
* Github account
* travis-ci.com account (https://travis-ci.com, sign in with your Github account, choose the free plan, don't add any projects yet)
* coveralls.io account (https://coveralls.io, sign in with your Github account, choose the free plan, don't add any projects yet)
* sonarcloud.io account (https://sonarcloud.io, sign in with your Github account, choose the free plan, don't add any projects yet)

### General Procedure
#### I. Setup
1. Fork the repo 'https://jeffgennari@github.com/jeffgennari/lg23devsecops to your own Github account
2. Go into your Github user settings
3. Scroll down to select "Applications". You should see TravisCI and SonarCloud here.
4. Click "Configure" for TravisCI.
5. Under Repository Access, choose "Only select repositories", and select your fork of the 2023-devsecops-example repository from the drop-down.
6. Read and click through any approval prompts. 
7. Click Save.
8. You will be redirected to the TravisCI page to finish configuration.
   After a few moments, you should see the page refresh and your
   repository will be listed. 
9. Go back to Github Settings, and click again on "Applications" on the left bar.
10. Click "Configure" for SonarCloud.
11. Under Repository Access, choose "Only select repositories", and select your fork of the 2023-devsecops-example repository from the drop-down.
12. Read and click through any approval prompts. 
13. Click Save.
14. You will be redirected to the SonarCloud site to finish
    configuration. It is OK to click back to Github at this point.
14. Clone your forked repository to your development machine.
15. cd into the 2023-devsecops-example directory.
16. Create a virtual environment for testing: `virtualenv -p python3 venv`
17. Activate the virtual environment: `. venv/bin/activate` or `venv\Scripts\activate` on Windows.
18. Install the Python requirements: `pip3 install -r requirements.txt`

#### II. Local Testing
Run local tests: `py.test --cov --cov-report=xml owm tests -vv`

All tests should complete successfully.

#### III. Client Testing
This is not required, but if you would like to see the client in action,
you will need to sign up under the free plan for the OpenWeatherMap API.
Once you have signed up, get your API key, and paste it into a file in the
repository root named `.apikey`. Once this is done, you should be able
to run `test.py` to see the weather in Pittsburgh and at a nearby 
location.

#### IV. Configure the Pipeline
1. Go to your SonarCloud.io account.
2. Use the "+" menu at the top right to add a new project.
3. You should see your repo listed here. Select it to import the project.
4. When asked to choose your analysis method, pick "With Travis CI".
5. Copy the "SONAR_TOKEN" key listed. We will use this in a future step.
6. Click Next.
7. Under "Edit your .travis.yml file," choose Other.
8. Click "Continue." We will edit the .travis.yml file later. 
9. Copy the `sonar.projectKey` and `sonar.organization` lines. We will
   use these in a future step.
10. Click your profile photo in the top right, then go to the Security tab.
11. Create a token. The name does not matter. Copy the token. We will use this in a future step. 
12. Go to your TravisCI account.
13. Select your 2023-devsecops-example repository.
14. From the menu at the right, choose "Settngs".
15. Under Environment Variables, enter a new variable named "SONAR_TOKEN", and paste in the security token you copied in step 5.
16. Click "Add" to add the variable.
17. In the repository directory, edit the `.travis.yml` file. This is the TravisCI configuration file. 
18. Locate the "organization" value under "sonarcloud". It is set to "jwoytek" by default. Change this to the value of `sonar.organization` copied in step 9.
19. Save the `.travis.yml` file. 
20. Edit the `sonar-project.properties` file. This is the SonarCloud configuration file.
21. Change the value of the `sonar.projectKey` and `sonar.organization` to those copied in steap 9.
22. Save the `sonar-project.properties` file. 
23. Go to your coveralls.io account.
24. Click the "+" to add a repo. 
25. Locate your repo in the list and click the switch to "on". You may
    have to click "Sync Repos" if your repo does not appear.


#### Trigger a TravisCI Build
TravisCI will build whenever a commit is pushed to your repo. You can also
trigger a build manually from within TravisCI. Here, we are going to 
commit the changes to the TravisCI and SonarCloud files, which will 
trigger a build, and should execute all of the steps to test, scan, and
report scan and coverage results if all went well. 

Commit the two modified configuration files in your repo, and push them
to github. This will trigger an automatic build cycle in TravisCI. 

Go to your TravisCI account, and in the dashboard you should see a new
job running.

Follow along in the log, and you should see TravisCI set up the
the environment, execute the python tests, execute the SonarCloud scan, 
report the SonarCloud results, and then upload the coverage results to
coveralls.io.


#### Review the Results
Once the build is complete and if it succeeds, you should see the build
job logs in TravisCI, Github should show a green check on the project 
by the latest commit, SonarCloud.io should show a report on the project
scan, and coveralls.io should show a report on code coverage from the
tests. 

#### GitHub Actions
If you would like to try a different pipeline, GitHub Actions is configured for manual builds. in the directory `.github/workflows/manual.yml`. This pipeline is run manually by pressing `Actions > Run Workflow` from the repository settings. You should inspect the `manual.yml` file because it has a number of dependencies that must be satisfied. In particular, SonarCloud you to set a SONAR_TOKEN for the project. To set this token, do the following 
    * In your GitHub repository, go to `Settings > Secrets > Actions` and create a new secret with the following details:
    * In the Name field, enter SONAR_TOKEN 
    * in the Value field, enter the hash that Jeff provides.

When you run the workflow, you will see the SonarCloud analysis in SonarCloud (e.g. https://sonarcloud.io/summary/overall?id=jgennari-2023-devsecops-example). Simiarlly, you will see the Coveralls report in the Coveralls website (e.g. https://coveralls.io/github/jeffgennari/lg23devsecops). The specific URLs may change to reflect your account.

One of the nice things about GitHub actions is that we can see results for public repositories.

#### Extension
You should notice that the code is not 100% covered by tests. Use the
reporting in coveralls.io to locate the code that is not covered by 
tests, and create tests such that coverage reaches 100%. 

SonarCloud.io will show some "code smells", pointing out some things that
could be improved in the code. Attempt to fix these inefficiencies. 

Create a branch and made some modifications to the branch, then create
a pull request. Observe the automatic testing and reporting that Github
will show during the TravisCI pipeline run to assist in evaluating a
pull request prior to merging. 

As a second extension, install an additional security-related GitHub Action from the marketplace (https://github.com/marketplace?type=actions).

#### Credit
Credit to Jonathan Woytek for this exercise.
