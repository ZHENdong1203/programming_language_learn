# Java
## 1. java标识符
* 标识符以字母，美元符号和下划线开头
* 首字符之后可以是字母，美元符号，下划线和数字的任意组合
* 大小写敏感
* 关键字不能做标识符
## 2. java注释
单行注释
使用`//`开始

多行注释
以`/*`开始，以`*/`结束

文档注释
以`/**`开始，以`*/`结束
## 3. java对象和类
* 类（Class），定义对象的属性和方法。
* 对象（Object），类的实例。
* 继承，一个类可以继承另一个类的属性和方法。
* 封装，将对象的字段私有化，通过公共方法访问。
* 多态，通过方法重载和方法重写实现。
* 抽象，使用抽象类和接口来定义必须实现的方法，不提供具体实现。
* 接口（Interface），定义类必须实现的方法，支持多重继承。
* 方法，定义类的行为，包含类中的函数。
* 方法重载（overload），同一个类中可以有多个同名的方法，但是参数不同。

类的变量
* 局部变量：在方法，构造方法或者语句块中定义的变量为局部变量。变量声明和初始化都在方法中，方法结束后，变量就会自动销毁。
* 成员变量：成员变量定义在类中，方法体之外的变量。这种变量在创建对象的时候实例化。成员变量可以被类中的方法，构造方法和特定类的语句块访问。
* 类变量：类变量也声明在类中，方法体之外，但必须声明为static类型。类变量与类相关，无论创建多少个类实例，静态变量在内存中只有一份，被所有实例共享。可通过类名或实例名访问。
* 参数变量：用于接收传递给方法或构造函数的值。参数变量的值传递有两种方式：（1）值传递，java基本数据类型都是采用值传递。值传递传递的是参数的值的副本，只会修改副本而不会影响原始值。（2）引用传递，java中的对象类型采用引用传递。传递的是实际参数的引用，会修改原始值的内容。

构造方法中的this关键字
* 引用当前对象的属性或方法
```java
public Person(String name, int age) {
    this.name = name; // this.name 表示类的属性
    this.age = age;
}
```
* 调用另一个构造方法。使用this()调用当前类的其他构造方法，必须放在当前构造方法的第一行。
```java
public Person(String name) {
    this(name, 0); // 调用另一个双参数的构造方法
}

public Person(String name, int age) {
    this.name = name;
    this.age = age;
}
```

## 4. java基本数据类型
### 内置数据类型
六种数字类型（四个整数类型，两个浮点型），一种字符类型，一种布尔型。

整数类型
* byte（8位）
* short（16位）
* int（32位），整型默认为int类型。
* long（64位），使用"L"或"l"后缀。
浮点型
* float（单精度，32位）
* double（双精度，64位），浮点型默认为double类型。
字符型
* char
布尔型
* boolean
### 引用数据类型
* 引用类型指向一个对象，指向对象的变量是引用变量。变量被声明后，类型就不能改变了。
* 对象，数组都是引用数据类型。
* 所有引用类型的默认值都是null。
### 常量
使用final关键字来定义常量，常量标识符通常全是大写。
## 5. java修饰符
### 访问控制修饰符
* public，类，变量，接口，方法。
* private，变量，方法。不能修饰类。
* default，类，接口，变量，方法。
* protected，变量，方法。不能修饰类，内部类除外。

| 修饰符     | 当前类 | 同一包内 | 子孙类(同一包) | 子孙类(不同包) | 其他包 |
|------------|--------|----------|----------------|----------------|--------|
| `public`   | Y      | Y        | Y              | Y              | Y      |
| `protected`| Y      | Y        | Y              | Y/N   | N      |
| `default`  | Y      | Y        | Y              | N              | N      |
| `private`  | Y      | N        | N              | N              | N      |

