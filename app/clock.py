from app import app, Response, request
import time
from datetime import datetime
from app.utility import returnClearScreen, returnClock
from app.timezone import processTZ, convertTZ

# generator functions - a bit hacky when it comes to threading
# goal will be to move towards something like aiohttp
def generateClock(timezone=None, ip=None):
    timezone = processTZ(timezone, ip)
    while True:
        yield returnClearScreen()
        now = convertTZ(datetime.now(), timezone)
        yield returnClock(now.hour, now.minute)
        # refresh every second
        time.sleep(1)

@app.route('/clock')
def clockRoute():
    tz = request.args.get('tz')
    ip = request.environ.get('X-Real-IP', request.remote_addr)
    return Response(generateClock(tz, ip), mimetype='text/plain')