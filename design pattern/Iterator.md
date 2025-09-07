## 概念
迭代器模式（Iterator Pattern） 是一种行为型设计模式，它提供一种方法顺序访问一个聚合对象中的元素，而不暴露该对象的内部表示。

常见应用：
- Java 自带的 Iterator 接口就是迭代器模式的典型实现。
- 用在集合类（List、Set、Map）中。

## 结构
- Iterator（抽象迭代器）: 定义访问和遍历元素的接口（如 hasNext()、next()）。
- ConcreteIterator（具体迭代器）: 实现迭代器接口，完成元素的遍历。
- Aggregate（抽象聚合）: 定义一个创建迭代器对象的接口。
- ConcreteAggregate（具体聚合）: 实现创建迭代器的方法，返回一个具体迭代器对象。

## 例子
```java
import java.util.*;

// 抽象迭代器
interface IteratorCustom<T> {
    boolean hasNext();
    T next();
}

// 抽象聚合
interface Aggregate<T> {
    IteratorCustom<T> createIterator();
}

// 具体聚合：学生集合
class StudentAggregate implements Aggregate<String> {
    private final List<String> students = new ArrayList<>();

    public void addStudent(String name) {
        students.add(name);
    }

    public void removeStudent(String name) {
        students.remove(name);
    }

    @Override
    public IteratorCustom<String> createIterator() {
        return new StudentIterator(students);
    }
}

// 具体迭代器
class StudentIterator implements IteratorCustom<String> {
    private final List<String> students;
    private int position = 0;

    public StudentIterator(List<String> students) {
        this.students = students;
    }

    @Override
    public boolean hasNext() {
        return position < students.size();
    }

    @Override
    public String next() {
        return students.get(position++);
    }
}

// 测试类
public class IteratorPatternDemo {
    public static void main(String[] args) {
        StudentAggregate aggregate = new StudentAggregate();
        aggregate.addStudent("Alice");
        aggregate.addStudent("Bob");
        aggregate.addStudent("Charlie");

        IteratorCustom<String> iterator = aggregate.createIterator();

        System.out.println("学生名单：");
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
```

双向迭代器
```java
import java.util.*;

// 抽象迭代器（双向）
interface BidirectionalIterator<T> {
    boolean hasNext();
    T next();
    boolean hasPrevious();
    T previous();
}

// 抽象聚合
interface Aggregate<T> {
    BidirectionalIterator<T> createIterator();
}

// 具体聚合：学生集合
class StudentAggregate implements Aggregate<String> {
    private final List<String> students = new ArrayList<>();

    public void addStudent(String name) {
        students.add(name);
    }

    public void removeStudent(String name) {
        students.remove(name);
    }

    @Override
    public BidirectionalIterator<String> createIterator() {
        return new StudentBidirectionalIterator(students);
    }
}

// 具体迭代器（双向）
class StudentBidirectionalIterator implements BidirectionalIterator<String> {
    private final List<String> students;
    private int position = -1; // 初始在第一个元素之前

    public StudentBidirectionalIterator(List<String> students) {
        this.students = students;
    }

    @Override
    public boolean hasNext() {
        return position < students.size() - 1;
    }

    @Override
    public String next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return students.get(++position);
    }

    @Override
    public boolean hasPrevious() {
        return position > 0;
    }

    @Override
    public String previous() {
        if (!hasPrevious()) {
            throw new NoSuchElementException();
        }
        return students.get(--position);
    }
}

// 测试类
public class BidirectionalIteratorDemo {
    public static void main(String[] args) {
        StudentAggregate aggregate = new StudentAggregate();
        aggregate.addStudent("Alice");
        aggregate.addStudent("Bob");
        aggregate.addStudent("Charlie");
        aggregate.addStudent("Diana");

        BidirectionalIterator<String> iterator = aggregate.createIterator();

        System.out.println("正向遍历:");
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

        System.out.println("\n反向遍历:");
        while (iterator.hasPrevious()) {
            System.out.println(iterator.previous());
        }
    }
}
```
## 优点
- 支持以不同方式遍历一个聚合对象（比如正序、逆序）。
- 封装了集合的内部表示，客户端只需使用迭代器。
- 遍历过程由迭代器独立完成，简化了聚合类。

## 缺点
- 增加了类的个数。
- 如果集合特别复杂，迭代器实现起来可能比较麻烦。