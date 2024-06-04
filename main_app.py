from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests

app = FastAPI(debug=True)

class Itemexample(BaseModel):
    name: str
    prompt: str
    instruction: str
    is_offer: Union[bool, None] = None

class Item(BaseModel):
    model: str
    prompt: str

urls = {
    "llama3": "http://localhost:11434/api/generate"
}

headers = {
    "Content-Type": "application/json"
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat/{llms_name}")
def update_item(llms_name: str, item: Item):
    if llms_name in urls:
        url = urls[llms_name]
        payload = {
            "model": item.model,
            "prompt": item.prompt,
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return {"data": response.json(), "llms_name": llms_name}  # Use response.json() if the response is JSON
        else:
            print("error:", response.status_code, response.text)
            return {"item_name": item.model, "error": response.status_code, "data": response.text}
    return {"item_name": item.model, "llms_name": llms_name, "error": "Unsupported model"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port = 8000)

