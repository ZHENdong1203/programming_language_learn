## 概念
组合模式（Composite Pattern）是一种结构型设计模式，它将对象组合成树形结构来表示“部分-整体”的层次结构。组合模式使客户端可以以统一的方式对待单个对象和对象组合。

常用场景：
- 文件系统（文件和文件夹）
- 图形绘制（图形和组合图形）
- 组织架构（员工和部门）

## 结构
- Component（抽象组件）: 定义了所有对象的公共接口，可以是叶子对象或容器对象。
- Leaf（叶子节点）: 叶子节点，没有子节点，实现具体操作。
- Composite（容器节点）: 容器节点，有子节点，实现组合操作。

## 例子
```java
import java.util.ArrayList;
import java.util.List;

// 抽象组件
abstract class Employee {
    protected String name;
    protected double salary;

    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    public abstract void showDetails();
}

// 叶子节点
class Developer extends Employee {
    public Developer(String name, double salary) {
        super(name, salary);
    }

    @Override
    public void showDetails() {
        System.out.println("Developer: " + name + ", Salary: " + salary);
    }
}

class Manager extends Employee {
    public Manager(String name, double salary) {
        super(name, salary);
    }

    @Override
    public void showDetails() {
        System.out.println("Manager: " + name + ", Salary: " + salary);
    }
}

// 容器节点
class Department extends Employee {
    private final List<Employee> employees = new ArrayList<>();

    public Department(String name) {
        super(name, 0); // 部门本身不关心工资
    }

    public void add(Employee e) {
        employees.add(e);
    }

    public void remove(Employee e) {
        employees.remove(e);
    }

    @Override
    public void showDetails() {
        System.out.println("Department: " + name);
        for (Employee e : employees) {
            e.showDetails();
        }
    }
}

// 测试类
public class CompositePatternDemo {
    public static void main(String[] args) {
        Developer dev1 = new Developer("Alice", 5000);
        Developer dev2 = new Developer("Bob", 6000);
        Manager man1 = new Manager("Charlie", 8000);

        Department devDept = new Department("Development");
        devDept.add(dev1);
        devDept.add(dev2);

        Department headDept = new Department("Head Office");
        headDept.add(man1);
        headDept.add(devDept);

        headDept.showDetails();
    }
}
```
在组合模式中：
- 安全方式（Safe）：叶子节点不提供 add/remove 方法，只能容器节点使用。
- 透明方式（Transparent）：在抽象组件（Component）中统一声明 add/remove 方法，叶子节点也会有这些方法（通常抛异常或不实现），客户端统一调用即可。
```java
import java.util.ArrayList;
import java.util.List;

// 抽象组件
abstract class Graphic {
    protected String name;

    public Graphic(String name) {
        this.name = name;
    }

    // 绘制方法
    public abstract void draw();

    // 透明方式统一声明 add/remove
    public void add(Graphic g) {
        throw new UnsupportedOperationException("不支持添加操作");
    }

    public void remove(Graphic g) {
        throw new UnsupportedOperationException("不支持删除操作");
    }
}

// 叶子节点
class Circle extends Graphic {
    public Circle(String name) {
        super(name);
    }

    @Override
    public void draw() {
        System.out.println("绘制圆形: " + name);
    }
}

class Rectangle extends Graphic {
    public Rectangle(String name) {
        super(name);
    }

    @Override
    public void draw() {
        System.out.println("绘制矩形: " + name);
    }
}

// 容器节点
class CompositeGraphic extends Graphic {
    private final List<Graphic> children = new ArrayList<>();

    public CompositeGraphic(String name) {
        super(name);
    }

    @Override
    public void draw() {
        System.out.println("组合图形: " + name + " 包含以下子图形:");
        for (Graphic g : children) {
            g.draw();
        }
    }

    @Override
    public void add(Graphic g) {
        children.add(g);
    }

    @Override
    public void remove(Graphic g) {
        children.remove(g);
    }
}

// 测试类
public class TransparentCompositeDemo {
    public static void main(String[] args) {
        // 创建叶子节点
        Graphic circle1 = new Circle("Circle 1");
        Graphic rect1 = new Rectangle("Rectangle 1");

        // 创建组合节点
        CompositeGraphic composite1 = new CompositeGraphic("Composite 1");
        composite1.add(circle1);
        composite1.add(rect1);

        // 创建更大的组合
        CompositeGraphic composite2 = new CompositeGraphic("Composite 2");
        composite2.add(new Circle("Circle 2"));
        composite2.add(composite1); // 可以直接添加组合节点

        // 绘制整个组合图形
        composite2.draw();
    }
}
```
## 优点
- 统一了对单个对象和组合对象的操作。
- 对树形结构的处理更加清晰。
## 缺点
- 设计较复杂，增加了系统的抽象性。
- 对于叶子节点和容器节点的区别可能增加理解成本。