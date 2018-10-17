import os, sys
import ConfigParser

ENV_CONFIG = {
    'dev': 'dev',
    'prod': 'prod',
    'staging': 'staging'
}

#ENV = os.getenv('ENV', 'prod')

ENV=os.environ["ENV"]

print ENV

def load_env_configuration(env):
    if not env:
        print('Please define the ENV')
        sys.exit(1)
    config = ConfigParser.RawConfigParser()
    config.read((os.path.join(os.getcwd(), 'configs/%s.cfg' % ENV_CONFIG[env])))
    return config

global configp

configp = load_env_configuration(ENV)
try:
    configp.set('rabbitmq', 'ip', os.environ['RABBITMQ_HOST'])
    configp.set('rabbitmq', 'username', os.environ['RABBITMQ_DEFAULT_USER'])
    configp.set('rabbitmq', 'password', os.environ['RABBITMQ_DEFAULT_PASS'])
    configp.set('mysql', 'ip', os.environ['MYSQL_HOST'])
    configp.set('mysql', 'username', os.environ['MYSQL_DEFAULT_USER'])
    configp.set('mysql', 'password', os.environ['MYSQL_DEFAULT_PASS'])
except:
    pass
