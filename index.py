from controller import (reader)
from database import (connection as cnc)
from dash import (Dash, html, dcc)
from plotly import (express as px)
from view import (app)

import pandas as pd


connection = cnc.run()


if __name__ == "__main__":
    app.run_view()


# connection.run()
