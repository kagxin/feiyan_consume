from .item_consumers.foo_item_consumer import FooItemConsumer
from .event_consumers.bar_event_consumer import BarEventConsumer
from .service_consumers.baz_service_consumer import BazSerivceConsumer
from .status_consumers.qux_status_consumers import QuxStatusConsumer

CONSUMERS_CLS = [
    FooItemConsumer,
    BarEventConsumer,
    BazSerivceConsumer,
    QuxStatusConsumer
]
