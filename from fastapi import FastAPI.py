from fastapi import FastAPI
app = FastAPI(title="Test microsevice")
@app.get("/api/v1/hello")
def hello(name: str = ""):
   return {"msg": f"Hello {name}"}