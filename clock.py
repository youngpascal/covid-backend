from apscheduler.schedulers.twisted import TwistedScheduler
from scrape import run_spider
from twisted.internet import reactor



if __name__ == "__main__":
    scheduler = TwistedScheduler()
    scheduler.add_job(run_spider, 'interval', minutes=5)
    scheduler.start()
    
    try:
        reactor.run()
    except (KeyboardInterrupt, SystemExit):
        pass