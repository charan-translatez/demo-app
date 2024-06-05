from sanic import Sanic
from sanic.response import text
import os

app = Sanic(__name__)

@app.get("/")
async def root_path(request):
    return text("Ok!")

app.run(host="0.0.0.0", port=os.environ["PORT"], debug=True, access_log=False)