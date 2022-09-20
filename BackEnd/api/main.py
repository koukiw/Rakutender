from fastapi import FastAPI


from routers import sample, auth

from routers.event import create, show, id, event_join, my_event_list
from routers.category import show as category_show, detail as category_detail

app = FastAPI()

app.include_router(sample.router)
app.include_router(create.router)
app.include_router(show.router)
app.include_router(id.router)
app.include_router(event_join.router)
app.include_router(category_show.router)
app.include_router(category_detail.router)
app.include_router(my_event_list.router)

app.include_router(auth.router)
