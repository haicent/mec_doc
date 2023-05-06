
import requests
import json
class DingTalk_Base:
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=25346a136b72e2ce378068aee8f82ebdd510d1c4ba6a5dd3f8ce633bc104142e'
    def send_msg(self,text):
        json_text = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": [
                    ""
                ],
                "isAtAll": True
            }
        }
        return requests.post(self.url, json.dumps(json_text), headers=self.__headers).content
class DingTalk_Disaster(DingTalk_Base):
    def __init__(self):
        super().__init__()
        # 填写机器人的url
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=25346a136b72e2ce378068aee8f82ebdd510d1c4ba6a5dd3f8ce633bc104142e'
if __name__ == '__main__':
    ding = DingTalk_Disaster()
    ding.send_msg('文档，MEC doc updated:\n http://doc.hiacent.info/\n')
