import scrapper_function

# pass proxyDict as argument to scrap method to enable proxy
#proxyDict = {'http': 'http://username:password@server:port', 'https':'https://username:password@server:port'}

scrapData=scrapper_function.scrap("https://www.peopleandthoughts.com/")
scrapper_function.drinkSoup('scrapData.txt',scrapData)

titles=scrapper_function.getTitles(scrapData) # ['title1','title2','title3']
paras=scrapper_function.getText(scrapData)    # ["Artical_text","Artical_text","Artical_text"]

# map artical title to artical text.
articles = dict()
for i in range(0,len(titles)):
    articles[titles[i]]= paras[i]

choice =int(raw_input("Enter Your choice: "))

# Fetch Artical and drink Soup
data = str(titles[choice])+"\n"+str(articles[titles[choice]])
scrapper_function.drinkSoup(titles[choice]+".txt",data)
print "Soup served! check file"+titles[choice]+".txt"