books=[]
issued bookss=[]
def borrow_book():
    name=input('Enter the book you want to borrow')
    if name in books:
     issued_books.append(name)
     books.remove(name)
     print(name,'is issued')
    else:
        print(name,'book is not available')
        