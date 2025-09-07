## 概念
备忘录模式（Memento Pattern）是一种行为型设计模式，主要用于在不破坏对象封装的前提下，捕获并保存对象的内部状态，以便之后可以将对象恢复到之前的状态。

常见的应用场景：
- 编辑器的撤销/恢复 (Undo/Redo)功能
- 游戏的存档/读档
- 事务操作的回滚

## 结构
备忘录模式通常包含三个角色：
- Originator（发起人/原发器）
    - 负责创建一个备忘录，用于记录当前对象的状态。
    - 也可以使用备忘录恢复状态。
- Memento（备忘录）
    - 用来存储 Originator 的内部状态。
    - 一般是只读的，不允许外部随意修改。
- Caretaker（管理者/负责人）
    - 负责保存和恢复备忘录。
    - 本身并不修改备忘录内容，只负责“看管”。

## 例子
```java
// 备忘录
class Memento {
    private final String state;

    public Memento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

// 发起人
class Originator {
    private String state;

    public void setState(String state) {
        System.out.println("设置状态: " + state);
        this.state = state;
    }

    public String getState() {
        return state;
    }

    // 创建备忘录
    public Memento saveStateToMemento() {
        return new Memento(state);
    }

    // 从备忘录恢复状态
    public void getStateFromMemento(Memento memento) {
        this.state = memento.getState();
        System.out.println("恢复状态: " + state);
    }
}

// 管理者
class Caretaker {
    private final java.util.Stack<Memento> mementoStack = new java.util.Stack<>();

    public void add(Memento state) {
        mementoStack.push(state);
    }

    public Memento undo() {
        if (!mementoStack.isEmpty()) {
            return mementoStack.pop();
        }
        return null;
    }
}

// 测试类
public class MementoPatternDemo {
    public static void main(String[] args) {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();

        originator.setState("状态 #1");
        caretaker.add(originator.saveStateToMemento());

        originator.setState("状态 #2");
        caretaker.add(originator.saveStateToMemento());

        originator.setState("状态 #3");
        System.out.println("当前状态: " + originator.getState());

        // 撤销操作
        originator.getStateFromMemento(caretaker.undo());
        originator.getStateFromMemento(caretaker.undo());
    }
}
```

```java
// 备忘录类：保存游戏状态
class GameMemento {
    private final int level;
    private final int hp;

    public GameMemento(int level, int hp) {
        this.level = level;
        this.hp = hp;
    }

    public int getLevel() {
        return level;
    }

    public int getHp() {
        return hp;
    }
}

// 发起人：游戏角色
class Game {
    private int level;
    private int hp;

    public Game(int level, int hp) {
        this.level = level;
        this.hp = hp;
    }

    public void play() {
        System.out.println("正在游戏... 当前等级: " + level + " 血量: " + hp);
        level++;
        hp -= 10; // 假设玩游戏会掉血
    }

    public void showState() {
        System.out.println("当前角色 -> 等级: " + level + " 血量: " + hp);
    }

    // 存档
    public GameMemento save() {
        System.out.println("存档成功！等级: " + level + " 血量: " + hp);
        return new GameMemento(level, hp);
    }

    // 读档
    public void load(GameMemento memento) {
        this.level = memento.getLevel();
        this.hp = memento.getHp();
        System.out.println("读档成功！恢复到 -> 等级: " + level + " 血量: " + hp);
    }
}

// 管理者：存档管理器
class Caretaker {
    private final java.util.Stack<GameMemento> saves = new java.util.Stack<>();

    public void add(GameMemento memento) {
        saves.push(memento);
    }

    public GameMemento undo() {
        if (!saves.isEmpty()) {
            return saves.pop();
        }
        return null;
    }
}

// 测试类
public class GameMementoDemo {
    public static void main(String[] args) {
        Game game = new Game(1, 100);
        Caretaker caretaker = new Caretaker();

        game.showState();
        caretaker.add(game.save()); // 存档 1

        game.play();
        caretaker.add(game.save()); // 存档 2

        game.play();
        game.play();
        game.showState();

        // 读档（回退到上一次存档）
        game.load(caretaker.undo());
        game.showState();

        // 再次读档（回退到更早的存档）
        game.load(caretaker.undo());
        game.showState();
    }
}

```
## 优点
- 可以实现对象状态的保存与恢复，支持撤销/回滚。
- 封装性好，状态存储在 Memento 中，不会暴露给外部。
## 缺点
- 可能会占用大量内存（特别是频繁保存时）。
- 如果对象状态过于复杂，保存和恢复的开销会比较大