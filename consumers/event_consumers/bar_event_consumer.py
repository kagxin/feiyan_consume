from consumers.event_consumers import EventConsumerBase


class BarEventConsumer(EventConsumerBase):

    def identifier(self):
        return 'DoorOpenAction'

    def execute(self, data):
        """
            业务逻辑
        """
        print('envent consumer example.')
        self.m.get_collection('bar_event').insert(data)
