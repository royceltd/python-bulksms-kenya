import requests


def sendSMS(number, message, senderid, apikey):
    endpoint = "https://bulksms.roycetechnologies.co.ke/api/sendmessage"

    data = {'sender_id': senderid, 'text_message': message,
            'phone_number': number}
    headers = {
        "Authorization": "Bearer "+apikey}
    res = requests.post(endpoint, data=data, headers=headers)
    print(res)
