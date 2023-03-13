from fastapi import APIRouter

from apis.route_list import routes_list

api_router = APIRouter()


for route in routes_list:
    api_router.include_router(route)
