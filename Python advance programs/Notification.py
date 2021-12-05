import time
from plyer import notification

while True:
    #notification
    notification.notify(title="Alert!!!",message="Drink water",timeout=5)
    time.sleep(1800)
