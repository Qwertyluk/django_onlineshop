# Online shop

This repository contains an online shop template.

## Overall information

* The project is created using the django framework. 
* MySQL database is used for the data storage.
* The Bootstrap framewok is used to create the responsive views.

## Functionality
* The Home page
    * Displays all products that exists in the database.
    * Tags discounted and sold out products
    * Allows users to sort products by name, price and category
    * Filters products - can only display discounted or available products

<p align="center">
  <img src="https://i.ibb.co/PTkbfSq/xd.png" alt="Home page">
</p>

Filter form on the home page:

<p align="center">
  <img src="https://i.ibb.co/wgXt8BG/filter.png" alt="Home page filter">
</p>


* User registration
    * It is possible for users to create their own accounts. For this purpose a login form and a login view have been created.

<p align="center">
  <img src="https://i.ibb.co/6Rw50Cz/registration.png" alt="Registration">
</p>

* User login
    * Users can sign in to their previously created accounts using the login form on the login page.

<p align="center">
  <img src="https://i.ibb.co/PghN4dQ/login.png" />
</p>

* User data management
    * Signed in users are able to manage their personal information which were inserted during the registration process. There is also possibility to change current password.


<p align="center">
  <img src="https://i.ibb.co/zm4d1JX/management.png" alt="Management">
</p>

* Product page
    * Product name, category, price, description and information about availability are displayed on the detailed product page. User can also add concrete quantity of the product to the cart.

<p align="center">
  <img src="https://i.ibb.co/YWv2hh9/product.png" alt="Product page">
</p>

* Cart
    * The cart was implemented using the session mechanism. 
    * A view has been created that displays all the products inserted in the cart. In the case of the lack of the products in the cart, information about it appears.
    * On the cart page there is possibility to manage the qantities of products. User can also remove concrete product from the cart. 
    * A delivery addres form has also been displayed on the cart page.

<p align="center">
  <img src="https://i.ibb.co/ZTvyN88/cart.png" alt="Cart">
</p>

* Orders
    * Confirmed user orders are inserted to the database. The database stores information about quantities of products in the orders and the delivery address associated with a concrete order.
    * Users with the administrator rights exist in the system. These users are able to see all orders created by users. They have possibility to confirm each order.
	* Created orders are confirmed using SMTP protocol with an e-mail sent to the e-mail address provided in the delivery address form.

<p align="center">
  <img src="https://i.ibb.co/YBx8GsC/orders.png" alt="Orders">
</p>






