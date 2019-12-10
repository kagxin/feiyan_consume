from consumers.status_consumers import StatusConsumerBase
from typing import *


class QuxStatusConsumer(StatusConsumerBase):

    def status_check(self, data):
        return data['status']['value'] == "1"

    def execute(self, data: Dict):
        """
            业务逻辑
        """
        print('status consumer example')
        self.m.get_collection('qux_status').insert(data)
