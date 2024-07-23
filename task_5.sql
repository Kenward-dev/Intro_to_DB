import mysql.connector

db = mysql.connector.connect(
	host="localhost",
    user="root",
    password="dogtorken",
    database="alx_book_store"
)

mycursor = db.cursor()

sql = "INSERT INTO customer(customer_id, custormer_name, email, address) VALUES (%s, %s, %s, %s)"
val = (1, "Cole Baidoo", "cbaidoo@sandtech.com", "123 Happiness Ave.")

mycursor.execute(sql, val)
db.commit()

mycursor.close()
mydb.close()
