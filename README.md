# inventory-system
An Inventory Management System for a small retail company

---

##  Features

* View all products in inventory
* View a single product
* Add new products
* Update product quantity
* Delete products
* Fetch real product data from OpenFoodFacts API
* Command Line Interface (CLI) for easy interaction
* Unit testing for reliability

---

##  Technologies Used

* Python
* Flask
* Requests (for API calls)

---

##  Project Structure

```
inventory-system/
│
│   ├── app.py
│   ├── models.py
│   
├── cli.py
├── test_app.py
├── requirements.txt
└── README.md
```

---

##Setup

1. Clone the repository:

```
git clone git@github.com:Asumpta2640/inventory-system.git
cd inventory-system
```

2. Install dependencies:

```
pipenv install
pipenv shell
```

3. Run the Flask server:

```
python app.py
```

4. Run the CLI (in a new terminal):

```
python cli.py
```
---


## Uses 

It allows users to:

* View products
* Add products
* Fetch products using barcode

Example:

```
1. View products
2. Add product
3. Fetch from API
4. Exit
```

---

## Future Improvements

* Add database (SQLite/PostgreSQL)
* Add authentication (admin login)
* Improve UI (React frontend)

---

## Author
This project was developed by Jelagat Asumpta email:sugutasumpta@gmail.com

---
#License

This project is licensed under the MIT License
