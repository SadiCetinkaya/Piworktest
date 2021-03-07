from urllib.parse import urlparse 
import mysql.connector 

def get_url(device_type): 
    mydb = mysql.connector.connect( host="localhost", user="yourusername", password="yourpassword",database="mydatabase") 
    mycursor = mydb.cursor()
    sql_state = "SELECT Stats_Access_Link FROM table_url where device_type = " + device_type
    mycursor.execute(sql_state)
    result = mycursor.fetchall()
    return result
    
def parser(url): 
    domain = urlparse(url).netloc 
    return domain  
    
def main(device_type): 
    result = parser(get_url(device_type))
    print(result)

main('AXO145')