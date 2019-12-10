### 代码结构
![image](https://user-images.githubusercontent.com/16145883/70503160-c937b080-1b5d-11ea-8477-82ff68e438ea.png)

### 新增用户程序
* 把原来的测试代码删掉 bar_event_consumer, foo_item_consumer, baz_service_consumer, qux_status_consumers
* 在consumers.ConsumerBase，添加数据库连接，日志logger等对象
* 继承ItemConsumerBase,EventConsumerBase,ServiceConsumerBase,StatusConsumerBase类，然后在consumers.register_consumer 中注册新建加的类


