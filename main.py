import pandas as pd
from fastapi import FastAPI, HTTPException, Header

df = pd.read_csv('players.csv')

prog = FastAPI()

API_KEY = 'apikeyftdssub02'

@prog.get("/")
def homepage():
    return {"message": "Hello World"}
@prog.get("/players")
def getAllPlayers(api_key:str=Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        return df.to_dict(orient='records')

@prog.get("/players/state/{state}")
def getPlayer(state:str,api_key:str=Header(None)):
    print(api_key)
    print(state)
    if api_key is None or api_key!= API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_state = df[df['state']==state]
        return player_by_state.to_dict(orient='records')
    
@prog.get("/players/pos/{position}")
def getPlayer(position:str,api_key:str=Header(None)):
    print(api_key)
    print(position)
    if api_key is None or api_key!= API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_position = df[df['position']==position]
        return player_by_position.to_dict(orient='records')

@prog.get("/players/pos/{year}")
def getPlayer(position:str,api_key:str=Header(None)):
    print(api_key)
    print(position)
    if api_key is None or api_key!= API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_position = df[df['position']==position]
        return player_by_position.to_dict(orient='records')