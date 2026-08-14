

**CRUD OPERATIONS using SQLAlchemy -**



***CREATE A NEW RECORD***

 with app.app_context():

     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

     db.session.add(new_book)

     db.session.commit()

 *NOTE: When creating new records, the primary key fields is optional. you can also write:*

* new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)*

 

 

**READ ALL RECORDS**

 with app.app_context():

     result = db.session.execute(db.select(Book).order_by(Book.title))

     all_books = result.scalars()



 *To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows.*

** 

**READ A PARTICULAR RECORD BY QUERY**

 with app.app_context():

     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

 *To get a single element we can use scalar() instead of scalars().*

 

 

**UPDATE A PARTICULAR RECORD BY QUERY**

 with app.app_context():

     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

     book_to_update.title = "Harry Potter and the Chamber of Secrets"

     db.session.commit()

 

**UPDATE A RECORD BY PRIMARY KEY**

 book_id = 1

 with app.app_context():

     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

      or book_to_update = db.get_or_404(Book, book_id)

     book_to_update.title = "Harry Potter and the Goblet of Fire"

     db.session.commit()



 *Flask-SQLAlchemy also has some handy extra query methods like get_or_404() (https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/#queries-for-views) that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated*



 

**DELETE A PARTICULAR RECORD BY PRIMARY KEY**

 book_id = 1

 with app.app_context():

     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

      or book_to_delete = db.get_or_404(Book, book_id)

     db.session.delete(book_to_delete)

     db.session.commit()



* You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.*





