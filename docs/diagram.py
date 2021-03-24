from diagrams import Diagram
from diagrams.k8s.compute import Pod
from diagrams.onprem.database import PostgreSQL


with Diagram('docs/drink-delivery-api', show=False):
    drik_delivery_api = Pod('api')
    drik_delivery_db = PostgreSQL("database")

    drik_delivery_api >> drik_delivery_db
    drik_delivery_db >> drik_delivery_api
