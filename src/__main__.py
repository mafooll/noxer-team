import os
import threading
import atexit
from loguru import logger
from src import create_app
from src.app.config import Config
from src.app.tasks import periodic_sync
from apscheduler.schedulers.background import (  # type: ignore
    BackgroundScheduler
)

app = create_app()
scheduler = BackgroundScheduler()


def sync_job():
    logger.info(f"Запущен sync_job в PID: {os.getpid()}")
    with app.app_context():
        periodic_sync()


def start_scheduler():
    scheduler.add_job(
        func=sync_job,
        trigger="interval",
        seconds=Config.LOAD_INTERVAL_SECONDS,
        max_instances=1,
    )
    scheduler.start()
    logger.info("Scheduler started")
    atexit.register(lambda: scheduler.shutdown())


if os.environ.get("RUN_SCHEDULER", "0") == "1":
    logger.success(os.environ.get("RUN_SCHEDULER", "0"))
    threading.Thread(target=start_scheduler, daemon=True).start()
