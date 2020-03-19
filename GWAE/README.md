# The Online Shop - Lab (Part 3); Forms 
<br/>
Today, we are continuing creating <b>our awesome online shop!</b>
Remember, never stop your <b>creativity</b>. Keep it going!
<br/>

Firstly, <b>Fork</b> and <b>Clone</b> this repository to your Desktop, and open the folder. Note that it has the finished Part 1 and Part 2 in it already.
<br/>

You can also use Today's lecture as reference if you forgot certain lines - https://tinyurl.com/flask-forms



## Part 1: Finalize "Cart" Feature
In store.html: 
1. Display products directly from the database. Note there are already products in the database.

(Hint: Use a function from database.py in order to get all the products and then pass them into render_template. You do NOT need a variable route here because you don't need any information from the user.)

a. Inside of `app.py`, in the function that is run when the user goes to the store page, first use the function query_all() to get all the products from the database.

b. Then pass those those products into the `render_template` function. Use something like `render_template('file.html', products = product_list)`

c. Finally inside of the `store_html` file create a for loop to go through all the products and display them on the page. Look at slide 2 for tips.

2. Make it so when you click on "Add To Cart" button it adds the selected product to the Cart table. 

(Hint: Now we will need a variable route since we need to know which product we should add to the cart. Use a variable route like "/add-to-cart/<int:product_id>" and the product_id will tell us which product we are adding. You will also find the "add_to_cart()" function from database.py very useful here!)
</br>

## Part 2: Creating Our Admin Portal
1. Create a new app route `@app.route("\login",methods=['GET','POST'])`. For right now, if the `request.method` is GET, have this route return the `render_template` of `"login.html"`, else return the string `"POST request"`.

(Hint: look at slide 15)

2. In `"login.html"` add a form that will allow the user to enter in a username, a password, and submit.  Make sure that your form tag `<form action="ROUTE" method="POST">` has an `action=` attribute that will POST this form to the route you made in the last step. Make sure all your input tags have name attributes. 

(Hint: look at slide 18)

3. Back in `app.py`, we will want to edit the `login` route so that on a POST request it will check if the user has put in the correct username and password, and if they are correct it will return the string `"logged in!"` and if they are wrong, it will return the `render_template` of `"login.html"`. 

(Hint: look at slide 24 to see how to get info out of a form, we will use something like `request.form[NAME ATTRIBUTE]`)  

(Hint 2: Note, you will NOT need a user class like other login examples since we will only have one admin account. Therefore, we can just check the login using something like `username == 'admin' and password=='admin'`)

# BONUSES:
4. Create an another app route and another html file and call it "portal.html", this will be the portal the admin can log into and control the website's database.

5. In portal.html:
- Create a table that shows all the products.
- In the table, have an "edit product" feature.
- In the table, have a "delete product" feature.
- After creating a table, create a new form for "adding products" feature.

## BONUS: Finalize your website design

Finalize your website's design, make sure it looks clean and organized, and add any missing colors/fonts...etc.

Ideas for design:
- Add a carousel (Slide show)
- Add a navbar

## BONUS:
- Implement a real "Paypal" API, and link it inside the cart.html to pay for the products. (You can find useful info here: https://developer.paypal.com/)
 
