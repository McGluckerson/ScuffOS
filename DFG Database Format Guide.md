how to access keys on the database

examples:
password: db["users"][user][password"] this will be a string
casino tokens: db["users"][user]["casino"]["casino tokens"] this will be an int

when searching the database using the os and prompted to "Enter key path: " enter the path like above but leave out the db as it is added automatically