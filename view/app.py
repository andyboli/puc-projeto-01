from controller import (reader)
from database import (connection)
import matplotlib.pyplot as plt
import numpy as np


def app():
    print(reader.lang('main_title'))
    connection.run()
    # Data
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    plt.plot(xpoints, ypoints)
    plt.savefig("mygraph.png")
