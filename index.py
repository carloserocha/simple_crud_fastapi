from config import engine, metadata, app
from fastapi.responses import JSONResponse
import uvicorn

# from controllers.route import post_route
from controllers.product import productRouter

# app.include_router(post_route, prefix="/api/post", tags=["post"])

app.include_router(productRouter, prefix="/api/product", tags=["product"])

@app.get("/")
def index():
    return JSONResponse(content={"message": "Hi there. I'm alived."})


if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("index:app", host="127.0.0.1", port=8000, debug=True)
