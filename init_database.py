from flask import Flask, render_template, request,url_for,redirect
import mysql.connector

app = Flask(__name__)

@app.route("/userIndex")
def userindex():
	return render_template('userIndex.html')

@app.route("/staffIndex")
def staffindex():
	return render_template('staffIndex.html')

@app.route("/customerIndex")
def customerindex():
	return render_template('customerIndex.html')

@app.route("/movieList")
def movieList():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Movie ORDER by MovieName")
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('movies.html',movies=movies)

@app.route("/addMovie")
def addMovie():
	return render_template('addMovie.html')
	
@app.route("/add_movie_submit",methods=['post'])
def addMovie_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie (MovieName, MovieYear) "
        "VALUES (%s, %s)"
    )
    data = (request.form['moviename'], request.form['movieyear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieList'))

@app.route("/deleteMovie")
def deleteMovie():
	return render_template('deleteMovie.html')
	
@app.route("/delete_movie_submit",methods=['post'])
def deleteMovie_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    delete_stmt = (
        "DELETE FROM Movie WHERE MovieName=%s"
		)
    data = (request.form['moviename'])
    cursor.execute(delete_stmt, (data,))
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieList'))

@app.route("/genreList")
def genreList():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT Genre,MovieName from Genre,Movie WHERE Genre.Movie_idMovie=Movie.idMovie ORDER by Genre")
    cursor.execute(query)
    genres=cursor.fetchall()
    cnx.close()
    return render_template('genres.html',genres=genres)

@app.route("/addGenre")
def addGenre():
	return render_template('addGenre.html')
	
@app.route("/add_genre_submit",methods=['post'])
def addGenre_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    genre_stmt = (
        "INSERT INTO Genre (Genre, Movie_idMovie) "
        "VALUES (%s, %s)"
    )
    data = (request.form['genrename'], request.form['movieid'])
    cursor.execute(genre_stmt, data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('genreList'))


@app.route("/deleteGenre")
def deleteGenre():
	return render_template('deleteGenre.html')
	
@app.route("/delete_genre_submit",methods=['post'])
def deleteGenre_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    delete_genre_stmt = (
        "DELETE FROM Genre WHERE Genre=%s and Movie_idMovie=%s"
		)
    data = (request.form['genrename'],request.form['movieid'])
    cursor.execute(delete_genre_stmt, (data))
    cnx.commit()
    cnx.close()
    return redirect(url_for('genreList'))

@app.route("/roomList")
def roomList():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from TheatreRoom")
    cursor.execute(query)
    rooms=cursor.fetchall()
    cnx.close()
    return render_template('rooms.html',rooms=rooms)

@app.route("/addRoom")
def addRoom():
	return render_template('addRoom.html')
	
@app.route("/add_room_submit",methods=['post'])
def addRoom_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    room_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber,Capacity)"
        "VALUES (%s,%s)"
    )
    data = (request.form['roomnumber'],request.form['roomcapacity'])
    cursor.execute(room_stmt, data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('roomList'))
	
@app.route("/modifyRoom")
def modifyRoom():
	return render_template('modifyRoom.html')
	
@app.route("/modify_room_submit",methods=['post'])
def modifyRoom_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    modifyroom_stmt = (
        "UPDATE TheatreRoom SET Capacity = %s Where RoomNumber=%s"
    )
    data = (request.form['newroomcapacity'],request.form['roomnumber'])
    cursor.execute(modifyroom_stmt, data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('roomList'))
	
@app.route("/deleteRoom")
def deleteRoom():
	return render_template('deleteRoom.html')
	
@app.route("/delete_room_submit",methods=['post'])
def deleteRoom_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    deleteRoom_stmt = (
        "DELETE FROM TheatreRoom WHERE RoomNumber=%s"
		)
    data = (request.form['roomnumber'])
    cursor.execute(deleteRoom_stmt, (data,))
    cnx.commit()
    cnx.close()
    return redirect(url_for('roomList'))

@app.route("/showingList")
def showingList():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Showing ORDER by ShowingDateTime")
    cursor.execute(query)
    showings=cursor.fetchall()
    cnx.close()
    return render_template('showings.html',showings=showings)	

