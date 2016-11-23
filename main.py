from googlefinance import getQuotes
import json
from Tkinter import *
from time import sleep

import re






'''
#test
for stock in stocks:
    print json.dumps(getQuotes(stock), indent=2)
'''

class Portfolio:
        
    def __init__(self):
        self.stocks  = []
        
    def addStock(self, s):
        if(s not in self.stocks):
            self.stocks.append(Stock(s))
 
 
 
        
        
class Stock:
    def __init__(self,ticker):
        self.ticker = ticker
        self.updateData()
        
    def updateData(self):
        self.raw_quote = getQuotes(self.ticker)
        quoteDict = parse(self.raw_quote)
        self.Index = str(quoteDict['Index'])
        self.LastTradeWithCurrency = float(quoteDict['LastTradeWithCurrency'])
        self.LastTradeDateTime = str(quoteDict['LastTradeDateTime'])
        self.LastTradePrice = float(quoteDict['LastTradePrice'])
        self.LastTradeTime = str(quoteDict['LastTradeTime'])
        self.LastTradeDateTimeLong = str(quoteDict['LastTradeDateTimeLong'])
        try:
            self.Dividend = float(quoteDict['Dividend'])
        except (KeyError,ValueError):
            self.Dividend = 0
        
        self.StockSymbol = str(quoteDict['StockSymbol'])
        self.ID = int(quoteDict['ID'])
        
       
                            
                                            

#iterate i over quote of type String
def parse(quote):
    return quote[0]

'''
def update(sleep_time, root, portfolio,var_list):
    root.update() 
    sleep(sleep_time)
    
    for i in range(0,len(portfolio.stocks)-1):
        portfolio.stocks[i].updateData()
        var_list[i] = portfolio.stocks[i].LastTradePrice
    
    '''

def update(sleep_time, root):
    root.update() 
    sleep(sleep_time)
            



####
#Folders will contain subgroups of stock positions
'''
UPDATE
'''

class Folder:
    def __init__(self, name):
        self.folder = []
        self.name = name
        
    def addStock(self,s):
        if isinstance(s,stock):
            self.folder.append(s)   
            


    
    
#print json.dumps(getQuotes('aapl'), indent=2) #print appl stock ticker


if __name__=="__main__":
    
    Shayan_portfolio = Portfolio()
    Shayan_portfolio.addStock('aapl')
    Shayan_portfolio.addStock('fhlc')
    #print len(Shayan_portfolio.stocks)
    Shayan_portfolio.addStock('nflx')
    Shayan_portfolio.addStock('dis')
    
    


    #Create Program Window
    root = Tk()
    
    root.title("Real-Time Stock Quotes")
    root.geometry("400x600")
    #search area
    content=StringVar()
    Search_label = Label(root,text = "Search any Stock", font = ("Helvetica", 14),fg = 'black').pack(side=TOP, anchor=NW)
    search_entry = Entry(root, textvariable=content).pack(side=LEFT, anchor=NW)
    def callback():
        x = content.get()
        new_stock = Stock(x)
        
        new = True
        for stock in Shayan_portfolio.stocks:
            #Test if it is a new stock
            if stock.ID == new_stock.ID:
                new = False
        if (new):#Make a new stock
            stock_label = StringVar()
            stock_ticker = new_stock.StockSymbol
            stock_label.set(str(new_stock.LastTradePrice))
            
            
            stock4 = Label(root,text = new_stock.StockSymbol, font = ("Circuit", 20),fg = 'black').pack(side=TOP,anchor=E, padx=20)
            stock_price  = Label(root, textvariable = stock_label, font = ("Circuit", 20),fg = 'black').pack(side=TOP, anchor=E, padx=20)
            Shayan_portfolio.stocks.append(new_stock)
    
    search_button = Button(root, text="search", command = callback).pack(side=LEFT, anchor=N)
    
   
    
    
    
    
    #have each stock have its own label
   
    var_list = []
    label_list = []
    label_price = []
    for stock in Shayan_portfolio.stocks:
        #print stock.StockSymbol
        
        stock_label = StringVar()
        stock_ticker = stock.StockSymbol
        stock_label.set(str(stock.LastTradePrice))
        #stock_label.set(3)
        
        stock4 = Label(root,text = stock.StockSymbol, font = ("Circuit", 20),fg = 'black').pack(side=TOP,anchor=E, padx=20)
        stock_price  = Label(root, textvariable = stock_label, font = ("Circuit", 16),fg = 'black').pack(side=TOP, anchor=E, padx=20)
        #stock4.place(bordermode = OUTSIDE, height = 100, width = 50)

        var_list.append(stock_label)
        label_list.append(stock_label)
        label_price.append(stock_price)
        


    #Keep updating until exit
    update_time = 40
    time = update_time
    while(True):
        update(.05,root)
        
        time = time - 1
        if(time == 0):
            time = update_time
            
            for i in range(0,len(Shayan_portfolio.stocks)-1):
                Shayan_portfolio.stocks[i].updateData()
                var_list[i].set(str(Shayan_portfolio.stocks[i].LastTradePrice))
    
    #root.update()
    

    
    
'''
we need to parse json dump quote object to 
retrieve stock attributes
'''


'''
def createLabel(root, ticker)
    stock = Stock('aapl')
    stock_label = StringVar()
    stock_label.set(str(stock.LastTradePrice)))
    Label(root,text = "Apple", font = ("Helvetica", 16),fg = 'red').pack()
'''
