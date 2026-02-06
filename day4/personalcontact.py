contact={
    "Karna":123456789,
    "rahul":987654321,
    "manya":456789123
    }
print(contact)
contact.update({"Keshav":12345612345})
print(contact.items())
contact.update({"Karna":92343312345})
print(contact.get("Karna","Contact not found"))
print(contact.get("Rajiv","Contact not found"))
for k,v in contact.items():
    print(f"Contacts:{k} Phone:{v}")
