from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler

from configs.db import initDB
from routes import idol_route
from services.idol_service import craw_data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def app_init():
   await initDB()
   
   scheduler = BackgroundScheduler()
   scheduler.add_job(craw_data, 'interval', days=1)
   scheduler.start()
 
   
app.include_router(idol_route.router)


 