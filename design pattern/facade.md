## 概念
- 为子系统中的一组接口提供一个 统一的高层接口，让子系统更易使用。
- 客户端只与外观类交互，不直接操作子系统内部复杂的类。
- 降低系统的复杂性，提高可维护性。
## 结构
![外观模式](facade.png)
Facade：外观类，封装子系统复杂操作，提供简单方法给客户端。
SubSystemX：子系统类，实际功能实现。
客户端：只调用外观类，不直接操作子系统。
## 例子
```java
// 子系统类 - 电视
class TV {
    public void on() {
        System.out.println("电视打开");
    }

    public void off() {
        System.out.println("电视关闭");
    }
}

// 子系统类 - 音响
class SoundSystem {
    public void on() {
        System.out.println("音响打开");
    }

    public void off() {
        System.out.println("音响关闭");
    }
}

// 子系统类 - 灯光
class Lights {
    public void on() {
        System.out.println("灯光打开");
    }

    public void off() {
        System.out.println("灯光关闭");
    }
}

// 外观类 - 家庭影院
class HomeTheaterFacade {
    private TV tv;
    private SoundSystem sound;
    private Lights lights;

    public HomeTheaterFacade(TV tv, SoundSystem sound, Lights lights) {
        this.tv = tv;
        this.sound = sound;
        this.lights = lights;
    }

    // 一键开机
    public void watchMovie() {
        System.out.println("准备看电影...");
        lights.off();
        tv.on();
        sound.on();
    }

    // 一键关闭
    public void endMovie() {
        System.out.println("电影结束...");
        tv.off();
        sound.off();
        lights.on();
    }
}

// 客户端
public class FacadeDemo {
    public static void main(String[] args) {
        TV tv = new TV();
        SoundSystem sound = new SoundSystem();
        Lights lights = new Lights();

        HomeTheaterFacade home = new HomeTheaterFacade(tv, sound, lights);

        // 客户端只调用外观方法
        home.watchMovie();
        System.out.println();
        home.endMovie();
    }
}
```
## 优点
- 降低系统复杂性，客户端与子系统解耦。
- 提高安全性，可以只暴露必要方法。
- 便于维护和扩展。
## 缺点
- 增加外观类维护成本，如果系统功能变化，外观类也要改。
- 不适合对子系统完全隐藏功能的场景，否则可能限制灵活性。
## 使用场景
- 当系统复杂，客户端需要与多个子系统交互。
- 提供统一接口，简化调用流程。
- 需要对外屏蔽子系统内部实现，保证解耦性。
