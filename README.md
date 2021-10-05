This is a stock system that will allow the user to track products and suppliers, edit their details or create new ones.

In order to use the system, please enter the following in your terminal:

```
createdb shop_manager

psql -d shop_manager -f db/shop_manager.sql

python3 console.py

flask run
```

Once these have been entered individually, please go to your browser and enter localhost:5000 in order to gain access.

This project meets the following MVPs:

- The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.

- The inventory should track manufacturers, including a name and any other appropriate details.

- The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.

- Show an inventory page, listing all the details for all the products in stock in a single view.

- As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

While also meeting the following extensions:

- Calculate the markup on items in the store, and display it in the inventory

- Filter the inventory list by manufacturer. 

- Categorise your items. Provide an option to filter the inventory list by these categories.

- Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.
