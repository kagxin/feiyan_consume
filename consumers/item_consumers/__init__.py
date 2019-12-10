from consumers import ConsumerBase
from typing import *


class ItemConsumerBase(ConsumerBase):

    def items(self) -> Iterable[AnyStr]:
        """
            返回关注的字段的元组
        """
        return ()

    def item_check(self, data: Dict) -> bool:
        """
            检查所有的 items key 是否都在data['items']中
        """
        if self.items() and all(map(lambda k: k in data['items'].keys(), self.items())):
            return True

    def check(self, data: Dict) -> bool:
        """
            根据check的结果，确定是否执行execute
        """
        if 'items' not in data:
            return False

        return self.item_check(data)

    def execute(self, data: Dict):
        """
            业务逻辑
        """
        pass
