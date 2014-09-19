import os
import ConfigParser

from celery import Celery


app_ini = '%s.ini' % os.environ.get('ENV', 'development')

config = ConfigParser.RawConfigParser()
config.read(app_ini)

celery = Celery('reviewq.celery',
                broker=config.get('celery', 'broker'),
                backend=config.get('celery', 'backend'),
                include=['reviewq.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(
    CELERY_BACKEND_TRANSPORT_OPTIONS=config.get('celery', 'backend_transport_options'),
)

if __name__ == '__main__':
    celery.start()