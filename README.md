
# Flask Vercel Postgres

[Voici le résultat](https://flask-squelette-vercel.vercel.app)

## Local
- **Programme nécessaire :**
  - *Clicker [ici](https://www.python.org/downloads/) pour installer Python*
  - *Clicker [ici](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) pour installer Postgres*
- **Instalation des packages Pyhton :**
  - *`pip install -r requirements.txt`*
- **Initialisation de la base de données :**
  - *Mettre le dossier `PostgreSQL\15\bin` dans le path pour utiliser la commande psql ([une aide si vous ne savez pas faire](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/),par defaut c'est :`C:\\PostgreSQL\15\bin`)*
  - *se connecter a la base de données en tant que postgres (`psql --username=postgres` a éxecuter dans un invite de commande(win + r et taper cmd))*
  - *`create user flaskapp password 'flaskapp';`*
  - *`create database flaskapp with owner flaskapp;`*
  - *Créer un fichier ```.env``` dans le dossier database qui contient : *
    ```ini
    HOST=localhost
    PORT=5432
    DATABASE=flaskapp
    USER=flaskapp
    PASSWORD=flaskapp
    ```
  - *double clicker sur database.py*
- **Lancer le serveur :**
  - *double clicker sur server.py*
  - *aller a l'url http://localhost*
## Online
  - **Créer une base de données en ligne :**
    - *Exemple : [ElephantSQL](https://www.elephantsql.com)*
  - **Initialisé la base de données en ligne :**
    - *Créer un fichier ```site.env``` dans le dossier database qui contient les identifiants de la base de données en ligne exemple :*
    ```ini
    HOST=lucky.db.elephantsql.com
    PORT=5432
    DATABASE=ryyfkeal
    USER=ryyfkeal
    PASSWORD=YsAWEdcwhEVANbrqmmhSvbEwmbo_PNz7
    ```
    - *lancé le fichier database.py avec l'argument ```--site```*
  - **Mettre le site en ligne**
    - *Aller sur [Vercel](https://vercel.com)*
    - *Se connecter avec son compte Github*
    - *Créer un nouveau projet*
    - *Choisir votre dépot github*
    - *Aller dans les paramètres pour ajouté les variables environements qui sont vos identifiants base de données*
    ![image](img_readme/Sans%20titre.png)


    