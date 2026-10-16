# Step1: Setup FASTAPI backend
from urllib import response
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from langchain_core.tools import tool

from ai_agent import graph, SYSTEM_PROMPT, parse_response
load_dotenv()  # Load environment variables from .env file
app = FastAPI()

# step2: Receive and validate request from Frontend

class Query(BaseModel):
    message: str



@app.post("/ask")



# query: Query -->> this basically means we are confirming that our
# query should be of type Query, which is a Pydantic model that we defined earlier. This ensures that the incoming request data is validated against the expected structure before processing it in the ask function.
async def ask(query: Query):
    # AI Agent
    # response = ai_agent(query)
   
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)



#  step3: Send response to frontend


    return {"response": final_response, "tool_called": tool_called_name}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
