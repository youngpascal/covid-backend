import os

BOT_NAME = 'covid'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
SQLALCHEMY_DATABASE_URI = 'postgres://ibziasnfwnuxns:a932844f0441c0ef944c2c238850446f8ca3eaab43f6bffe74f812b6729a9faf@ec2-3-230-106-126.compute-1.amazonaws.com:5432/dcu38i64pte8r3'

#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False





ITEM_PIPELINES = {'scraper.pipelines.TutorialPipeline': 300}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