子类与基类不在同一包，在子类中，子类实例可以访问从基类继承而来的protected方法，而不能访问基类实例的protected方法。
### 非访问修饰符
* static，静态变量，静态方法。静态方法不能使用类的非静态变量。
* final，final变量，一旦赋值后，不能被重新赋值。final方法，父类中的final方法可以被子类继承，但不能被重写。final类，不能被继承。
* abstract，抽象类不能用来实例化对象，声明抽象类是为了将来对该类进行扩充。一个类包含抽象方法，一定要声明为抽象类。一个抽象类可以包含抽象方法和非抽象方法。抽象方法是没有任何实现的方法，该方法的具体实现由子类提供。
任何继承抽象类的子类必须实现父类的所有抽象方法。
* synchronized，被该关键字修饰的方法同一时间只能被一个线程访问。
* transient，序列化对象中包含transient修饰的变量，该变量不会被持久化。
* volatile，被该关键字修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，以强制线程将变化值回写到共享内存。因此，在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。
### 6. Java运算符
* 算术运算符（+,-,*,/,%,++,--）
* 关系运算符（==,!=,>,<,>=,<=）
* 逻辑运算符（&&,||,!）
* 条件运算符（三元运算符）
```java
variable x = (expression) ? value if true : value if false
```
* instance of运算符，检查对象是否是一个特定类型。
```java
( Object reference variable ) instanceof  (class/interface type)
```
### 7. java循环结构
while循环
```java
while( 布尔表达式 ) {
  //循环内容
}
```
do-while循环
```java
do {
       //代码语句
}while(布尔表达式);
```
for循环
```java
for(初始化; 布尔表达式; 更新) {
    //代码语句
}
```
增强for循环
```java
for(循环变量声明语句 : 集合对象)
{
   //代码句子
}
```

### 8. java条件语句
if-else
```java
if(布尔表达式){
   //如果布尔表达式的值为true
}else{
   //如果布尔表达式的值为false
}
```
if-else if-esle
```java
if(布尔表达式 1){
   //如果布尔表达式 1的值为true执行代码
}else if(布尔表达式 2){
   //如果布尔表达式 2的值为true执行代码
}else if(布尔表达式 3){
   //如果布尔表达式 3的值为true执行代码
}else {
   //如果以上布尔表达式都不为true执行代码
}
```

### 9. switch case语句
```java
switch(expression){
    case value :
       //语句
       break; //可选
    case value :
       //语句
       break; //可选
    //你可以有任意数量的case语句
    default : //可选
       //语句
}
```

### 10.java Number类
所有包装类（Interger，Long，Byte，Double，Float，Short）都是抽象类Number的子类。

| 类名       | 对应基本类型 | 描述                     |
|------------|-------------|--------------------------|
| Byte       | byte        | 字节型包装类             |
| Short      | short       | 短整型包装类             |
| Integer    | int         | 整型包装类               |
| Long       | long        | 长整型包装类             |
| Float      | float       | 单精度浮点型包装类       |
| Double     | double      | 双精度浮点型包装类       |
| BigInteger | -           | 不可变任意精度整数       |
| BigDecimal | -           | 不可变任意精度十进制数   |


基本数据类型的强制类型转换
```java
int x = 10;
System.out.println((double)x);

=> 10.0
```
包装类的类型转换，使用`.xxxValue()`函数
```java
Double num = 1234.56; // 实际是Double类型

System.out.println(num.intValue());    // 1234 (截断小数)
System.out.println(num.longValue());   // 1234
System.out.println(num.floatValue());  // 1234.56
```

### 11.java String类
String创建的字符串存储在公共池（常量池）中，而new创建的字符串对象在堆上。
```java
String s1 = "Runoob"; //常量池
String s4 = new String("Runoob"); //堆
```
String类是不可变的，一旦创建，它的值就无法改变了。要做修改，可使用StringBuffer或StringBuilder类。

StringBuffer和StringBuilder类的对象能被多次修改，并且不产生新的未使用的对象。StringBuffer是线程安全的，StringBuilder不是线程安全的，但是StringBuilder有速度优势。

`.length()`返回字符串长度
`string1.concat(string2);` 连接两个字符串，也可以直接使用+来连接字符串。

### 12. java数组
声明数组
```java
dataType[] arrayRefVar; 
```
创建数组
```java
arrayRefVar = new dataType[arraySize];
```
声明和创建
```java
dataType[] arrayRefVar = new dataType[arraySize];

dataType[] arrayRefVar = {value0, value1, ..., valuek};
```
数组索引从0开始。

