from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Test Time API")


@app.get("/time")
def get_time():
    now_local = datetime.now().astimezone()
    now_utc = datetime.now(timezone.utc)
    return {
        "server_time": now_local.isoformat(timespec="seconds"),
        "server_time_utc": now_utc.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "unix": int(now_utc.timestamp()),
        "timezone": str(now_local.tzinfo),
    }

@app.get("/date")
def get_date():
    now = datetime.now().astimezone()
    return {
        "server_date": now.date().isoformat(),
        "server_datetime": now.isoformat(timespec="seconds"),
    }    


@app.get("/")
def root():
    return {"ok": True, "endpoints": ["/time"]}
