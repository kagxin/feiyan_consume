from consumers.register_consumer import CONSUMERS_CLS
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial


def dispatch(d):
    for consumer_cls in CONSUMERS_CLS:
        _consumer = consumer_cls()
        if _consumer.check(d):
            _consumer.execute(d)


if __name__ == '__main__':
    """
    属性上报，
    事件上报，
    服务调用上报,
    在线状态上报
    """
    data = [
        {
            "deviceType": "AirPurifier",
            "iotId": "BJDL69fQU0ns5BphFXZQ000100",
            "requestId": "2455",
            "productKey": "a1oGhuzmqk8",
            "gmtCreate": 1573088799841,
            "deviceName": "wujiaw",
            "items": {
                "PM25": {
                    "value": 35,
                    "time": 1573088799842
                }
            },
        },
        {
            "deviceType": "SmartDoor",
            "identifier": "DoorOpenAction",
            "iotId": "Xzf15db9xxxxxxxxx01046b400",
            "name": "开门通知",
            "time": 1534319108982,
            "type": "info",
            "productKey": "a17xxxxTYNA",
            "deviceName": "Xzf15xxxxucTHBgUo6WR",
            "value": {
                "KeyID": "x8xxxxxkDY",
                "LockType": 3
            }
        },
        {
            "gmtCreate": 151111139881,
            "iotId": "4z819VQHxxxxxxxxxxxx7ee200",
            "productKey": "p1gsv0teUBd",
            "deviceName": "xxxxxxxxxx",
            "requestId": "1234",
            "code": 200,
            "message": "success",
            "topic": "/sys/p1gsv0teUBd/xxxxxxxxxx/thing/service/property/set",
            "data": {}
        },
        {
            "deviceType": "SmartDoor",
            "iotId": "Xzf15dxxxxxxxxxxxxxxxx01046b400",
            "action": "online",
            "productKey": "a17xxxxxxTYNA",
            "gmtCreate": 15311111368,
            "deviceName": "Xzf1xxxxxxxxxxxxgUo6WR",
            "status": {
                "time": 1534319611368,
                "value": "1"
            }
        }
    ]

    """
        可以将线程池替换为celery等其他并发消费方式
    """

    executor = ThreadPoolExecutor()
    for future in as_completed(map(partial(executor.submit, dispatch), data)):
        try:
            future.result()
        except Exception as e:
            print(str(e))
