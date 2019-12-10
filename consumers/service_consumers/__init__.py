# from consumers import ConsumerBase

from consumers import ConsumerBase
from typing import *


class ServiceConsumerBase(ConsumerBase):

    def service_check(self, data: Dict) -> bool:
        return True

    def check(self, data: Dict) -> bool:
        """
            根据check的结果，确定是否执行execute
        """
        if 'code' not in data:
            return False

        return self.service_check(data)

    def execute(self, data: Dict):
        """
            业务逻辑
        """
        pass