多维数组（二维数组为例）
```java
type[][] typeName = new type[typeLength1][typeLength2];
```

### 13.java方法
方法的定义
```java
修饰符 返回值类型 方法名(参数类型 参数名){
    ...
    方法体
    ...
    return 返回值;
}
```
可变参数

声明方式
```java
typeName... parameterName
```
一个方法只能指定一个可变参数，它必须是方法的最后一个参数。任何普通的参数必须在它之前声明。
```java
public class VarargsDemo {
    public static void main(String[] args) {
        // 调用可变参数的方法
        printMax(34, 3, 3, 2, 56.5);
        printMax(new double[]{1, 2, 3});
    }
 
    public static void printMax( double... numbers) {
        if (numbers.length == 0) {
            System.out.println("No argument passed");
            return;
        }
 
        double result = numbers[0];
 
        for (int i = 1; i <  numbers.length; i++){
            if (numbers[i] >  result) {
                result = numbers[i];
            }
        }
        System.out.println("The max value is " + result);
    }
}
```
### 14.java异常
try-catch
```java
try
{
   // 程序代码
}catch(ExceptionName e1)
{
   //Catch 块
}
```
多重捕获
```java
try{
   // 程序代码
}catch(异常类型1 异常的变量名1){
  // 程序代码
}catch(异常类型2 异常的变量名2){
  // 程序代码
}catch(异常类型3 异常的变量名3){
  // 程序代码
}
```
多异常合并捕获，可以用一个 catch 块处理多个无继承关系的异常。
```java
try {
    // 可能抛出多个不同类型异常的代码
} catch (异常类型1 | 异常类型2 | 异常类型3 异常变量) {
    // 统一处理
}
```
throw 关键字用于在代码中抛出异常，而 throws 关键字用于在方法声明中指定可能会抛出的异常类型。

try-with-resource
* try-with-resources 是一种异常处理机制，它能够自动关闭在 try 块中声明的资源，无需显式地在 finally 块中关闭。
* 在 try-with-resources 语句中，只需要在 try 关键字后面声明资源，然后跟随一个代码块。无论代码块中的操作是否成功，资源都会在 try 代码块执行完毕后自动关闭。
```java
try (resource declaration) {
  // 使用的资源
} catch (ExceptionType e1) {
  // 异常块
}
```
可以声明多个资源，使用`;`分隔每个资源。
### 15.java继承
继承的关系是“is-a”，父类更通用，子类更具体。
```java
class 父类 {
}
 
class 子类 extends 父类 {
}
```
* super关键字：实现对父类成员的访问，用来引用当前对象的父类。
* this关键字：指向自己的引用，引用当前对象，即它所在方法或构造函数所属的对象实例。
* 子类不继承父类的构造器，只是调用。如果父类的构造器带参数，必须在子类的构造器中显式的通过super关键字调用父类的构造器并配以适当的参数列表。
### 16.重写和重载
重写是指子类定义了一个与其父类中具有相同名称、参数列表和返回类型的方法，并且子类方法的实现覆盖了父类方法的实现。 即外壳不变，核心重写！

重写的规则：
* 参数列表与被重写方法的参数列表必须完全相同。
* 返回类型与被重写方法的返回类型可以不相同，但是必须是父类返回值的子类。
* 访问权限不能比父类中被重写的方法的访问权限更低。例如：如果父类的一个方法被声明为 public，那么在子类中重写该方法就不能声明为 protected。
* 父类的成员方法只能被它的子类重写。
* 声明为 final 的方法不能被重写。
* 声明为 static 的方法不能被重写，但是能够被再次声明。
* 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为 private 和 final 的方法。
* 子类和父类不在同一个包中，那么子类只能够重写父类的声明为 public 和 protected 的非 final 方法。
* 重写的方法能够抛出任何非强制异常，无论被重写的方法是否抛出异常。但是，重写的方法不能抛出新的强制性异常，或者比被重写方法声明的更广泛的强制性异常，反之则可以。
* 构造方法不能被重写。
* 如果不能继承一个类，则不能重写该类的方法。
重载(overloading) 是在一个类里面，方法名字相同，而参数不同。返回类型可以相同也可以不同。每个重载的方法（或者构造函数）都必须有一个独一无二的参数类型列表。

