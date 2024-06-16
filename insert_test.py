import psycopg2
import logging


logging.basicConfig(
    level=logging.DEBUG, 
    filename = 'log_test1.log', 
    format = '%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s', 
    datefmt='%H:%M:%S',
    )

host = 'localhost'
user = 'postgres'
password = '758325Nt'
db_name = 'test_project'

try:
  # connect to exist database
  connection = psycopg2.connect(host=host,
                                user=user,
                                password=password,
                                database=db_name)
  
  connection.autocommit = True
  
  
  with connection.cursor() as cursor:
      with open (r'C:\Users\Ирина\Desktop\Преддиплом\test_case\city.csv', encoding='utf-8-sig') as file:
          next(file)
          cursor.copy_from(file, 'city', sep=',')
      with open (r'C:\Users\Ирина\Desktop\Преддиплом\test_case\customers.csv', encoding='utf-8-sig') as file:
          next(file)
          cursor.copy_from(file, 'customers', sep=',')
      with open (r'C:\Users\Ирина\Desktop\Преддиплом\test_case\orders.csv', encoding='utf-8-sig') as file:
          next(file)
          cursor.copy_from(file, 'orders', sep=',')
      with open (r'C:\Users\Ирина\Desktop\Преддиплом\test_case\games.csv', encoding='utf-8-sig') as file:
          next(file)
          cursor.copy_from(file, 'games', sep=',')     
      with open (r'C:\Users\Ирина\Desktop\Преддиплом\test_case\games_ordered.csv', encoding='utf-8-sig') as file:
          next(file)
          cursor.copy_from(file, 'games_ordered', sep=',')
                                
                                
  logging.info(connection.commit())
  logging.info(print('Insert created successfully'))

except Exception as ex:
  logging.info(f'{ex} - while working with postgreSQL')

finally:
  if connection:
    connection.close()
    logging.info('Connection is closed')
    
with open('log_test1.log') as file:
    file = file.read()
    print(file)


    

