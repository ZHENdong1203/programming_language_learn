# 简单工厂模式
## 概念
由一个工厂类根据传入的参数，决定创建哪一种产品类的实例
## 结构
简单工厂模式包含三个部分：
- 抽象产品：定义所有产品的共同接口或抽象类
- 具体产品：实现抽象产品的具体类
- 工厂类：提供一个静态方法，根据传入的参数决定创建哪种具体产品
## 例子
```java
// 抽象产品
interface Shape {
    void draw();
}

// 具体产品 - 圆形
class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("画一个圆形");
    }
}

// 具体产品 - 方形
class Square implements Shape {
    @Override
    public void draw() {
        System.out.println("画一个方形");
    }
}

// 具体产品 - 三角形
class Triangle implements Shape {
    @Override
    public void draw() {
        System.out.println("画一个三角形");
    }
}

// 工厂类
class ShapeFactory {
    // 简单工厂的核心方法
    public static Shape createShape(String type) {
        if ("circle".equalsIgnoreCase(type)) {
            return new Circle();
        } else if ("square".equalsIgnoreCase(type)) {
            return new Square();
        } else if ("triangle".equalsIgnoreCase(type)) {
            return new Triangle();
        }
        return null;
    }
}

// 客户端
public class SimpleFactoryDemo {
    public static void main(String[] args) {
        Shape shape1 = ShapeFactory.createShape("circle");
        shape1.draw();

        Shape shape2 = ShapeFactory.createShape("square");
        shape2.draw();

        Shape shape3 = ShapeFactory.createShape("triangle");
        shape3.draw();
    }
}

```
## 优点
- 通过工厂封装了对象创建过程，客户端不用关心具体类名。
- 实例化对象集中管理，便于维护。
## 缺点
- 不符合开闭原则：如果新增产品（比如 Rectangle），必须修改工厂类代码。
- 工厂类职责过重，所有对象的创建都要依赖它，容易变得复杂。
## 使用场景
- 需要创建的对象较少。
- 客户端不想关心具体对象的创建过程。比如：日志类、图形类、数据库连接等场景。