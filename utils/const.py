#import os
JWT_SECRET_KEY = "c07e154e8067407c909be11132e7d1bcee77542afd6c26ba613e2ffd9c3375ea"
JWT_ALGORITH = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5



TOKEN_DISCRIPTION ="it checks email and password if there are true it returns jwt token to you"
TOKEN_SUMMARY ="it returns JWT Token"

DB_HOST = "localhost"
DB_HOST_PRODUCTION = "10.110.0.2"
DB_USER = "postgres"
DB_PASSWORD = "11223344E"
DB_NAME = "inventory_db"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
#DB_URL_PRODUCTION = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST_PRODUCTION}/{DB_NAME}"
DB_URL_PRODUCTION = f"postgres://lrcuatcaglpgao:1bbf8d8bffeac7d9e3025d57765590c79e740a596c3b0ecd850b14b1d7cc08ac@ec2-18-210-159-154.compute-1.amazonaws.com:5432/d7cjjf5ebbf0s3"



