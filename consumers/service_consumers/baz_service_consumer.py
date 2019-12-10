from consumers.service_consumers import ServiceConsumerBase


class BazSerivceConsumer(ServiceConsumerBase):

    def service_check(self, data):
        if 'productKey' in data and data['productKey'] == 'p1gsv0teUBd':
            return True
        return False

    def execute(self, data):
        print('service consumer example')
        self.m.get_collection('baz_service').insert(data)
