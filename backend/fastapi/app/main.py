import uvicorn
from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware


from app.routers import news, newsTheme, keyword
from app.routers import media, tv, radio
from app.routers import community_rec, sns_rec, community_sub

app = FastAPI()

origins = [
    "http://j9c107.p.ssafy.io",
    "https://j9c107.p.ssafy.io",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fastapi")
def main():
    return responses.RedirectResponse(url="/docs/")

app.include_router(news.router)
app.include_router(newsTheme.router)
app.include_router(media.router)
app.include_router(keyword.router)

app.include_router(tv.router)
app.include_router(radio.router)
app.include_router(community_rec.router)
app.include_router(sns_rec.router)
app.include_router(community_sub.router)

if __name__ == '__main__':
    uvicorn.run(debug=False, host='0.0.0.0', port=8000)

