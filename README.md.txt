#Flask-Restful-App

To run this project first created a virtual env & run 
pipenv shell in this directory using python 3.7
 
# Install dependencies
	pipenv install

# Run project 
	python main.py
	
# Send request 
	# serach all book make a get request
		http://127.0.0.1:5000/api/book
	# serach single book with isbn number make get request
		http://127.0.0.1:5000/api/user/book && send a json data like
		{
			"isbn": "5",
			"name": "book5",
			"description": "book5 description",
			"price": 5000,
			"writer": "E",
		}
	# add a book in database
	......
	# remove a book in database
	.....
	# delete a book in database
	......
	# serach a custom search in book 
	......
