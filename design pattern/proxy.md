## 概念
为某个对象提供一个“代理”或“替身”，由代理对象控制对真实对象的访问。
## 分类
常见的代理模式有三种：
- 静态代理（在代码中手动编写代理类）
- 动态代理（JDK Proxy）（基于反射、InvocationHandler）
- CGLIB 动态代理（基于字节码生成，可代理没有接口的类）
## 例子
静态代理
```java
// 抽象接口
interface Subject {
    void request();
}

// 真实对象
class RealSubject implements Subject {
    @Override
    public void request() {
        System.out.println("真实对象处理请求");
    }
}

// 代理对象
class ProxySubject implements Subject {
    private RealSubject realSubject;

    public ProxySubject(RealSubject realSubject) {
        this.realSubject = realSubject;
    }

    @Override
    public void request() {
        System.out.println("代理：检查权限");
        realSubject.request();
        System.out.println("代理：记录日志");
    }
}

// 客户端
public class StaticProxyDemo {
    public static void main(String[] args) {
        RealSubject real = new RealSubject();
        Subject proxy = new ProxySubject(real);
        proxy.request();
    }
}
```
JDK动态代理
```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

// 抽象接口
interface Subject {
    void request();
}

// 真实对象
class RealSubject implements Subject {
    @Override
    public void request() {
        System.out.println("真实对象处理请求");
    }
}

// 动态代理处理器
class DynamicProxyHandler implements InvocationHandler {
    private Object target;

    public DynamicProxyHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("动态代理：检查权限");
        Object result = method.invoke(target, args);
        System.out.println("动态代理：记录日志");
        return result;
    }
}

// 客户端
public class DynamicProxyDemo {
    public static void main(String[] args) {
        RealSubject real = new RealSubject();

        Subject proxy = (Subject) Proxy.newProxyInstance(
                RealSubject.class.getClassLoader(),
                new Class[]{Subject.class},
                new DynamicProxyHandler(real));

        proxy.request();
    }
}
```
## 优点
- 代理可以在不修改原有类的情况下，增强功能（符合开闭原则）。
- 可以实现 AOP（面向切面编程），如 Spring 的事务、日志、权限控制。
- 动态代理避免了编写大量重复的代理类。
## 缺点
- 静态代理类多时，维护成本高。
- JDK 动态代理只能代理接口，不能代理类（需要 CGLIB 来解决）。
- 增加了系统复杂度。
## 使用场景
- 远程代理（RMI，RPC 调用）
- 虚拟代理（延迟加载，如大图片）
- 安全代理（权限检查）
- 智能代理（记录日志、统计方法执行时间）
- Spring AOP（事务、日志、权限控制）本质上就是 动态代理。
## 注意
- 代理模式（Proxy）的意图是控制对另一个对象的访问，例如实现懒加载或远程代理。同时，代理模式可以透明地增加缓存和权限校验功能，而无需修改原始接口源码。
- 代理模式降低了系统的耦合度。通过代理类可以将客户端与目标对象分离，实现更好的解耦。虽然代理模式会增加代码的复杂度，但不会提升调用性能。