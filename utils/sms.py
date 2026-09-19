import requests

def send_sms_alert(phone_number, name):
    """Sends a real SMS using Fast2SMS OTP Route"""
    url = "https://www.fast2sms.com/dev/bulkV2"
    FAST2SMS_KEY = "beEDaCwcKzNuv1sqU0hfGJn6HoPT2LpSBtjYXFxVAOmWl58iZybxnPSso3gmjZ0kAyrzMq6CGJDEfiad" 
    
    payload = {
        "route": "v3",
        "sender_id": "TXTIND",
        "message": f"Hello {name}, welcome to AgriTrustX. Your secure market and weather shield is active.",
        "language": "english",
        "flash": 0,
        "numbers": phone_number
    }
    headers = {
        "authorization": FAST2SMS_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code == 200
    except:
        return False