重载的规则：
* 被重载的方法必须改变参数列表(参数个数或类型不一样)；
* 被重载的方法可以改变返回类型；
* 被重载的方法可以改变访问修饰符；
* 被重载的方法可以声明新的或更广的检查异常；
* 方法能够在同一个类中或者在一个子类中被重载。
* 无法以返回值类型作为重载函数的区分标准。

### 17.java抽象类
* 抽象类除了不能实例化对象之外，类的其他功能依然存在，成员变量，成员方法和构造方法的访问方式和普通类一样。抽象类不能实例化对象，所以抽象类必须被继承。
* 抽象方法只包含方法名，没有方法体。该方法的具体实现由他的子类确定。
* 声明抽象方法会造成下面两个结果：
    * 如果一个类包含抽象方法，那么该类必须是抽象类。
    * 任何子类必须重写父类的抽象方法，或者声明自身为抽象类。

### 18.java接口
接口无法被实例化，但是可以被实现。一个实现接口的类，必须实现接口内所描述的所有方法，否则就声明为抽象类。

接口与类的相似点：
* 一个接口可以有多个方法。
* 接口文件保存在.java结尾的文件中，文件名使用接口名。
* 接口的字节码文件保存在.class结尾的文件中。
* 接口相应的字节码文件必须在与包名称相匹配的目录结构中。
接口与类的区别：
* 接口不能用于实例化对象。
* 接口没有构造方法。
* 接口中所有的方法必须是抽象方法，Java 8 之后 接口中可以使用 default 关键字修饰的非抽象方法。可以有静态方法和方法体。允许有私有方法。
* 接口不能包含成员变量，除了 static 和 final 变量。
* 接口不是被类继承了，而是要被类实现。
* 接口支持多继承。
接口的特性：
* 接口中每一个方法也是隐式抽象的,接口中的方法会被隐式的指定为 public abstract（只能是 public abstract，其他修饰符都会报错）。
* 接口中可以含有变量，但是接口中的变量会被隐式的指定为 public static final 变量（并且只能是 public，用 private 修饰会报编译错误）。
* 接口中的方法是不能在接口中实现的，只能由实现接口的类来实现接口中的方法。
接口和抽象类的区别：
* 抽象类中的方法可以有方法体，就是能实现方法的具体功能，但是接口中的方法不行。（java 8之后，接口中可以有静态方法，默认方法和私有方法）。
* 抽象类中的成员变量可以是各种类型的，而接口中的成员变量只能是 public static final 类型的。
* 一个类只能继承一个抽象类，而一个类却可以实现多个接口。

接口的声明：
```java
[可见度] interface 接口名称 [extends 其他的接口名] {
        // 声明变量
        // 抽象方法
}
```
### 19.java枚举
枚举一般表示一组常量。
* `values()`  返回枚举类中的所有值
* `ordinal()` 找到每个枚举常量的索引
* `valueOf()` 返回指定字符串值的枚举常量。

### 20.java集合
ArrayList可动态修改的数组，没有固定大小的限制，可以添加或删除元素。
```java
import java.util.ArrayList; // 引入 ArrayList 类

ArrayList<E> objectName =new ArrayList<>();　 // 初始化
```
* `add()` 添加元素
* `get()` 访问元素
* `set()` 修改元素
* `remove()` 删除元素
* `size()` 计算大小
LinkedList可在开头，结尾或中间插入和添加元素
```java
// 引入 LinkedList 类
import java.util.LinkedList; 

LinkedList<E> list = new LinkedList<E>();   // 普通创建方法
或者
LinkedList<E> list = new LinkedList(Collection<? extends E> c); // 使用集合创建链表
```
HashSet，无序集合，不允许有重复元素，不是线程安全。
```java
import java.util.HashSet; // 引入 HashSet 类
HashSet<String> sites = new HashSet<String>();
```
* `add()`添加元素
* `contains()` 判断元素是否存在
* `remove()` 删除元素
* `clear()` 删除集合中所有元素
* `size()` 计算大小
*HashMap，存储key-value键值对，允许key为null，不支持线程同步，无序。
```java
import java.util.HashMap; // 引入 HashMap 类
HashMap<Integer, String> Sites = new HashMap<Integer, String>();
```
* `put()`添加元素
* `get(key)` 获取key对应的value
* `remove(key)` 删除key对应的value
* `clear()` 删除所有元素
* `size()` 计算大小

