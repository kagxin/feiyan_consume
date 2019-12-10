# from consumers import ConsumerBase

from consumers import ConsumerBase
from typing import *


class StatusConsumerBase(ConsumerBase):

    def status_check(self, data: Dict) -> bool:
        return True

    def check(self, data: Dict) -> bool:
        """
            根据check的结果，确定是否执行execute
        """
        if 'status' not in data:
            return False

        return self.status_check(data)

    def execute(self, data: Dict):
        """
            业务逻辑
        """
        pass
