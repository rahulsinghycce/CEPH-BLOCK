# CEPH-BLOCK
from the client side using "CURL" how to engage a CEPH RBD cluster to create a image/vol

CEPH-BLOCK-API
handling the API- CURL based call for provisioning from client side on SDS block image

From the client machine the user need to run the curl and get the vol created as,

curl -H 'Content-Type: application/json' -X POST -d '{"volume":"apivol13","pool":"cephclient","size":2}' http://0.0.0.0:5000/volume ( endpoint app will be dockerized )

output:

{ "pool": "cephclient", "size": 2, "status": "successful", "volume": "apivol13" }

On server end the app will excute :

# python runapp.py

Serving Flask app "runapp" (lazy loading)
Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Debug mode: on
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
Debugger PIN: 399-938-108 apivol13 cephclient 2 Connected to the cluster.
Creating a context for the 'data' pool 0.0.0.0 - -  "POST /volume HTTP/1.1" 200 -

User permissions needed:

ceph auth add client.rahul mon 'allow r' osd 'allow rw pool=ceph-pool' mgr 'allow *'

Dependencies:

Python 2.7

Flask 1.1.1

rbd

rados
