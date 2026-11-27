import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint , abort
from db import stores
from schemas import StoreSchema

blp=Blueprint(
    "stores", # if we want to create some relation between blueprint
    __name__, # uniques name
    description="Operations on Stores"
)

@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200,StoreSchema)
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store Not Found")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found")
    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def put(self,store_data,store_id):

        try:
            store = stores[store_id]
            store |= store_data
            return store
        except KeyError:
            abort(404, message="Item not Found")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self,store_data):

        for store in stores.values():
            if (
                    store_data["name"] == store["name"]
            ):
                abort(400, message=f"{store} already exists ")
        store_id = uuid.uuid4().hex  # unique identifier
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201


