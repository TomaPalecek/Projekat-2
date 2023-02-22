# Drugi Projekat
## Pravljenje web aplikacije za trivia kviz

admin:
email - tatamate@itbc.org
pass - 123

### Ciljevi aplikacije:
* Omogucavanje korisnika da igraju kviz nalik milionera jedan protiv drugog
* Kreiranje kviza/izazivanje drugih igraca na kviz
* Odgovaranje na pitanja
* Pracenje statistika igraca
* Specijnih permisija u zavisnosti autorizacije korisnika

### Predvidjeni Entiteti baze podataka:
* users, players, admins, admin_types for logging in and creating a user/player/admin
* quizzes for the creation of a quiz and tracking its stats
* q and as for generating questions for a quiz and gathering players answers
* questions and categories for creating questions and its categories

### Lista ruta:
* CRUD operacije svih entiteta
* Odgovaranje na pitanja
* Prihvatanje/odbijanje zahteva za kviz
* unosenje vremena za kviz
* proglasavanje pobednika...




## Instrukcije za pokretanje :)

### Installation

### Create virtual environment
##### PyCharm
```bash
venv ./venv
```
##### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
##### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
#### Activate Virtual environment
Open terminal and navigate to project directory, then run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

#### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
#### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

#### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


### Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```