Iterator迭代器，用于遍历集合。只能从前往后遍历集合的元素，不能往回遍历。
### 21.java泛型
泛型方法，在调用时可以接收不同类型的参数。
定义泛型方法的规则：
* 所有泛型方法声明都有一个类型参数声明部分（由尖括号分隔），该类型参数声明部分在方法返回类型之前（在下面例子中的`<E>`）。
* 每一个类型参数声明部分包含一个或多个类型参数，参数间用逗号隔开。一个泛型参数，也被称为一个类型变量，是用于指定一个泛型类型名称的标识符。
* 类型参数能被用来声明返回值类型，并且能作为泛型方法得到的实际参数类型的占位符。
* 泛型方法体的声明和其他方法一样。注意类型参数只能代表引用型类型，不能是原始类型（像 int、double、char 等）。

java 中泛型标记符：
* E - Element (在集合中使用，因为集合中存放的是元素)
* T - Type（Java 类）
* K - Key（键）
* V - Value（值）
* N - Number（数值类型）
* ? - 表示不确定的 java 类型
```java
public class GenericMethodTest
{
   // 泛型方法 printArray                         
   public static < E > void printArray( E[] inputArray )
   {
      // 输出数组元素            
         for ( E element : inputArray ){        
            System.out.printf( "%s ", element );
         }
         System.out.println();
    }
 
    public static void main( String args[] )
    {
        // 创建不同类型数组： Integer, Double 和 Character
        Integer[] intArray = { 1, 2, 3, 4, 5 };
        Double[] doubleArray = { 1.1, 2.2, 3.3, 4.4 };
        Character[] charArray = { 'H', 'E', 'L', 'L', 'O' };
 
        System.out.println( "整型数组元素为:" );
        printArray( intArray  ); // 传递一个整型数组
 
        System.out.println( "\n双精度型数组元素为:" );
        printArray( doubleArray ); // 传递一个双精度型数组
 
        System.out.println( "\n字符型数组元素为:" );
        printArray( charArray ); // 传递一个字符型数组
    } 
}
```
有界的类型参数，声明一个有界类型参数，首先列出类型参数的名称，后跟extends关键字，最后紧跟它的上界。
```java
public class MaximumTest
{
   // 比较三个值并返回最大值
   public static <T extends Comparable<T>> T maximum(T x, T y, T z)
   {                     
      T max = x; // 假设x是初始最大值
      if ( y.compareTo( max ) > 0 ){
         max = y; //y 更大
      }
      if ( z.compareTo( max ) > 0 ){
         max = z; // 现在 z 更大           
      }
      return max; // 返回最大对象
   }
   public static void main( String args[] )
   {
      System.out.printf( "%d, %d 和 %d 中最大的数为 %d\n\n",
                   3, 4, 5, maximum( 3, 4, 5 ) );
 
      System.out.printf( "%.1f, %.1f 和 %.1f 中最大的数为 %.1f\n\n",
                   6.6, 8.8, 7.7, maximum( 6.6, 8.8, 7.7 ) );
 
      System.out.printf( "%s, %s 和 %s 中最大的数为 %s\n","pear",
         "apple", "orange", maximum( "pear", "apple", "orange" ) );
   }
}
```
泛型类，声明方式和普通类类似，要在类名后添加类型参数声明部分。
```java
public class Box<T> {
   
  private T t;
 
  public void add(T t) {
    this.t = t;
  }
 
  public T get() {
    return t;
  }
 
  public static void main(String[] args) {
    Box<Integer> integerBox = new Box<Integer>();
    Box<String> stringBox = new Box<String>();
 
    integerBox.add(new Integer(10));
    stringBox.add(new String("菜鸟教程"));
 
    System.out.printf("整型值为 :%d\n\n", integerBox.get());
    System.out.printf("字符串为 :%s\n", stringBox.get());
  }
}
```
