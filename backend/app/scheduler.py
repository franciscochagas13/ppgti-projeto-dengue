# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.apiDengue import fetch_and_store_data
import datetime

def start_scheduler(app):
    now = datetime.datetime.now()
    current_year = now.year
    current_week = now.isocalendar()[1]
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: fetch_and_store_data(ew_start=current_week, ew_end=current_week, ey_start=current_year, ey_end=current_year), trigger="interval", weeks=1)
    
    scheduler.start()

    # Para assegurar que o scheduler pare ao encerrar a aplicação
    @app.before_request
    def initialize():
        if not scheduler.running:
            scheduler.start()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        scheduler.shutdown()
