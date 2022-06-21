# API Reference

## Getting Started
- Base URL: Currently this app can only be run locally and is not hosted as a base URL. The API is hosted at the default, http://127.0.0.1:8000/.
- AUthentication:This version of the application requires authentication.



## Endpoints

## POST/registration

- General:
  - Create a new user and Returns a message.
- Sample: POST http://127.0.0.1:8000/v1/registration

```json
{
	"message": "Registration successful"
}
```

## POST/token

- General:
   - Generates token using user details(password and username), Returns token.
- Sample: POST http://127.0.0.1:8000/v1/token

```json
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUiI1NiJ9.eyJzdWIiOiJvbnllIiwiZXhwIjoxNjU2MTh4NDM4fQ.9KouIEG03XNeQO34WXgSeoRiOGPMjZUIAhuUXbp2ZWc"
}
```

## POST/login

- General:
  - Login user using user details(email, password). Return firstname, lastname, username and email.
  - Authorization is required.
- Sample: POST http://127.0.0.1:8000/v1/login

```json
{
	"is_valid": {
		"firstname": "onyekachi",
		"lastname": "tony",
		"username": "onye",
		"email": "onye@gmail.com"
	}
}
```

## POST/item

- General:
  - Creates a new item using the submitted item, name, quantity, price, description and owner. Returns a  success message.
  - Authorization is required.
- Sample: POST http://127.0.0.1:8000/v1/item

```json
{
	"message": "item added successful"
}
``` 

### GET/item/{id}

- General:
  - It fetch item of  a given  ID if exist. Returns item name, quantity, price, description and owner.
  - Authorization is required.
- Sample: GET http://127.0.0.1:8000/v1/item/1

```json
{
	"name": "laptop",
	"quantity": 1,
	"price": 336000.0,
	"description": "hp Envy x360 brand new",
	"owner": "onye"
}	
``` 

### GET/{user}/items

- General:
  - It fetch all items of  a given user  if exist. Returns all user items.
  - Authorization.
- Sample: GET http://127.0.0.1:8000/v1/onye/items

```json
{
	"user items": [
		{
			"name": "laptop",
			"quantity": 1,
			"price": 336000.0,
			"description": "hp Envy x360 brand new"
		},
		{
			"name": "laptop",
			"quantity": 1,
			"price": 545000.0,
			"description": "MacBook Pro 8-core CPU and 10-core GPU brand new"
		}
	]
}
```

### GET/item

- General:
  - It fetch a list of all items.
  - Authorization is required.
- Sample: GET http://127.0.0.1:8000/v1/item

```json
[
	{
		"name": "laptop",
		"quantity": 1,
		"price": 336000.0,
		"description": "hp Envy x360 brand new",
		"owner": "onye"
	},
	{
		"name": "laptop",
		"quantity": 1,
		"price": 545000.0,
		"description": "MacBook Pro 8-core CPU and 10-core GPU brand new",
		"owner": "onye"
	}
]
```

## DELETE/item/{id}

- General:
  - Deletes item with a given ID if exist. Returns  success message.
  - Authorization is required.
- Sample: DELETE http://127.0.0.1:8000/v1/item/21

```json
[
	"item deleted"
]
```

## PATCH/item/{id}

- General:
  - Updates item with a given ID if exist. Returns  success message.
  - Authorization is required.
- Sample: PATCH http://127.0.0.1:8000/v1/item/22

```json
{
	"message": "item is updated"
}
```





