import json
import requests

API_URL = "http://127.0.0.1:8000/api/ingest"

with open("email-data-advanced.json", "r", encoding="utf-8") as f:
    emails = json.load(f)

success = 0
failed = 0

for email in emails:

    try:

        response = requests.post(
            API_URL,
            json=email,
            timeout=10,
        )

        if response.status_code in (200, 201, 202):

            success += 1

            print(
                f"✓ {email['message_id']} : {response.status_code}"
            )

        else:

            failed += 1

            print(
                f"✗ {email['message_id']} : {response.status_code}"
            )

            print(response.text)

    except Exception as e:

        failed += 1

        print(
            f"✗ {email['message_id']} : {e}"
        )

print("\n-------------------------")
print(f"Success : {success}")
print(f"Failed  : {failed}")
print("-------------------------")