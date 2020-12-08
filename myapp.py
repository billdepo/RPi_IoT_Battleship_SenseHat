# My Final Project - Create a Battleship Game Using Raspberry Pi and the SenseHat's LED Matrix

# Import flask framework
from flask import Flask, render_template, request, session, g, url_for, redirect

# Import sense_hat library (to work with Raspberry Pi's sense hat sensor hat)
from sense_hat import SenseHat

import random # Import random library - we will use it to shuffle a table
green=[0,200,0] # RGB = [0,200,0]. Using green color for battleship's ships positions (randomly generated positions).
black=[0,0,0]   # Rest of the LED matrix to be displaying nothing

# Creating list that has 64 elements (equal to LED matrix size 8x8) which contains 10 places for the ships (green) and the rest LED matrix positions are no colored
shipmap=[green]*10+[black]*54

s = SenseHat()  # create SenseHat object s

#clear the LED matrix on SenseHat (turn off any leds) during the start of our application
s.clear()  # no arguments in clear() method defaults to off

#Create a list that contains smaller lists with the details of each user. Initializing this users list to empty:
users = []

#With append() we add each user as a list with three fields, a unique user_id, user's name and password
users.append([1, 'Giannis', 'kodikos_Gianni'])
users.append([2, 'Maria', 'kodikos_Marias'])

# We give the name app to Flask
app = Flask(__name__)
app.secret_key = "Μυστικό_Κλειδί_Κρυπτογράφησης"

@app.before_request
def before_request():
    # Initialization of object g.user:
    g.user = None
    #Check if session cookie is occupied or in other words the user is connected/logged in
    if 'user_id' in session:
        # Run the users list to check the saved unique number in the session cookie with the registered users
        for user in users:
            if user[0] == session['user_id']: #compare the user_ids
                g.user = user #save the list with the details of the user in g.user so that they are accessible by all pages
                g.s = s #similarly, we make public to all pages, the object s in order to have access to SenseHat's data


# @app.route() of library Flask runs the following function depending on the URL that a visitor opens (GET request to server)
@app.route('/')
def route_func():
    #Check if the visitor is logged in as registered user and if no redirect him to logme page to login
    if not g.user: #true when g.user is None, therefore when user is not logged in (not None == True)
        return redirect(url_for('logme'))

    return render_template('index.html') #render the index.html page that greets user and has other links


# Using methods to define that we can receive data from our HTML form
@app.route('/logme', methods=['POST', 'GET'])
def logme():
    # As soon as a visitor visits the login page, we remove any session cookie saved to his computer with session.pop
    session.pop('user_id', None)
    #The contained commands of the following if are executed when a visitors hit the button "ΕΙΣΟΔΟΣ"
    if request.method == 'POST':
        # When a visitor hits the button, we save the username and password set given 
        username = request.form['username']
        password = request.form['password']
        for user in users:
            # If provided info is correct (registered user), a session cookie is created with name user_id. We access the list of users to make sure this visitor has registered as a user.
            if user[1] == username and user[2] == password:
                session['user_id'] = user[0] #store in session the unique user_id
                # Έπειτα δρομολογούμε το χρήστη στην αρχική σελίδα
                return redirect(url_for('route_func')) #redirect to home page

    return render_template('login.html') #if username, password given are wrong the page is refreshed


@app.route('/sense')
def sense_data():
    #check if not logged in as user (in such case this page can't be accessed)
    if not g.user:
        return redirect(url_for('logme')) #and visitor gets directed to login page to login

    return render_template('info.html') 


@app.route('/ships', methods=['POST', 'GET'])
#Battleship page where the game takes place
def battleship():
    #check if not logged in as user (in such case this page can't be accessed)
    if not g.user:
        return redirect(url_for('logme'))  #and visitor gets directed to login page to login

    #case when a User is logged in
    #first check if given number between [0,7]
    if request.method == 'POST': #checking if "ΑΠΟΣΤΟΛΗ στο Sense-HAT" button is pressed

        horizontal_index = int(request.form["horizontal"])
        if (horizontal_index < 8) and (horizontal_index >= 0):
            vertical_index = int(request.form["vertical"])
            if (vertical_index < 8) and (vertical_index >=0):
                s.set_pixel(horizontal_index, vertical_index, [0,0,200]) #light a new blue LED according to the data the user provided
        
        elif horizontal_index >= 8 :
            s.clear() #clear any lit LEDs at SenseHat

            #populate 10 random LEDs in LED Matrix with green color
            random.shuffle(shipmap) #updates the shipmap list randomly with 10 new green led positions
            s.set_pixels(shipmap) #updates the LED matrix based on the randomly generated shipmap

    return render_template('ships.html')


@app.context_processor
#Basic function:
def a_processor():
    # In the basic function, we implement a fucntion named roundv() [or other name we want] that accepts two argumnets (value and number of decimal digits)
    def roundv(value, digits):
        # We pass those arguments to Python's round() function
        return round(value, digits)

    #Latly, the basic function returns as a dictionary the name of the function roundv() we implemented in order to be available to HTML templats
    return {'roundv': roundv}


if __name__ == '__main__':
    app.run(debug=False)
    #in production mode debug = False
    #also if we wanted to make the pages accessible in the LAN network from other PCs we could include inside app.run the following: host='0.0.0.0'