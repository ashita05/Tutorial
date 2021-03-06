import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Books(book_id varchar(20)UNIQUE,title_id str(50)UNIQUE,genre str(10))')
c.execute('CREATE TABLE IF NOT EXISTS Titles(title_id varchar(20)UNIQUE,title str(50),publisher_id varchar(20)UNIQUE)')
c.execute('CREATE TABLE IF NOT EXISTS Publishers(publisher_id varchar(20)UNIQUE,name str(20),zip_code int(10))')
c.execute('CREATE TABLE IF NOT EXISTS ZipCodes(zip_code int(10)UNIQUE,city str(20))')
conn.commit()
conn.close()
c.execute('INSERT INTO Books VALUES(356789,"The Fault in our stars","Fiction")')
c.execute('INSERT INTO Titles VALUES(56899,"The Fault in our stars",54647483838)')
c.execute('INSERT INTO Publishers VALUES(54647483838,"Penguin books",1407)')
c.execute('INSERT INTO ZipCodes VALUES(1407,"New york")')
conn.commit()
conn.close()