import os
import pyrax
from pyrax.exceptions import NoSuchObject

home = os.environ['HOME']
creds = home + "/.pyrax"
logs = home + "/logs/cdn"

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credential_file(creds, region="ORD")
print "Authenticating"...
pyrax.authenticate()

cf = pyrax.cloudfiles
print "Getting container..."
container = cf.get_container(".CDN_ACCESS_LOGS")
print "Getting objects..."
objects = container.get_objects()

print "Found %s objects to download" % len(objects)

for obj in objects:
    try:
        obj.download(logs, structure=False)
    except NoSuchObject, e:
        print "Couldn't download %s; %s" % (obj, e)
        continue

    try:
        obj.delete()
    except NoSuchObject, e:
        print "Couldn't delete %s; %s" % (obj, e)
