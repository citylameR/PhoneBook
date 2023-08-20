import json


def contacts_to_json(contacts):
    output = []
    for contact in contacts:
        item = {
            'id': contact.id,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'company': contact.company,
            'work_phone': contact.work_phone,
            'personal_phone': contact.personal_phone
        }
        output.append(item)

    return json.dumps(output, indent=4, ensure_ascii=False)
