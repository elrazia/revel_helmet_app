# Revel Helmet App

## What:
Creating an API to predict whether users are wearing a helmet a la [this NY Times Article](https://www.nytimes.com/2020/08/26/nyregion/revel-nyc-rules-helmet.html).

## How to get started:
1. Fork this repo
2. Cd into it and run `pipenv install` (additionally, you may run `pipenv install --dev` to get packages like requests for testing out API calls)
3. Add a `.env` file at the top-level containing:
```
AWS_ACCESS_KEY_ID=<key_id_here>
AWS_SECRET_ACCESS_KEY=<secret_key_here>
AWS_DEFAULT_REGION=us-east-1
```
4. `pipenv run python app.py` should get the API up and running locally.