@app.route("/addShowing")
def addShowing():
	return render_template('addShowing.html')
	
@app.route("/add_showing_submit",methods=['post'])
def addShowing_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    addShowing_stmt = (
        "INSERT INTO Showing (ShowingDateTime, Movie_idMovie,TheatreRoom_RoomNumber,TicketPrice)"
        "VALUES (%s,%s,%s,%s)"
    )
    data = (request.form['datetime'],request.form['movieid'], request.form['roomnumber'],request.form['price'])
    cursor.execute(addShowing_stmt, (data))
    cnx.commit()
    cnx.close()
    return redirect(url_for('showingList'))

@app.route("/deleteShowing")
def deleteShowing():
	return render_template('deleteShowing.html')
	
@app.route("/delete_showing_submit",methods=['post'])
def deleteShowing_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    deleteShowing_stmt = (
        "DELETE FROM Showing WHERE idShowing=%s"
		)
    data = (request.form['showingid'])
    cursor.execute(deleteShowing_stmt, (data,))
    cnx.commit()
    cnx.close()
    return redirect(url_for('showingList'))

@app.route("/modifyShowing")
def modifyShowing():
	return render_template('modifyShowing.html')
	
@app.route("/modify_showing_submit",methods=['post'])
def modifyShowing_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    modifyShowing_stmt = (
        "UPDATE Showing SET ShowingDateTime=%s,Movie_idMovie=%s,TheatreRoom_RoomNumber=%s,TicketPrice=%s WHERE idShowing=%s"
		)
    data = (request.form['datetime'],request.form['movieid'], request.form['roomnumber'],request.form['price'],request.form['showingid'])
    cursor.execute(modifyShowing_stmt, (data))
    cnx.commit()
    cnx.close()
    return redirect(url_for('showingList'))

############################################
#customers
@app.route("/customerList")	
def customerList():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer ORDER by LastName")
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('customers.html',customers=customers)

@app.route("/addCustomer")
def addCustomer():
	return render_template('addCustomer.html')
	
@app.route("/add_customer_submit",methods=['post'])
def addCustomer_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    insert_customer = (
	"INSERT INTO Customer (FirstName, LastName, EmailAddress, Sex) "
	"VALUES (%s,%s,%s,%s)"
    )
    data = (request.form['firstname'], request.form['lastname'],request.form['email'],request.form['sex'])
    cursor.execute(insert_customer, data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))	
	
@app.route("/deleteCustomer")
def deleteCustomer():
	return render_template('deleteCustomer.html')

@app.route("/delete_customer_submit",methods= ['post'])
def delete_customer_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    delete_customer = (
	"DELETE FROM Customer WHERE idCustomer = %s"
    )
    data = (request.form['customerid'])
    cursor.execute(delete_customer, (data,))
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))

@app.route("/modifyCustomer")
def modifyCustomer():
	return render_template('modifyCustomer.html')

@app.route("/modify_customer_submit",methods= ['post'])
def modify_customer_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    modify_customer = (
	"UPDATE Customer SET FirstName = %s, LastName = %s,Sex = %s WHERE idCustomer = %s"
    )
    data = (request.form['firstname'],request.form['lastname'],request.form['sex'],request.form['customerid'])
    cursor.execute(modify_customer, (data))
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))

#attendence
@app.route("/attendenceList")
def attendenceList():
    return render_template('attendences.html')

@app.route("/customerInf_submit")
def customerInf_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT TicketPrice as total_paid,Customer_idCustomer,Showing_idShowing,Rating,FirstName,LastName from Showing,Attend,Customer WHERE Showing.idShowing = Attend.Showing_idShowing and Attend.Customer_idCustomer = Customer.idCustomer")
    cursor.execute(query)
    customerInfs=cursor.fetchall()
    cnx.close()
    return render_template('customerInfs.html',customerInfs=customerInfs)
	
