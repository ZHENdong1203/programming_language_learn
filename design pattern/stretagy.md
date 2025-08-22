## 概念
定义一系列算法（策略），将他们封装起来，并且使它们可以相互替换
## 结构
一般包含三个角色：
- 抽象策略：定义算法的接口
- 具体策略：实现不同的算法
- 环境类： 持有一个策略对象，并对外提供统一的调用入口
## 例子
```java
// 抽象策略
interface PaymentStrategy {
    void pay(int amount);
}

// 具体策略 - 支付宝支付
class AlipayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用支付宝支付：" + amount + " 元");
    }
}

// 具体策略 - 微信支付
class WeChatPayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用微信支付：" + amount + " 元");
    }
}

// 具体策略 - 信用卡支付
class CreditCardStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用信用卡支付：" + amount + " 元");
    }
}

// 环境类
class PaymentContext {
    private PaymentStrategy strategy;

    // 允许动态切换策略
    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void pay(int amount) {
        if (strategy == null) {
            throw new IllegalStateException("未设置支付策略");
        }
        strategy.pay(amount);
    }
}

// 客户端
public class StrategyPatternDemo {
    public static void main(String[] args) {
        PaymentContext context = new PaymentContext();

        // 使用支付宝
        context.setPaymentStrategy(new AlipayStrategy());
        context.pay(100);

        // 切换为微信
        context.setPaymentStrategy(new WeChatPayStrategy());
        context.pay(200);

        // 切换为信用卡
        context.setPaymentStrategy(new CreditCardStrategy());
        context.pay(300);
    }
}

```
## 优点
- 避免了大量的 if-else 或 switch-case。
- 可以方便地增加新的策略，而无需修改原有代码（符合开闭原则）。
- 策略可以灵活切换，扩展性好。
## 缺点
- 客户端需要知道所有策略，并手动选择合适的策略。
- 如果策略很多，类的数量会增加。
## 使用场景
- 一个系统需要动态选择不同的算法，比如支付方式、压缩算法、排序方式。
- 消除复杂的条件语句，避免 if-else 嵌套。
- 多个类的行为差别只在于算法或逻辑时，可以用策略模式替代继承。

## 策略模式和简单工厂模式结合
客户端的代码可以更简洁，只传参数，又工厂类选择要创建的具体策略。
```java
// 策略接口
interface PaymentStrategy {
    void pay(int amount);
}

// 具体策略 - 支付宝支付
class AlipayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用支付宝支付：" + amount + " 元");
    }
}

// 具体策略 - 微信支付
class WeChatPayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用微信支付：" + amount + " 元");
    }
}

// 具体策略 - 信用卡支付
class CreditCardStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用信用卡支付：" + amount + " 元");
    }
}

// 简单工厂 - 根据参数返回不同的策略
class PaymentStrategyFactory {
    public static PaymentStrategy getStrategy(String type) {
        if ("alipay".equalsIgnoreCase(type)) {
            return new AlipayStrategy();
        } else if ("wechat".equalsIgnoreCase(type)) {
            return new WeChatPayStrategy();
        } else if ("creditcard".equalsIgnoreCase(type)) {
            return new CreditCardStrategy();
        }
        throw new IllegalArgumentException("未知的支付方式: " + type);
    }
}

// 环境类
class PaymentContext {
    private PaymentStrategy strategy;

    public PaymentContext(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void pay(int amount) {
        strategy.pay(amount);
    }
}

// 客户端
public class StrategyFactoryDemo {
    public static void main(String[] args) {
        // 客户端只需告诉工厂支付方式
        PaymentStrategy strategy1 = PaymentStrategyFactory.getStrategy("alipay");
        PaymentContext context1 = new PaymentContext(strategy1);
        context1.pay(100);

        PaymentStrategy strategy2 = PaymentStrategyFactory.getStrategy("wechat");
        PaymentContext context2 = new PaymentContext(strategy2);
        context2.pay(200);

        PaymentStrategy strategy3 = PaymentStrategyFactory.getStrategy("creditcard");
        PaymentContext context3 = new PaymentContext(strategy3);
        context3.pay(300);
    }
}
```
工厂类的代码可以写在context类的构造函数中，使用switch语句根据传入的参数选择创建对应的策略。
```java
// 策略接口
interface PaymentStrategy {
    void pay(int amount);
}

// 具体策略 - 支付宝支付
class AlipayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用支付宝支付：" + amount + " 元");
    }
}

// 具体策略 - 微信支付
class WeChatPayStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用微信支付：" + amount + " 元");
    }
}

// 具体策略 - 信用卡支付
class CreditCardStrategy implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("使用信用卡支付：" + amount + " 元");
    }
}

// 环境类
class PaymentContext {
    PaymentStrategy strategy;

    public PaymentContext(String type) {
        switch (type) {
            case "Alipay":
                strategy = new AlipayStrategy();
                break;
            case "WeChat":
                strategy = new WeChatPayStrategy();
                break;
            case "CreditCard":
                strategy = new CreditCardStrategy();
                break;
        }
    }

    public void pay(int amount) {
        strategy.pay(amount);
    }
}

// 客户端
public class StrategyFactoryDemo {
    public static void main(String[] args) {
        // 客户端只需告诉工厂支付方式
        PaymentContext context1 = new PaymentContext("Alipay");
        context1.pay(100);

        PaymentContext context2 = new PaymentContext("WeChat");
        context2.pay(200);

        PaymentContext context3 = new PaymentContext("CreditCard");
        context3.pay(300);
    }
}
```
