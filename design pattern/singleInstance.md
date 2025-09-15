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
## 注意
- 在双重检查锁定（DCL）实现中，使用volatile关键字修饰单例实例变量是必须的，因为它可以防止指令重排序问题，确保线程安全（在Java 5及以上版本的内存模型中）。
- 单例模式的设计初衷是为了确保一个类只有一个实例,并不是为了提高系统性能。事实上,对于不需要频繁创建和销毁的对象,我们有其他更合适的设计模式和优化方案。
- 饿汉式：线程安全且无需显式同步，但实例在类加载时初始化，不符合延迟加载。 
- 懒汉式：线程安全且延迟加载，但使用synchronized方法，属于显式同步。 
- 双重检查锁定加volatile：线程安全且延迟加载，但使用synchronized块，属于显式同步，不符合要求。 
- 静态内部类单例：线程安全（由JVM类加载机制保证），延迟加载（通过静态内部类的加载机制实现，仅在首次调用getInstance时初始化实例），且无需显式同步（无synchronized代码）。
- 在 Java 中实现单例，要求：惰性加载；在高并发下基本零运行时同步开销；实现简单、易读；不特别关心反序列化或反射攻击。
    - synchronized懒汉式：存在同步开销，高并发下性能差，不满足基本零运行时同步开销要求。 
    - 使用volatile的双重检查锁：支持惰性加载，高并发下仅首次创建有同步开销，之后基本零开销，但实现相对复杂（需volatile和双重检查），易读性较差
    - 静态内部类Holder模式：支持惰性加载（类加载机制保证首次调用时初始化），无任何同步代码，高并发下零运行时同步开销，实现简洁易读，完美满足所有要求。 
    - 枚举实现单例：非惰性加载（枚举常量在类加载时初始化），不符合惰性加载要求。 
- Spring框架中的bean默认是单例的,通过IOC容器来管理这些单例对象的生命周期。当使用@Autowired注解进行依赖注入时,容器会确保注入的是同一个单例对象,这完全符合单例模式的设计理念。
