from fastapi import FastAPI, HTTPException
from datetime import datetime,timedelta
import pytz

app = FastAPI()


@app.get("/api")
async def get_info(slack_name:str, track: str):
    day = datetime.now().astimezone(pytz.UTC).strftime("%A")
    time = datetime.now().astimezone(pytz.UTC)
    formatted_time = time.strftime("%Y-%m-%dT%H:%M:%SZ")

    utc_offset = time.utcoffset()
    if utc_offset < timedelta(hours=-2) or utc_offset > timedelta(hours=2):
        raise HTTPException(status_code=400, detail="Not in range")

    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"  

    github_repo_url = "https://github.com/username/repo" 

    api = {
        "slack_name":slack_name,
        "current_day":day,
        "utc_time": formatted_time,
        "track": track,
        "github_file_url": "https://github.com/eniolaomotee/HNG-StageOne/blob/main/Stage1.py",
        "github_repo_url":"https://github.com/eniolaomotee/HNG-StageOne",
        "status_code": 200
        }
    return api  
    
