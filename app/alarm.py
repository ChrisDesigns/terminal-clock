from app import app, Response
import time
from datetime import datetime, timedelta
from app.utility import returnClearScreen, convertTimeFormat

# generator functions - a bit hacky when it comes to threading
# goal will be to move towards something like aiohttp
def generateAlarm(delta=None):
    target_date = datetime.now() + delta
    while True:
        yield returnClearScreen()
        diff = target_date - datetime.now()
        yield "{}\n".format(convertTimeFormat(diff))
        # refresh every second
        time.sleep(1)

@app.route('/alarm/<min_till>/<sec_till>')
def alarmRoute(min_till=None, sec_till=None):
    if (min_till or sec_till):
        delta = timedelta(
            seconds=int(sec_till),
            minutes=int(min_till)
        )
        return Response(generateAlarm(delta), mimetype='text/plain')
    