import os
import pyrax

home = os.environ['HOME']
creds = home + "/.pyrax"
logs = home + "/logs/cdn"

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credential_file(creds, region="ORD")
pyrax.authenticate()

cf = pyrax.cloudfiles
container = cf.get_container(".CDN_ACCESS_LOGS")
objects = container.get_objects()

for obj in objects:
    obj.download(logs, structure=False)
    obj.delete()
