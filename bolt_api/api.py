"""Core Django-Bolt API routes."""

from django_bolt import BoltAPI
from items.views import router as items_router

api = BoltAPI()
# FIXME: docs disappear when initializing the api instance with a prefix
# This might be happening only single api instances
# uncomment items/api.py and it will work
# api = BoltAPI(prefix="/api")


@api.get("/")
async def root():
    return {"message": "Hello World!"}


another_api = BoltAPI(prefix="/another-api")


@another_api.get("/get")
async def another_root():
    return {"message": "Hello from another world!"}


# FIXME: it's registered as "mount/path" as an invalid path
#  it might be better to enforce "/" prefix for mount calls
#  or can be added automatically?
api.mount("mount", another_api)

api.include_router(items_router)
