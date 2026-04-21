books=[]
issued books=[]
def return_book():
    name=input('Enter the book name you want to return')
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,'is returned')
    else:
        print(name,'is not issued')