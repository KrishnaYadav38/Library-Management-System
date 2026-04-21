books=[]
issued books=[]
def show_books():
    if len(books)==0:
        print('No books available')
    else:
        print('Available books')
        for b in books:
            print(b)
    