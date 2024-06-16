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
    logging.info(cursor.execute('''CREATE TABLE "customers"(
    "id" SERIAL NOT NULL,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "city_id" SMALLINT NOT NULL
);
ALTER TABLE
    "customers" ADD PRIMARY KEY("id");
CREATE TABLE "games"(
    "id" SERIAL NOT NULL,
    "game_name" VARCHAR(100) NOT NULL,
    "price" DECIMAL(8, 2) NOT NULL,
    "quantity" BIGINT NOT NULL
);
ALTER TABLE
    "games" ADD PRIMARY KEY("id");
CREATE TABLE "city"(
    "id" SERIAL NOT NULL,
    "city_name" VARCHAR(50) NOT NULL
);
ALTER TABLE
    "city" ADD PRIMARY KEY("id");
CREATE TABLE "orders"(
    "id" SERIAL NOT NULL,
    "customer_id" BIGINT NOT NULL,
    "order_date" DATE NOT NULL,
    "order_sum" BIGINT NOT NULL
);
ALTER TABLE
    "orders" ADD PRIMARY KEY("id");
CREATE TABLE "games_ordered"(
    "id" SERIAL NOT NULL,
    "game_id" BIGINT NOT NULL,
    "order_id" BIGINT NOT NULL,
    "quantity" BIGINT NOT NULL
);
ALTER TABLE
    "games_ordered" ADD PRIMARY KEY("id");
ALTER TABLE
    "orders" ADD CONSTRAINT "orders_customer_id_foreign" FOREIGN KEY("customer_id") REFERENCES "customers"("id");
ALTER TABLE
    "games_ordered" ADD CONSTRAINT "games_ordered_order_id_foreign" FOREIGN KEY("order_id") REFERENCES "orders"("id");
ALTER TABLE
    "customers" ADD CONSTRAINT "customers_city_id_foreign" FOREIGN KEY("city_id") REFERENCES "city"("id");
ALTER TABLE
    "games_ordered" ADD CONSTRAINT "games_ordered_game_id_foreign" FOREIGN KEY("game_id") REFERENCES "games"("id");'''))
    logging.info(connection.commit())
    logging.info(print('Table created successfully'))

except Exception as ex:
  logging.info(f'{ex} - while working with postgreSQL')

finally:
  if connection:
    connection.close()
    logging.info('Connection is closed')
    
with open('log_test1.log') as file:
    file = file.read()
    print(file)