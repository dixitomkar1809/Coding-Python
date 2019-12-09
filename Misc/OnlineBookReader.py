class OnlineBookReader:
    def __init__(self):
        self.library = Library()
        self.userManager = UserManager()
        self.display = Display()
        self.activeBook = None
        self.activeUser = None

    def getLibrary(self):
        return self.library

    def getUserManager(self):
        return self.userManager

    def getDisplay(self):
        return self.display

    def getActiveBook(self):
        return self.activeBook

    def getActiveUser(self):
        return self.activeUser

    def setActiveBook(self, book):
        self.activeBook = book
        return

    def setActiveUser(self, user):
        self.activeUser = user
        return

class Library:
    def __init__(self):
        self.books = {}

    def addBook(self, book):
        if book.id in self.books:
            return False
        else:
            self.books[book.id] = book
            return True

    def removeBook(self, book):
        if book.id in self.books:
            del self.books[book.id]
            return True
        else:
            return False



class UserManager:
    def __int__(self):
        self.users = {}

    def addUser(self, user):
        if user.id in self.users:
            return False
        else:
            self.users[user.id] = user
            return True
    def removeUser(self, user):
        if user.id not in self.users:
            return False
        else:
            del self.users[user.id]
            return True



class Display:
    def __init__(self):
        self.activeBook = None
        self.activeUser = None
        self.pageNumber = 0

    def displayUser(self, user):
        self.activeUser = user
        self.refreshUserName()

    def displayBook(self, book):
        self.activeBook = book
        self.pageNumber = 0
        self.refreshTitle()
        self.refreshDetails()
        self.refreshPage()

    def turnPageForward(self):
        self.pageNumber+=1
        self.refreshPage()

    def turnPageBackward(self):
        self.pageNumber-=1
        self.refreshPage()

    def refreshTitle(self):
        print(self.activeBook.getTitle())

    def refreshDetails(self):
        print(self.activeBook.getDetails())

    def refreshUserName(self):
        print(self.activeUser.getUserName())

    def refreshPage(self):
        print(self.pageNumber)


class Book:
    def __init__(self, title, details):
        self.bookId = id
        self.bookTitle = title
        self.bookDetails = details

class User:
    def __init__(self):
        pass