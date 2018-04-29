import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import quandl
from pyfont import pyfont
from matplotlib.pyplot import style
style.use("ggplot")
quandl.ApiConfig.api_key = "ZAFoDrTr19ayeaJDrttM"

df = quandl.get("LPPM/PLAT")


ydata = df["GBP AM"]
ax = plt.subplot(111, facecolor = "lightslategray")

ax.set_xlabel(pyfont.pyfont.convert("Date", "sorcerer"))
ax.set_ylabel(pyfont.pyfont.convert('GBP PRICE OF PLATINUM', "sorcerer"))
t = pyfont.pyfont.convert("GBP AM PLATINUM", "sorcerer")
title = ax.set_title(pyfont.pyfont.convert("GBP AM PLATINUM", "sorcerer"))

ax.grid(True)

plt.plot(ydata)
plt.show()
