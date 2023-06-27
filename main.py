from bs4 import BeautifulSoup
import requests

search = input("Search for:") 
params = {"q": search} 
r = requests.get("https://www.bing.com/search", params = params) 

soup = BeautifulSoup(r.text, "html.parser") #gets the code for entire web page

results = soup.find("ol", {"id": "b_results"}) #finds the relevant code in web page that we are looking for
                     #element i am looking for
                            #attributes in the element
links = results.findAll("li", {"class" : "b_algo"})  #finds only the b_algo types in results

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"] #finds whatever specific attribute we are looking for

    if item_text and item_href:
        print(item_text)
        print(item_href)
       #exit() print("Parent:" , item.find("a").parent) #finds the parent element of the href 
        #print("Summary:", item.find("a").parent.parent.parent.find("p").text)
        children = item.find("h2")
        print("Next sibling of the h2:" , children)
        
        """
        children = item.children #compile a list if children elements in the list element
            for child in children:
            print("Child:", child)"""