@app.route("/showingInf_submit")	
def showingInf_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT TicketPrice as total_paid,Customer_idCustomer,Showing_idShowing,Rating,ShowingDateTime from Showing,Attend,Customer WHERE Showing.idShowing = Attend.Showing_idShowing and Attend.Customer_idCustomer = Customer.idCustomer")
    cursor.execute(query)
    showingInfs=cursor.fetchall()
    cnx.close()
    return render_template('showingInfs.html',showingInfs=showingInfs)

@app.route("/movieInf_submit")	
def movieInf_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT TicketPrice as total_paid,Customer_idCustomer,Showing_idShowing,Rating,idMovie,MovieName from Movie,Showing,Attend,Customer WHERE Showing.idShowing = Attend.Showing_idShowing and Attend.Customer_idCustomer = Customer.idCustomer and Movie.idMovie = Showing.Movie_idMovie")
    cursor.execute(query)
    movieInfs=cursor.fetchall()
    cnx.close()
    return render_template('movieInfs.html',movieInfs=movieInfs)
	
@app.route("/rateSort_submit")
def rateSort_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT Rating,TicketPrice as total_paid,Customer_idCustomer,Showing_idShowing from Showing,Attend,Customer WHERE Showing.idShowing = Attend.Showing_idShowing and Attend.Customer_idCustomer = Customer.idCustomer ORDER by Rating")
    cursor.execute(query)
    rateSorts=cursor.fetchall()
    cnx.close()
    return render_template('rateSorts.html',rateSorts=rateSorts)

#########################part2

#allow user to search showing information
@app.route("/search_Showings")
def search_Showings():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query1 = ("SELECT DISTINCT Genre from Genre")
    cursor.execute(query1)
    genres = cursor.fetchall()
    query2 = ("SELECT DISTINCT ShowingDateTime from Showing ORDER BY ShowingDateTime")
    cursor.execute(query2)
    datetimes = cursor.fetchall()
    return render_template('search_Showings.html',genres = genres, datetimes = datetimes)

@app.route("/search_Showings_submit",methods= ['post'])
def search_Showings_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    search_stmt = (
    "SELECT idShowing,ShowingDateTime,MovieName,RoomNumber,TicketPrice from Genre,Showing,TheatreRoom,Movie WHERE Genre.Genre = %s and Showing.ShowingDateTime > %s and Showing.ShowingDateTime < %s and Movie.MovieName = %s and Genre.Movie_idMovie = Movie.idMovie and Showing.Movie_idMovie = Movie.idMovie and Showing.TheatreRoom_RoomNumber = TheatreRoom.RoomNumber"
    )
    data = (request.form['searchgenre'], request.form['starttime'],request.form['endtime'],request.form['searchmovie'])
    cursor.execute(search_stmt, data)
    searchInfs=cursor.fetchall()

#check seats:####################
    if request.form.get('seat_is_available'):
        resultShowings= []
        for searchInf in searchInfs:
            id=str(searchInf[0])
            result='SELECT (SELECT Capacity FROM TheatreRoom, Showing WHERE TheatreRoom.RoomNumber=Showing.TheatreRoom_RoomNumber AND Showing.idShowing='+id+') - (SELECT COUNT(*) FROM Attend WHERE Showing_idShowing='+id+')' 
            cursor.execute(result)
#           if result<=0:
#           print("Room Full")
            seatsAvailable=cursor.fetchall()
        if seatsAvailable[0][0]>0:
           resultShowings.append(searchInf)
    else:
        resultShowings=searchInfs
################################
    cnx.close()
    return render_template('searchInfs.html',searchInfs=resultShowings)      

#allow user to buy a ticket and attend a showing
@app.route("/attend_Showings")
def attend_Showings():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query1 = ("SELECT * from Customer")
    cursor.execute(query1)
    customers = cursor.fetchall()
    query2 = ("SELECT Showing.idShowing,Showing.ShowingDateTime,Showing.TheatreRoom_RoomNumber,Showing.TicketPrice,Movie.MovieName from Showing, Movie where Movie.idMovie = Showing.Movie_idMovie ORDER by ShowingDateTime")
    cursor.execute(query2)
    showings = cursor.fetchall()
    return render_template('attend_Showings.html',customers = customers , showings = showings)


