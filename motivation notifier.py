from plyer import notification
import os
import time
import json
import random
CWD = os.getcwd()
filename = '%s/%s' % (CWD, 'quotes.json')
while True:
    with open(filename, encoding="utf8") as json_file:
        data = json.load(json_file)
        r = random.randint(0, len(data) - 1)
        Writer = data[r]['from']
        Quote = data[r]['text']

        notification.notify(title="MOTIVATOR",
                            message=Quote + "\n" "by" " " + Writer,
                            app_icon="C:\\Users\\FASNA\\PycharmProjects\\Nonstoppings\\Robsonbillponte-Sinem-File-Finder.ico",
                            timeout=10,
                            )
        time.sleep(12*60*60)


