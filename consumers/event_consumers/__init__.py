from consumers import ConsumerBase
from typing import *


class EventConsumerBase(ConsumerBase):

    def identifier(self) -> AnyStr:
        """
            事件标示
        """
        return ''

    def event_check(self, data: Dict) -> bool:
        """
            检查标示
        """
        return data['identifier'] == self.identifier()

    def check(self, data: Dict) -> bool:
        """
            根据check的结果，确定是否执行execute
        """
        if 'identifier' not in data:
            return False

        return self.event_check(data)

    def execute(self, data: Dict):
        """
            业务逻辑
        """
        pass