@app.route("/attend_Showings_submit",methods = ['post'])
def attend_Showings_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    insert_newattendence_stmt = (
    "INSERT INTO Attend(Customer_idCustomer,Showing_idShowing)"
    "VALUES(%s,%s)"
    )
    data = (request.form['customer'],request.form['showing'])
    try:
        cursor.execute(insert_newattendence_stmt, data)
        cnx.commit()
        cnx.close()
        msg = "Ticket Bought Successfully !!!"
    except BaseException:
        msg = "Fail to buy ticket, please try again! "
    return render_template('attendInfs.html',msg = msg)

#allow user to rate a showing
@app.route("/rate_Showings")
def rate_Showings():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query1 = ("SELECT Distinct Customer.idCustomer,Customer.FirstName, Customer.LastName from Customer,Attend where Customer.idCustomer = Attend.Customer_idCustomer ")
    cursor.execute(query1)
    customers = cursor.fetchall()
    query2 = ("SELECT Showing.idShowing,Customer.FirstName,Customer.LastName,Showing.ShowingDateTime,Showing.TicketPrice,Movie.MovieName from Showing, Movie , Attend, Customer where Movie.idMovie = Showing.Movie_idMovie and Attend.Showing_idShowing = Showing.idShowing and Attend.Customer_idCustomer = Customer.idCustomer  ORDER by idCustomer")
    cursor.execute(query2)
    showings = cursor.fetchall()
    return render_template('rate_Showings.html',customers = customers , showings = showings)

@app.route("/rate_Showings_submit",methods = ['post'])
def rate_Showings_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    update_rating_stmt = (
    "UPDATE Attend SET Rating = %s WHERE Customer_idCustomer = %s and Showing_idShowing = %s"
    )
    data = (request.form['rate'],request.form['customer'],request.form['showing'])
    try:
        cursor.execute(update_rating_stmt, data)
        cnx.commit()
        cnx.close()
        msg = "You have rated successfully !!!"
    except BaseException:
        msg = "Fail rating, Please try again!!!"
    return render_template('rateInfs.html',msg = msg)
	

#View watched Movies
@app.route("/searchViewed")
def searchViewed():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query1 = ("SELECT * from Customer")
    cursor.execute(query1)
    customers = cursor.fetchall()
    return render_template('searchViewed.html',customers=customers)	

@app.route("/watchedInfo_submit",methods = ['post'])
def watchedInfo_submit():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    watchedInfo_stmt = (
    "SELECT Distinct Movie.MovieName, Attend.Rating FROM Customer,Attend, Movie,Showing WHERE Attend.Customer_idCustomer= %s and Attend.Showing_idShowing=Showing.idShowing and Showing.Movie_idMovie = Movie.idMovie"
    )
    data = (request.form['customer'])
    cursor.execute(watchedInfo_stmt,(data,))
    watchedinfos=cursor.fetchall()
    cnx.close()
    return render_template('watchedInfo.html',watchedinfos=watchedinfos)

#view customer profile
@app.route("/searchProfile")
def searchProfile():
	return render_template('searchProfile.html')	

@app.route("/profiles",methods=['post'])
def profile():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    profiles = ("SELECT * from Customer WHERE FirstName=%s and LastName=%s")
    data = (request.form['pfirstname'],request.form['plastname'])
    cursor.execute(profiles, (data))
    profiles=cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('profiles.html',profiles=profiles)

#SQL injection attack
@app.route("/sql_injection")
def sql_injection():
    return render_template('sql_injection.html')
	
	
@app.route("/ListCustomers")	
def ListCustomers():
    cnx = mysql.connector.connect(user='root', password="root",database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer ORDER by LastName")
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('ListCustomers.html',customers=customers)

	
@app.route("/submit_sql_injection",methods = ['post'])
def submit_sql_injection():
    cnx = mysql.connector.connect(user='root', password='root', database='movietheatre')
    cursor = cnx.cursor()
    customerid=request.form['customerid']
    firstname=request.form['firstname']
    lastname = request.form['lastname']
    query = ("SELECT * from Customer where idCustomer='"+customerid
    +" FirstName="+firstname+" LastName="+lastname)
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('ListCustomers.html',customers=customers)

if __name__ == "__main__":
    app.run(debug=True)