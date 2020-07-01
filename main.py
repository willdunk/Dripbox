from app.app import app
from app.task import delta_rss

app.apscheduler.add_job(func=delta_rss, trigger='interval', seconds=60, id='rss')

if __name__ == "__main__":
	app.run(host='0.0.0.0')
