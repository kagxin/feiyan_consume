### 代码结构
![image](https://github.com/kagxin/feiyan_consume/blob/master/readme.jpg)

### 新增用户代码
* 把原来的测试代码删掉 bar_event_consumer, foo_item_consumer, baz_service_consumer, qux_status_consumers
* 在consumers.ConsumerBase，添加数据库连接，日志logger等对象
* 继承ItemConsumerBase,EventConsumerBase,ServiceConsumerBase,StatusConsumerBase类，然后在consumers.register_consumer 中注册新添加的类


