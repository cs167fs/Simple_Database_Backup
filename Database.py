#!/usr/bin/python
#############################################################################################
#
# This python script is uded for the back up of the techdocs database
# using the mysqldump utility.
#
#############################################################################################

# Import required python libraries 
import os
import time 
import datetime 

# MySQL database details for which the backup will be done...
# In order to make multiple database backups, create a text file with the dtaabase names that you wis to back up and use that text file ame as the database that you want to backup 
# below

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = '_root_user_password_'
#DB_name = '/backup/dbnames.txt'
DB_NAME = 'db_name'
BACKUP_PATH = '/Users/user1/WORK/DATABASES/Backup/'
NAME = 'Simple_db'
# Getting current datetime to create seperate backup folder like "SimpleDb -10-10-2017-000001".
DATETIME = time.strftime('-%d-%m-%Y--%H-%M-%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME + NAME 

# Checking if the backup folder already exists or not. If it doesn't exist then a folder will be created. 

print "Creating Backup Folder"
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH) 

# Code for checking if there is one database to back up or a number of assigned database.
print "Checking for Database name file."
if os.path.exists(DB_NAME):
     file1 = open(DB_NAME)
     multi = 1
     print "Databases file found..."
     print "Starting backup of all dbs listed in file " + DB_NAME
else:
     print "Database file not found..."
     print "Starting backup of databae " + DB_NAME
     multi = 0 

# Starting the actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flengths = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()    # reading database name from file
       db = db[:-1]              # deletes extra line 
       dumpcmd = "mysqldump -u" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
       os.system(dumpcmd)

print "Backup Script Completed"
print "Your backups have been created in '" + TODAYBACKUPPATH + "' directory"







