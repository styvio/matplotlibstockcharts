import requests
import json

import matplotlib.pyplot as plt

out = (requests.get("https://www.styvio.com/api/TDOC")).json()

plt.plot(out['maxStockValues'])
plt.show()
