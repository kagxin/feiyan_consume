from consumers.item_consumers import ItemConsumerBase


class FooItemConsumer(ItemConsumerBase):

    def items(self):
        return 'PM25',

    def execute(self, data):
        self.m.pm25.insert(data)
        print('item consumer example')
