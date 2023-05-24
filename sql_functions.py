# importing libraries 
import mysql.connector
import datetime 

#establishing connection
String = 'Your Connection details'
connection = mysql.connector.connect(
    String
)
cursor = connection.cursor(dictionary=True)



## USER

#function to add user details 
def add_user(details):                                      
    # dictiorary input
    values = list(details.values())
    prompt = f"""
             insert into user_details 
             values ( %s, %s, %s, %s, %s, Now() ); 
             """
    cursor.execute(prompt,values)
    connection.commit()

#get the name of user from id 
def get_uname(user_id):
    prompt = f"""select * from user_details
    where user_id = '{user_id}';"""
    cursor.execute(prompt)
    result = cursor.fetchall()
    for row in result:
        return row['name']

#user authentication
def user_authenticate(user_id,password):
    prompt = f"""select * from user_details
    where user_id = '{user_id}';"""
    cursor.execute(prompt)
    result = cursor.fetchall()
    if result:
        for row in result:
            if row['password'] == password:
                return 1
            return "Wrong Password"
    return "No User Name Exits"


## ADMIN

#function to add new admins 
def add_admin(details):                                     
    # dictiorary input
    values = list(details.values())
    prompt = f"""
             insert into admin_details 
             values ( %s, %s, %s); 
             """
    cursor.execute(prompt,values)
    connection.commit()

#admin authentication
def admin_authenticate(admin_id,adminpass):
    prompt = f"""select * from admin_details
    where admin_id = '{admin_id}';"""
    cursor.execute(prompt)
    result = cursor.fetchall()
    if result:
        for row in result:
            if row['password'] == adminpass:
                return 1
            return "Wrong Password"
    return "No Admin Found"


## FLIGHTS

#function to add flights 
def add_flight(details):                                    
    # dictiorary input
    values = list(details.values())
    prompt = f"""
             insert into flight_details
             (flight_id , flight_company, flight_time, flight_name)
             values ( %s, %s, %s ,%s); 
             """
    cursor.execute(prompt,values)
    connection.commit()
    return True

#function to remove flights 
def remove_flight(flight_id):                                    
    prompt = f"""
             delete from flight_details where flight_id = '{flight_id}';
             """
    cursor.execute(prompt)
    connection.commit()
    return True

#update the number of empty seat function 
def update_seats(flight_id):
    prompt = f"""select * from flight_details 
                where flight_id = '{flight_id}';
             """
    cursor.execute(prompt)
    result = cursor.fetchall()
    for row in result:
        seats = row['empty_seat']
        if seats > 0 :
            seats=seats-1
            prompt = f""" update flight_details 
                        set empty_seat = %s 
                        where flight_id = %s ;
                        """
            values = (seats,flight_id)
            cursor.execute(prompt,values)
            connection.commit()
            return True
        return False

#function to get flight names
def get_fname(flight_id):
    prompt = f"""select * from flight_details
    where flight_id = '{flight_id}';"""
    cursor.execute(prompt)
    result = cursor.fetchall()
    for row in result:
        return row['flight_name']

def get_fdetails(flight_id):
    prompt = f"""select * from flight_details
    where flight_id = '{flight_id}';"""
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result

#function to get flights based on time 
def get_flights(time): 
    # input must be datetime format
    prompt = f"""select * from flight_details 
                where flight_time > '{time}';
             """
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result

#function to display all flights():
def all_flights():
    prompt = f"""select * from flight_details;
             """
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result

#BOOKING 

#function to add booking details
def add_booking(details):                                   
    # dictiorary input
    values = list(details.values())
    prompt = f"""
             insert into booking_details(flight_id , user_id , booking_time)
             values ( %s, %s , NOW()); 
             """
    cursor.execute(prompt,values)
    connection.commit()

#function to get a specific users past bookings 
def get_mybooking(user_id): 
    #input must be the user id
    prompt = f"""select * from booking_details 
                where user_id = '{user_id}';
             """
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result


#function to get all bookings based on flight number
def get_bookings(flight_id): 
    prompt = f"""select * from booking_details 
                where flight_id = '{flight_id}' ;
             """
    cursor.execute(prompt)
    result = cursor.fetchall()
    return result