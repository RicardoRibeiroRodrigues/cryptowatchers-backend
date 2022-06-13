# Cryptowatchers - Backend
The backend for the cryptoWatchers site project, the frontend with the explanation of the features and the live demo is linked [here](https://github.com/insper-tecnologias-web/projeto-3-crypto-watcher-front).

## To run the backend localy:
1. Clone the repo
```sh
git clone https://github.com/RicardoRibeiroRodrigues/cryptowatchers-backend/
```
2. Make a virtual environment for the project:
```sh
python -m venv env
```
3. Install the dependencies.
In the project root (Remenber to activate the env):
```sh
pip install -r requirements.txt
```
4. For a easier local setup, change the database settings to sqlite:
On [cryptowatchers-backend/cryptoWatchers/settings.py](https://github.com/RicardoRibeiroRodrigues/cryptowatchers-backend/blob/main/cryptoWatchers/settings.py), change the DATABASE constant to (just uncomment this one and comment the other): 
```python
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
}
```
5. Apply the migrations:
```sh
python manage.py migrate
```
6. Run the server
```sh
python manage.py runserver
```

## Api paths:
- api/token/:    
Path to login a user, fill the POST request body as such: 
```json
{
  "username": "{{your username}}",
  "email": "{{your email}}"
}
```
Returns in the response body:
```json
{"token": "{{your token}}"}
```
- api/register/:        
Path to register a user, fill the POST request body as such:
```json
{
  "username": "{{your username}}",
  "email": "{{your email}}",
  "password": "{{your password}}"
}
```
Returns: 
```json
{"token": "{{your token}}"}
```
- api/cryptos/:
To create a new crypto, POST with the request body as such:
```json
{
  "crypto_id": "{{The crypto id in coincap API}}",
  "buying_price": "{{the price you paid}}",
  "quantity": "{{The quantity bought}}",
  "notes": "{{your notes about the purchase}}"
}
```
With the authorization header:
```json
{
  "Authorization": "Token {{your token}}"
}
```
Returns the list of all the cryptos of the user, including the one just posted.         
To see the coinCap API id, see [their documentation](https://docs.coincap.io/).      
To get the list of all user's crypto, make a GET request with the authorization header:
With the authorization header:     
```json
{
  "Authorization": "Token {{your token}}"
}
```
Returns a json with all user's crypto.
