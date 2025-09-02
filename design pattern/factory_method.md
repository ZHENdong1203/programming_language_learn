## 概念
定义一个创建对象的接口，让子类决定实例化哪一个类。工厂方法模式使得对象的创建延迟到子类中进行。
## 结构
工厂方法模式一般包含四个角色：
- 抽象产品（Product）：定义产品的抽象接口。
- 具体产品（ConcreteProduct）：实现抽象产品的具体类。
- 抽象工厂（Factory）：定义工厂的抽象接口。
- 具体工厂（ConcreteFactory）：实现工厂接口，负责创建某种具体产品。

符合开闭原则
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

// 抽象工厂
interface ShapeFactory {
    Shape createShape();
}

// 具体工厂 - 生产圆形
class CircleFactory implements ShapeFactory {
    @Override
    public Shape createShape() {
        return new Circle();
    }
}

// 具体工厂 - 生产方形
class SquareFactory implements ShapeFactory {
    @Override
    public Shape createShape() {
        return new Square();
    }
}

// 客户端
public class FactoryMethodDemo {
    public static void main(String[] args) {
        // 使用圆形工厂
        ShapeFactory circleFactory = new CircleFactory();
        Shape circle = circleFactory.createShape();
        circle.draw();

        // 使用方形工厂
        ShapeFactory squareFactory = new SquareFactory();
        Shape square = squareFactory.createShape();
        square.draw();
    }
}
```

