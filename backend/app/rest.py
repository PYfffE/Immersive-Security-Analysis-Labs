from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/rest/hello")
async def root(request: Request):
    return {
        "message": "Deployed!",
        "ip": request.client.host
    }
