##Documentation for Code Deployment on Azure Cloud
This document explains how to deploy the FastAPI app to Azure. The below are the exact steps I would follow when deployment is required.

##Azure Deployment Process
1. Azure Services Used:

- Azure App Service: For hosting the FastAPI web app (serverless, scalable, supports Python) and provides a public URL.
- GitHub Actions: For CI/CD (automated builds and deployments) to automatically deploy on every push to main.

2. Deployment Method/Tools:

Use GitHub Actions for free CI/CD (integrated with repo).
Tools: Azure CLI, VS Code Azure extension, or Azure Portal.

##Prerequisites(before deploying)

- An Azure Account.
- The application code in a Github repository.
- requirements.txt includes:
  - `fastapi`
  - `uvicorn[standard]`
  - `pydantic`
  - `pytest`
  - `gunicorn` (needed by Azure for production start-up)

Step-by-Step Process:

Step 1: Prepare the Application
Update Code for Production:
- Ensure main.py and utils.py are production-ready (e.g., handle environment variables if needed).

Step 2: Create Azure Resources:
- Go to Azure Portal → Create App Service (Linux, Python runtime).
- Name it (e.g., pangram-api), select a region, and choose a free tier.
- Click Review + Create > Create. Wait for deployment (5-10 minutes).
- Once created, go to App Service in the portal and note the URL (e.g., https://pangram-api.azurewebsites.net).

Step 3: Set Up CI/CD with GitHub Actions:
- In repo, create a file .github/workflows/deploy.yml with the following content:

name: Deploy to Azure
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'your-app-name'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}

- Get the publish profile from Azure Portal (App Service → Get Publish Profile) and add it as a GitHub secret.
- This workflow triggers on pushes/PRs to main, installs dependencies, runs tests, and deploys.

Step 4: Add Azure Secrets to GitHub:
- In Azure Portal, go to App Service > Deployment Center > Settings > Download publish profile.
- Open the downloaded .PublishSettings file and copy the content.
- In GitHub repo, go to Settings > Secrets and variables > Actions > New repository secret.
- Name: AZURE_WEBAPP_PUBLISH_PROFILE
- Value: Paste the entire publish profile content.
- Save.

Step 5: Deployment
- Trigger Deployment: Push changes to the main branch in GitHub repo. GitHub Actions will automatically build, test, and deploy.
- Monitor Deployment: Check the Actions tab in GitHub for logs. If issues arise, review Azure App Service logs in the portal (App Service > Logs > Enable Application Logging).
- Access the App: Visit https://your-app-name.azurewebsites.net/check_pangram (e.g., via GET: ?text=The%20quick%20brown%20fox or POST with JSON).

Environment Used
OS: Windows 10.
Python Version: 3.9+.
IDE: VS Code.
