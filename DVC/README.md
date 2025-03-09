- Create a repo in the dagshub
- Clone that repo: e.g. `git clone https://dagshub.com/mehedibijoy/E2E-Diabetes-Detection.git`
- Go inside the folder: e.g. `cd E2E-Diabetes-Detection`
- Create a new README.md file inside the folder.
- Add the file to git: `git add README.md`
- Make first commit: `git commit -m "first commit"`
- Rename the branch: `git branch -M main`
- Push the README.md file from origin to the main: `git push -u origin main`


- Now activate the venv: `conda activate MLOps`
- Install requirements: `pip install -r requirements.txt`

- Create a data folder and copy the data.csv file into the folder.

- Initialize DVC: `dvc init`

- To track the data.csv using dvc: `dvc add data/data.csv`
    - It will create `.gitignore` and `data.csv.dvc` inside `./data/`. These two will be tracked with `git`.
    - To track these with `git`: `git add data/.gitignore data/data.csv.dvc`
    - To commit: `git commit -m "Added data.csv with DVC"`


- Now, to push everythin in DagsHub repository
    - go to `Remote` / `Data` / `DVC`
    - Add a DagsHub DVC remote:
        - `dvc remote add origin s3://dvc`
        - `dvc remote modify origin endpointurl https://dagshub.com/mehedibijoy/E2E-Diabetes-Detection.s3`
    - Setup Credintials:
        - `dvc remote modify origin --local access_key_id your_token`
        - `dvc remote modify origin --local secret_access_key your_token`
    - Check number of remote lists: `dvc remote list`
    - `dvc pull -r origin`
    - `dvc push -r origin`
    - `git push origin main`


- Make some modifications to the data. e.g. removed first three rows.
    - `dvc add data/data.csv` (the md5 hash key in data.csv.dvc will be updated)
    - `git add .`
    - `git commit -m "second commit"`
    - `dvc pull -r origin`
    - `dvc push -r origin`
    - `git push origin main`

















