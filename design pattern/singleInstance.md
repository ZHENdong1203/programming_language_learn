# 单例设计模式
单例模式主要是为了避免因为创建了多个实例造成资源的浪费，且多个实例由于多次调用容易导致结果出现错误，而使用单例模式能够保证整个应用中有且只有一个实例。
## 1.保证对象的唯一性
* 不允许其他程序new对象
* 在该类中创建对象
* 对外提供一个可以让其他程序获取该对象的方法
## 2.实现单例模式
* 构造函数私有化
* 通过new在本类中创建一个对象
* 定义一个公共方法，将该类创建的对象返回
## 3.代码实现
### 饿汉式
含义：类加载的时候就创建单例对象，不管是否会用到

特点： 
- 写法简单，线程安全（因为类加载的时候就初始化了）
- 如果实例始终没有被用到，可能造成内存浪费
```java
public class Singleton {
    // 类加载时就创建
    private static final Singleton instance = new Singleton();

    // 私有构造方法
    private Singleton() {}

    // 获取实例的方法
    public static Singleton getInstance() {
        return instance;
    }
}
```
### 懒汉式
含义：第一次调用getInstance方法的时候才创建单例对象。

特点：
- 延迟加载，节省资源
- 多线程下需要处理同步问题，否则可能出现多个实例。
- 保证线程安全，使用双重检查锁定
```java
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) { 
            synchronized (Singleton.class) {
                if (instance == null) { 
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```
### 内部类
和饿汉式类似，但是使用内部类可以在需要的时候才创建单例对象。
```java
public class Singleton {

    private Singleton() {
    }

    private static class SingletonHodler {
        private static Singleton singleton = new Singleton();
    }

    public static Singleton getInstance() {
        return SingletonHodler.singleton;
    }
}
```
### 枚举
使用枚举实现单例：
* 线程安全：枚举类在类加载时就会实例化，和饿汉式类似，天然线程安全。
* 防止反射破坏：反射无法通过 Constructor 强行创建新的枚举实例。
* 防止反序列化破坏：反序列化时，枚举会自动保证单例（不会创建新对象）。普通的单例类如果实现了 Serializable，在反序列化时会重新创建实例，而枚举不会。
```java
public enum Singleton {
    INSTANCE;  // 唯一实例

    // 你可以定义一些方法
    public void doSomething() {
        System.out.println("枚举单例方法被调用");
    }
}
```
使用方式：
```java
public class Test {
    public static void main(String[] args) {
        Singleton s1 = Singleton.INSTANCE;
        Singleton s2 = Singleton.INSTANCE;

        System.out.println(s1 == s2); // true，保证单例

        s1.doSomething(); // 调用方法
    }
}
```


