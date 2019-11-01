import string
from subprocess import call
from random import SystemRandom

call(['git', 'clone', 'https://github.com/Changggg/ecopad_portal', 'data/static/portal'])
call(['git', 'clone', 'https://github.com/Changggg/ecopad_api', 'api_code']) # -v /api /usr/


# Generate secrets on creation
with open(r'config/ssl/backend/keystoresecret', 'w') as f:
    f.write(''.join(SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(32)))

call(['docker', 'build', '--rm', '-t', 'cybercom/openssl', 'config/ssl/openssl/'])
call(['run/genSSLKeys'])
