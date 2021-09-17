#Shravya A
#St Joseph Engineering College, Mangaluru
import sqlite3 as db
from sqlite3 import Error

def create_conn(table_name):    
    conn=None
    try:
        conn = db.connect(table_name)
        print("Successfully Connected.")
    except Error as e:
        print(e)
    return conn

def execute_query(conn,sql):    
    cur=None
    try:
        cur=conn.execute(sql)
        print("Query Successfully Executed.")
    except Error as e:
        print(e)
    return cur

def display(cur):              
    print("")
    for row in cur:
        print(row)


#create table query
create_table_query='''CREATE TABLE MOVIE ( 
    ID INTEGER PRIMARY KEY,
    MOV_NAME VARCHAR(20),
    MOV_ACTOR VARCHAR(25),
    MOV_ACTRESS VARCHAR(25),
    MOV_YEAR INTEGER,
    MOV_DIRECTOR VARCHAR(25))
    '''

#insert data queries
insert_data1_query='''INSERT INTO MOVIE(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) VALUES ('Bahubali 2','Prabhas','Anushka Shetty',2017,'Rajamouli')'''
insert_data2_query='''INSERT INTO MOVIE(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) VALUES ('KGF','Yash','Srinidhi shetty',2018 ,'Prashanth Neel')'''
insert_data3_query='''INSERT INTO MOVIE(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) VALUES ('Chhichhore','Sushant Singh Rajput','Shraddha Kapoor',2019 ,'Nitesh Tiwari')'''
insert_data4_query='''INSERT INTO MOVIE(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) VALUES ('Master','Vijay','Malavika Mohanan',2021 ,'Lokesh Kanagaraj')'''
insert_data5_query='''INSERT INTO MOVIE(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) VALUES ('Trance','Fahadh','Nazriya Nazim',2020 ,'Anwar Rasheed')'''


#display queries
display_all_query='''SELECT * FROM MOVIE'''
display_actor_query='''SELECT * FROM MOVIE WHERE MOV_ACTOR='Vijay' '''
display_director_query='''SELECT * FROM MOVIE WHERE MOV_DIRECTOR='Rajamouli' '''


#creating connection with data base
conn=create_conn("fav_movie")

execute_query(conn,create_table_query)
execute_query(conn,insert_data1_query)
execute_query(conn,insert_data2_query)
execute_query(conn,insert_data3_query)
execute_query(conn,insert_data4_query)
execute_query(conn,insert_data5_query)

#SELECT queries
print("\n\nDisplay All")
cur=execute_query(conn,display_all_query)
display(cur)

print("\n\nDisplay by Actor Vijay")
cur=execute_query(conn,display_actor_query)
display(cur)

print("\n\nDisplay by Director Rajamouli")
cur=execute_query(conn,display_director_query)
display(cur)

conn.close()
