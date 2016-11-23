from googlefinance import getQuotes
import json
from Tkinter import *
from time import sleep

import re




kkk_stocks = ['aapl', 'sbux', 'cpxx', 'nflx', 'fhlc']

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
        self.updateData(ticker)
        
    def updateData(self,ticker):
        self.raw_quote = getQuotes(ticker)
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
    
def update(sleep_time, root):
    root.update() 
    sleep(sleep_time)   
    
    
    
    
    
    '''
    tempString = '' 
    atributeList = [] #return list of data
    k = 1 #make sure to check the second part of each value
    print len(quote)
    for i in range(1,len(quote)):
        if(quote[i] == 'u'):
            if(char[i+1] == '\''):
                if(k % 2 == 0):
                    k = k+1
                    i = i+2
                    while not (char[i] == '\''):
                        tempString += char[i]
                    atributeList.append(tempString)
    return atributeList
    '''            
                    
                



####
#Folders will contain subgroups of stock positions
#such as a biotech sector or a group of commodity stocks

class Folder:
    def __init__(self, name):
        self.folder = []
        self.name = name
        
    def addStock(self,s):
        if isinstance(s,stock):
            self.folder.append(s)   
            

    

 
'''      
class Bond:
 '''
#Shayan_portfolio = Portfolio()

#Shayan_portfolio.addStock('aapl')
#Shayan_portfolio.addStock('auy')
#Shayan_portfolio.addStock('fhlc')
#Shayan_portfolio.addStock('bby')


    
    
    
#print json.dumps(getQuotes('aapl'), indent=2) #print appl stock ticker


def main():
    
    Shayan_portfolio = Portfolio()
    Shayan_portfolio.addStock('aapl')
    Shayan_portfolio.addStock('fhlc')
    #print len(Shayan_portfolio.stocks)
    Shayan_portfolio.addStock('nflx')
    Shayan_portfolio.addStock('dis')
    
    
    
    root = Tk()
    
    root.title("Current Portfolio")
    root.geometry("400x600")
    #search area
    content=StringVar()
    Search_label = Label(root,text = "Search any Stock", font = ("Helvetica", 16),fg = 'red').pack(side=TOP, anchor=NW)
    search_entry = Entry(root, textvariable=content).pack(side=LEFT, anchor=NW)
    def callback():
        x = content.get()
        new_stock = Stock(x)
        if (new_stock in Shayan_portfolio.stocks):
            stock_label = StringVar()
            stock_ticker = new_stock.StockSymbol
            stock_label.set(str(new_stock.LastTradePrice))
            #stock_label.set(3)
            
            stock4 = Label(root,text = new_stock.StockSymbol, font = ("Circuit", 16),fg = 'red').pack(side=TOP,anchor=E, padx=20)
            stock_price  = Label(root, textvariable = stock_label, font = ("Circuit", 16),fg = 'red').pack(side=TOP, anchor=E, padx=20)
        Shayan_portfolio.stocks.append(new_stock)
    #search button
    search_button = Button(root, text="search", command = callback).pack(side=LEFT, anchor=N)
    
    #page name
    
    
    
    
    #have each stock have its own label
   
    var_list = []
    label_list = []
    for stock in Shayan_portfolio.stocks:
        #print stock.StockSymbol
        
        stock_label = StringVar()
        stock_ticker = stock.StockSymbol
        stock_label.set(str(stock.LastTradePrice))
        #stock_label.set(3)
        
        stock4 = Label(root,text = stock.StockSymbol, font = ("Circuit", 16),fg = 'red').pack(side=TOP,anchor=E, padx=20)
        stock_price  = Label(root, textvariable = stock_label, font = ("Circuit", 16),fg = 'red').pack(side=TOP, anchor=E, padx=20)
        #stock4.place(bordermode = OUTSIDE, height = 100, width = 50)
        
        label_list.append(stock_label)
        
    
    
    
    
    
    root.update() 
    sleep(2)
    
    
    update(1,root)
    
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