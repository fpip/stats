import pyrax

pyrax.set_credential_file('~/.pyrax')
pyrax.authenticate()
cf_ord = pyrax.connect_to_cloudfiles(region="ORD")
container = cf_ord.get_container(".ACCESS_LOGS")
objects = container.get_objects()
for obj in objects:
    obj.download("~/logs/cdn", structure=False)
    obj.delete()
