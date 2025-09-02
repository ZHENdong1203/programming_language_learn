## 概念
用一个已经存在的对象作为原型，通过 复制（clone） 来创建新的对象，而不是通过 new。这样可以避免复杂对象的重复初始化，提高性能。
## 结构
原型模式一般包含两个角色：
- 抽象原型（Prototype）：声明 clone() 方法。
- 具体原型（ConcretePrototype）：实现 clone() 方法，可以返回自身的拷贝。
## 例子
Java 中 Object 类已经提供了 clone() 方法（浅拷贝），只要类实现 Cloneable 接口，就能用原型模式。
浅拷贝
```java
class Resume implements Cloneable {
    private String name;
    private int age;
    private String workExperience;

    public Resume(String name, int age, String workExperience) {
        this.name = name;
        this.age = age;
        this.workExperience = workExperience;
    }

    public void show() {
        System.out.println(name + " | 年龄: " + age + " | 工作经验: " + workExperience);
    }

    @Override
    protected Resume clone() {
        try {
            return (Resume) super.clone(); // 浅拷贝
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }
}

public class PrototypeDemo {
    public static void main(String[] args) {
        Resume r1 = new Resume("张三", 25, "2年Java开发经验");
        Resume r2 = r1.clone(); // 克隆一个副本
        Resume r3 = r1.clone();

        r1.show();
        r2.show();
        r3.show();
    }
}
```
深拷贝
```java
import java.util.ArrayList;
import java.util.List;

// 学生类
class Student implements Cloneable {
    private String name;
    private int age;
    private List<String> courses; // 引用类型字段

    public Student(String name, int age, List<String> courses) {
        this.name = name;
        this.age = age;
        this.courses = courses;
    }

    public void addCourse(String course) {
        this.courses.add(course);
    }

    public void showInfo() {
        System.out.println("姓名: " + name + ", 年龄: " + age + ", 课程: " + courses);
    }

    // 深拷贝（手动复制）
    @Override
    protected Student clone() {
        try {
            // 先浅拷贝基本字段
            Student copy = (Student) super.clone();
            // 再手动拷贝引用类型字段
            copy.courses = new ArrayList<>(this.courses);
            return copy;
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }
}

// 测试
public class DeepCloneManualDemo {
    public static void main(String[] args) {
        List<String> courses = new ArrayList<>();
        courses.add("Java");
        courses.add("数据库");

        Student s1 = new Student("李四", 21, courses);

        // 深拷贝
        Student s2 = s1.clone();

        // 修改 s1 的课程
        s1.addCourse("操作系统");

        System.out.println("=== 原始对象 ===");
        s1.showInfo();

        System.out.println("=== 深拷贝对象 ===");
        s2.showInfo();
    }
}
```
深拷贝可以通过实现序列化接口的方式实现
```java
import java.io.*;
import java.util.ArrayList;
import java.util.List;

// 学生类
class Student implements Cloneable, Serializable {
    private String name;
    private int age;
    private List<String> courses; // 引用类型字段

    public Student(String name, int age, List<String> courses) {
        this.name = name;
        this.age = age;
        this.courses = courses;
    }

    public void addCourse(String course) {
        this.courses.add(course);
    }

    public void showInfo() {
        System.out.println("姓名: " + name + ", 年龄: " + age + ", 课程: " + courses);
    }

    // 浅拷贝
    @Override
    protected Student clone() {
        try {
            return (Student) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }

    // 深拷贝（通过序列化实现）
    public Student deepClone() {
        try {
            // 写入字节流
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos);
            oos.writeObject(this);

            // 读取字节流
            ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
            ObjectInputStream ois = new ObjectInputStream(bis);
            return (Student) ois.readObject();

        } catch (IOException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}

// 测试
public class DeepCloneDemo {
    public static void main(String[] args) {
        List<String> courses = new ArrayList<>();
        courses.add("Java");
        courses.add("数据库");

        Student s1 = new Student("张三", 20, courses);

        // 浅拷贝
        Student s2 = s1.clone();

        // 深拷贝
        Student s3 = s1.deepClone();

        // 修改 s1 的课程
        s1.addCourse("操作系统");

        System.out.println("=== 原始对象 ===");
        s1.showInfo();

        System.out.println("=== 浅拷贝对象 ===");
        s2.showInfo();

        System.out.println("=== 深拷贝对象 ===");
        s3.showInfo();
    }
}
```
## 浅拷贝
- 被复制对象的所有变量都含有与原来的对象相同的值，而所有的对其他对象的引用都仍然指向原来的对象。
- 只复制对象本身和基本类型字段，如果对象里有引用类型字段（比如数组、集合），只会复制引用，指向同一块内存。
## 深拷贝
- 不仅复制对象本身，还会递归复制引用类型字段，生成完全独立的副本。
- 不仅复制对象本身，还会递归复制引用类型字段，生成完全独立的副本。
## 优点
- 快速复制对象，性能比 new 更高（尤其是复杂对象）。
- 隔离了对象创建过程，客户端不用知道创建细节。
## 缺点
- 必须实现 Cloneable 并重写 clone()，有一定侵入性。
- 深拷贝实现较复杂。
## 使用场景
- 需要频繁创建相似对象（比如游戏中的怪物、地图元素）。
- 初始化代价大（如配置类、数据库连接信息）。
- 需要保存对象状态，并在后续快速恢复。
