#from fastapi import FastAPI
#import pyjokes
#
#app = FastAPI()
#
#@app.get('/')
#def joke():
 #   return pyjokes.get_joke()
#
#@app.get("/{friend}")
#def friend_joke(friend:str):
#    return friend + "tells his joke:" + property.get_joke()
#
#@app.get("/multi/{friend}")
#def multi_friends_joke(friend:str,jokes_number:int):
#    result=""
#    for i in range(jokes_number):
#        result += friend + f"tells his joke #{i+1}:" + pyjokes.get_joke()+" "
#    return result
#
#from pydantic import BaseModel
#
#class Joke(BaseModel):
#    friend: str
#    joke: str
#
#class Jokelnput(BaseModel):
#    friend: str
#
#@app.post("/")
#def create_joke(joke_input:Jokelnput):
#    return joke_input.friend + "tells his joke:"+pyjokes.get_joke()
#
#@app.post("/")
#def create_joke(joke_input:Jokelnput):
#    return Joke(friend=joke_input.friend,joke=pyjokes.get_joke())
#
#@app.post("/",response_model=Joke)
#def creaet_joke(joke_input:Jokelnput):
#    """Создание шутки"""
#    return Joke(friend=joke_input.friend,joke=pyjokes.get_joke())


from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()
class  WikiInput(BaseModel):
    name: str
    quantity: int


@app.get("/route")
def wiki():
    return wikipedia.search("Bill", results=2)


@app.post("/wiki/{name}")
def wiki_search(name, quantity: WikiInput):
    return wikipedia.search(name, results=quantity)

@app.get("/wikipedia/{name}")
def wiki_suggest(name: str):
    return wikipedia.suggest(name)

@app.get("/name")
def wiki_summary(name:str):
    return wikipedia.summary(name)
