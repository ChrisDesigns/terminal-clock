from app import app, Response
import time
from datetime import datetime
from app.utility import returnClearScreen, returnClock


# generator functions - a bit hacky when it comes to threading
# goal will be to move towards something like aiohttp
def generateClock():
    while True:
        yield returnClearScreen()
        now = datetime.now()
        yield returnClock(str(now.hour), str(now.minute))
        # refresh every second
        time.sleep(1)

@app.route('/clock')
def clockRoute():
    return Response(generateClock(), mimetype='text/plain')