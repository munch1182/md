# Kotlin相较于JAVA的差异

- 官方文档：https://www.kotlincn.net/docs/reference/basic-types.html
- 使用和学习kotlin最简单最快的方法就是将java代码复制到kotlin文件中由as自动转换
- androidstudio-tool-Kotlin-show kotlin bytecode可以看到kotlin编译后的文件
- kotlin与java的差距多在写法上，kotlin从编译层面对java的写法进行优化，使代码可以写的更简单

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [基础语法](#基础语法)
- [一些细节](#一些细节)
- [kotlin拓展](#kotlin拓展)

<!-- /code_chunk_output -->

## 基础语法

- 类的继承和实现，
    - 使用`:`来取代`extends`和`implements`，如
    ```java
    class MainActivity extends BaseActivity implements View.OnClickListener
    ```
    变成了
    ```kotlin
    class MainActivity : BaseActivity() , View.OnClickListener
    ```
     class继承需要显示声明构造，对于BaseActivity，即`()`，接口则不需要

- 默认可见性
    - koltin的类如无声明，则是`public final`的    
    方法如无声明也是`public final`的  
    变量如无声明则是`public`的
    - kotlin写在其它类内部的类并非内部类，不会持有外部类的默认引用，要成为内部类，需要给写在内部的类使用`inner`关键字即`inner class NameClass{}`

- 构造函数
    - kotlin的构造函数分为主构造函数和次构造函数
    - 主构造函数需要写在类头，使用`constructor`声明，无修饰符时constructor可省略，例如：    
        ```kotlin
        class CustomView constructor(context: Context, attrs: AttributeSet?, defStyleAttr: Int) : View(context, attrs, defStyleAttr)
        ```
        这表明CustomView的主构造函数有三个参数，并且将这三个参数传值给了其父类View

    - 如果需要在主构造函数中编写代码，可以使用`init`关键字
        ```kotlin
        class CustomView(context: Context, attrs: AttributeSet?, defStyleAttr: Int) : View(context, attrs, defStyleAttr){
           init {
                val typedArray = context.obtainStyledAttributes(attrs, R.styleable.CustomView)
                typedArray.recycle()
            } 
        }
        ```
        init范围内的代码可以调用主构造函数内的参数，可以把init看作主构造函数的方法体

    - 次构造函数必须使用`constructor`关键字，且可以使用`this`或者`super`来调用自己的或父类的其它构造，如果主构造函数有参数，则次构造函数必须调用主构造函数，如无参数，会隐式调用
        ```kotlin
        class CustomView(context: Context, attrs: AttributeSet?, defStyleAttr: Int) : View(context, attrs, defStyleAttr){
           init {
                val typedArray = context.obtainStyledAttributes(attrs, R.styleable.CustomView)
                typedArray.recycle()
            }
            //次构造函数
            constructor(context: Context, attrs: AttributeSet?) : this(context, attrs, 0) //省略了{}
            //次构造函数
            constructor(context: Context) : this(context, null) {}
        }
        ```
        这表示该类有三个构造函数，并且两个次构造函数最后都委托了主构造函数并传值给父类。
        次构造函数可以有方法体及其实现，空方法体可以省略{}

- 方法写法改变
    - 方法需要使用`fun`关键字，并且返回值放到了最右侧，即   
        ```java
        //java:
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
        }
        //kotlin:
        @Override fun onCreate(savedInstanceState: Bundle?):Unit { //Unit可以看作java的void，当方法返回值是Unit时也可以省略
            super.onCreate(savedInstanceState)
        }
        ```

- 参数默认值
    - kotlin可以直接给参数标记上默认值，这样调用者调用方法时，如果传入了该参数的值，则使用传入的值，如果省略了该参数，即使用默认值，类似于java有默认值的方法重载：
        ```kotlin
        fun newView(context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0):CustomView{
           return CustomView(context, attrs, defStyleAttr)
        }
        ```
        调用:
        ```kotlin
        newView(Context())
        newView(Context(),AttributeSet())
        newView(Context(),AttributeSet(),1)
        newView(Context(),defStyleAttr = 1)
        ```
        四种都可以调用该方法，但是使用的值不同，最后一个表示传入context和defStyleAttr的值，但attrs使用默认值    
        kotlin函数参数可以使用其`参数名称 = 要传的值`来声明该值属于哪一个参数，即上例中的`defStyleAttr = 1`，这样使用时，可以省略中间的某些参数，也可以调转传参数的顺序

- var、val关键字与类型推断
    - kotlin的变量类型声明需要使用`var/val`关键字，并且与java的格式不同
        ```java
        //java:
        ArrayList<BaseDto<User>> userList = new ArrayList<BaseDto<User>>()

        //kotlin:
        val userList : ArrayList<BaseDto<User>> = ArrayList<BaseDto<User>>() // kotlin 的对象去掉了java的new关键字，直接调用构造即可代表新建对象
        ```
    - 类型推断：简单来说，只要`=`右边能确定变量类型，那么`=`左边就不必显式声明变量的类型，如果不能确定或者需要确定类型，则需要手动声明
        ```kotlin
        val a = 1   // a是int类型
        val a = 1.0 // a是double类型
        val a = 1d  // a是double类型
        val a = "1" // a是String类型

        val userList = ArrayList<BaseDto<User>>() // userList是ArrayList类型
        val a = SportFragment() // a是SportFragment类型
        val a : Fragment = SportFragment() // a是Fragment的
        ```
    - kotlin函数也可以这样写来省略返回值声明
        ```kotlin
        fun newInstance(name:String) = User(name)  //test是一个返回User类型的函数，这里省略了返回值声明，省略了{}

        fun test() = newInstance("test name") //同上
        ```
    - var和val的区别在于，val声明的变量是final的，不可再更改
    - 推断规则与java一致，只是写法不一样
    - 从主构造函数可以将构造函数的参数直接声明为类的变量，只要在参数前加入val/var关键字，其与java传参进构造函数并赋值给变量是一样的，这是kotlin的简化写法。只有主构造函数可以这样声明变量。
        ```java
        //kotlin:
        class CustomView(private val context2: Context, attrs: AttributeSet?, defStyleAttr: Int) : View(context2, attrs, defStyleAttr) 
        //此时context2是一个私有成员变量且被构造赋值，类作用域可用，attrs和defStyleAttr是构造参数，只有init范围可用

        //对应的java:
        public class CustomView extends View {

            private Context context2;

            public CustomView(Context context2, @Nullable AttributeSet attrs, int defStyleAttr) {
                super(context2, attrs, defStyleAttr);
                this.context2 = context2;
            }
        }
        ```

- 非空判断
    - kotlin声明类型时需要手动声明类型是否可以为null，如果可能为null，需要添加`?`
        ```kotlin
        var a ：SportFragment //a是SportFragment类型且a不能被传入null
        var a : SportFragment? //a是SportFragment类型且a可能null可以被赋值为null
        ```
        这种声明类似于android的`@Nullable`和`@Nonnull`，但更具强制性        
    - kotlin有`?.`和`?:`两种方式来简化空值的判断和操作
    - 对比：    
        ```java
        //java:
        Intent intent = getIntent();
        if (intent==null){
            return;
        }
        String extra = intent.getStringExtra(KEY_EXTRA_STR);
        if (extra==null){
            return;
        }
        // do something

        //kotlin:(kotlin中getIntent()方法会被简化成intent)
        val extra = intent?.getStringExtra(KEY_EXTRA_STR) ?: return
        // do something
        ```     
        这两种写法是等同的，kotlin编译成java文件其实与java的写法是一致的
    - `?.`即不为null时的操作，由对象调用，是`if(对象 != null)`的简写
    - `?.`的链式调用，会截至到为空的部分位置
        ```kotlin
        A().a()?.b()?.c()?.d()

        //编译成java则是
        A var1 = (new A()).a();
        if (var1 != null) {
            var1 = var1.b();
            if (var1 != null) {
                var1 = var1.c();
                if (var1 != null) {
                    var1.d();
                }
            }
      }
        ```

    - `?:`即为null时的操作，`?:`一般用在赋值操作时，即`val extra = intent?.getStringExtra(KEY_EXTRA_STR) ?: "def"`  
    意味着如果intent不为null且从intent取出的值不为null，则将该值赋予extra，否则，则将def赋予extra；`?:`后也可以直接跟`return`或者`throw Exception()`，表明为空时所做的操作
    - `!!`：如果一个变量被声明了可为空，但需要它必须不为空，如被当作一个参数传入一个不为空的位置时，需要使用`!!`来告诉编译器该变量此时不为空，否则会编译失败。相当于`Any?`强转为`Any`，如果运行时该变量仍为空，则会抛出空指针异常
    - 在使用kotlin代码调用java的时候，因为java没有这个强制特性，需要自行根据java中的定义判断其值是否可能为空，也可以都认为可空来进行非空判断

- get/set
    - kotlin的属性会默认加上get(var、val)/set(var)方法，你也可以显示声明其get/set方法，如
        ```kotlin
        var url = ""
            get() {
                // field在get/set中即指代当前属性
                return if (BuildConfig.DEBUG) {
                    field
                } else {
                    URL_RELEASE
                }
            }
            set(value) {
                field = if (value.contains("debug") && BuildConfig.DEBUG) { //当if-else的操作都是赋值时，就可以这样将=左边放到if-else外面来，if-else里会取最后一行的值
                    value
                } else {
                    URL_RELEASE
                }
            }
        ```
    调用属性时kotlin会自动省略get/set方法的显示但实际会调用，直接使用url即会自动调用其get方法，直接给url赋值会自动调用set方法，且每次调用时都会调用相应方法
    - 对属性声明的可见性会影响get/set方法的生成，但编译成java属性始终是`private`的，若要使其可见，需使用`@JvmField`注解声明

- 类或关键字改变
    - 去掉了`new`关键字，kotlin新建对象只需要调用构造而不需要在前面使用`new`

    - java->kotlin：
        - `Object.class` -> `Any.class`
        - `void`   -> `Unit`
        - `instanceof` -> `is`

    - `constructor`: kotlin用来显式声明构造方法，没有修饰符如private时或者注解符如@inject时可不写

    - `object`: //与java的Object类没有关系，kotlin的object是一个关键字
        - 表示一个匿名对象
            ```kotlin
            val click = object : View.OnClickListener{ //click没有声明类型，因为返回值确定
                override fun onClick(v: View?) {
                }
            }

            //使用
            view.setOnClickListener(click)
            ```
            表示声明一个对象click，其值是一个View.OnClickListener的匿名实现
        - 替代`class`声明一个类，表示该类是一个单例类，注意：并非静态类，虽然其可以类似静态的访问，由`object`声明的类可以来写工具类代码
            ```kotlin
            //kotlin：
            object Singleton {

                val a = getAVal()

                private fun getAVal(): Int {
                    return 1
                }
            }
            ```
            kotlin调用：Singleton.a     
            java中调用kotlin的Singleton：Singleton.INSTANCE.getA()

            编译的java文件：
            ```java
            public static final class Singleton {
                private static final int a;
                @NotNull
                public static final Test.Singleton INSTANCE;

                public final int getA() {
                    return a;
                }

                private final int getAVal() {
                    return 1;
                }

                private Singleton() {
                }

                static {
                    Singleton var0 = new Singleton();
                    INSTANCE = var0;
                    a = var0.getAVal();
                }
            }
            ```

    - `companion`: 表示伴生对象，每个类只能有一个伴生对象，伴生对象的初始化是在相应的类被加载（解析）时，相当于Java 静态初始化器，相对应的`object`是在调用时，kotlin在`companion`中声明该方法的静态方法或字段
        ```kotlin
        class TestActivity : BaseActivity() {

            companion object {
                const val TAG = "TestActivity"
            }
        }
        ```
        相当于java中在TestActivity中声明`public static final String TAG = "TestActivity"`，事实上，伴生对象中的字段会直接生成在`TestActivity`类中而不是默认的`object`单例类`Companion`中，这是`companion`的作用

    - `const`: const关键字表明该值为编译期常量，表明该值固定，否则编译器会当成属性生成相应get/set方法，`const`只支持基础数据类型和String，在类里只能写在`object`或者`companion object`中

    - `@JvmStatic`: 被`@JvmStatic`声明的方法或字段才会被编译成java的`static`，而不是被编译成单例类方法或者字段的形式，这才是java的静态，但是在写法上，`object`可以被看做静态，`@Jvmstatic`一般用于需要被java调用的方法上

    - `open`: kotlin的类如果要可继承，其类需要显式使用`open`关键字，方法如可重写也需要最前面加上`open`关键字，即`class BaseActivity`应该写成`open class BaseActivity`，否则不能继承或者重写

    - `init`: 该关键字用来声明初始化代码块，其中的代码会在主构造函数中执行

    - `vararg`: 不定参数，用在函数的参数中，与java的不定参数`...`是一样的，在使用时可以被当作集合

    - `as`/`as?`: 强转关键字，类似于java的`(MainActivity)activity`,kotlin写作`activity as Mainactivity`，`as?`表示如果activity不为Mainactivity，则转成null

    - `lateinit`: 延迟关键字，kotlin属性必须初始化，而某些属性当前不能初始化，但又不能为null时，可以使用此关键字来延迟给属性初始化，这样的声明只能用`var`即`lateinit var a:View`

- 基本数据类型
    - java的基本数据类型在kotlin中使用时被当作对象，分别是`Byte`、`Short`、`Int`、`Long`、`Float`、`Double`、`char`，`String`在kotlin中不是基本数据类型而是独立的数据类型

    - kotlin会在编译时优化，如果你只使用了基本数据类型数据的部分，编译时还是会被编译成java的基本数据类型    
        ```kotlin
        //koltin:
        val a = 1
        val a1:Int? = 1
        val a2:Int = 1
        val a3 = 1.0
        val a4:Double? = 1.0
        val a5:Double? = null
        ```

        ```java
        //编译后的java文件:
        int a = true;
        int a1 = true;
        int a2 = true;
        double a3 = 1.0D;
        double a4 = 1.0D;
        Double a5 = (Double)null;
        ```
    - 作为对象，基本数据类型也有非空判断
    - 基本数据类型转化：在kotlin中转化需要调用方法，如`val a6 = a4?.toInt()?.toByte()`，其实现与java一致

- 循环与区间：
    ```kotlin
    for (i in 1..4) { //1 <= i && i <= 4
        print(i)
    }
    for (i in 4 downTo 1){ //1 <= i && i <= 4 并且反向循环，即4、3、2、1
        print(i)
    }
    for (i in 1 until 4) {// => 1 <= i && i < 4
        print(i)
    }
    ```

- 控制流
    - kotlin没有三元表达式`a ? b : c `，可以使用if代替，`if (a) b else c`

    - `when`:kotlin没有switch，可以使用when来替代，事实上也会被编译成switch
        ```kotlin
         override fun onOptionsItemSelected(item: MenuItem):Boolean{
             //因为when的分支返回值一致，可以直接将return写在这里
            return when (item.itemId) {
                R.id.home -> consume { navigateToHome() }
                R.id.search -> consume { MenuItemCompat.expandActionView(item) }
                R.id.settings -> consume { navigateToSettings() }
                else -> super.onOptionsItemSelected(item)
            }
         }
        ```
        when每一分支是独立的，因此不会有java的缺少`break`而穿透的情形   
        kotlin对when做了拓展，其还可以代替`if()else if() else`块：
        ```kotlin
        val a :Any = 0
        when (a) {
            0, 1, 2 -> {
            }
            is Double -> {
            }
            returnBoolean(a) -> {
            }
            else -> {
            }
        }
        //也可以不带参数
        when {
            a is Double -> {
            }
            a == 0 || a == 1-> {
            }
            returnBoolean(a) -> {
            }
            else -> {
            }
        }
        ```
        kotlin的when会逐层检查是否符合，如果符合则会调用其分支。多个符合也只会调用第一个，因为其是使用`if-else`实现的
    
- 返回与跳转
    - return/break/continue  默认范围在直接包围它的函数，但是你可以用lable标签来指定返回的位置
        ```kotlin
        out@ for (i in 1..100) {
            inner@ for (j in 1..100) {
                if (……) 
                    break@out //会直接返回到外部循环
            }
        }
        ```


## 一些细节

- kotlin对java的简化，比如`arrayListOf(1,2,3)`，这一部分不用记，按照java的方式写后as会自动提示，多提示几遍就记住了
- 字符串拼接，使用`${}`可以直接调用属性或者函数：`val str = "a = ${a.getInt()}" `
- `data class`：相当于java的自定义数据类，data class只需要定义属性，kotlin会为其自动实现`toString()`、`hashCode()`、`equals`三个方法
- kotlin的函数可以直接写在文件中而无需类包裹，这样的方法全局可用，但实际上kotlin编译成java时会包裹一个文件名加上`kt`后缀的类，java调用这样的方式时需要使用这个类目来调用这个方法，此处可以在文件顶行(在package语句前)使用`@file:JvmName("类名")`来自定义类名，如果有多个文件使用相同类名，还可以使用`@file:JvmMultifileClass`来将这些文件编译到一起
- 对于类似于自定义view有多个构造函数的且有默认值的情形，可以使用`@JvmOverloads`来简化写法
    ```kotlin
    class CustomView @JvmOverloads constructor(context: Context, attrs: AttributeSet?=null, defStyleAttr: Int=0) : View(context, attrs, defStyleAttr){
        init {
            val typedArray = context.obtainStyledAttributes(attrs, R.styleable.CustomView)
            typedArray.recycle()
        }
    }
    ```
    `@JvmOverloads`会自动生成有默认值的次构造函数

## kotlin拓展

- 属性委托： https://www.kotlincn.net/docs/reference/delegated-properties.html
    - 某些属性具有延迟属性或者可观察属性时，可使用属性委托来赋值，委托关键字是`by`，如
        ```kotlin
        val btn by lazy { findViewById<Button>(R.id.btn) } //因为返回值固定，因此可以使用类型推断省略声明
        ```
        因为btn只有在`setContentView`之后才能被找到，作为属性却要先声明，因此可以使用属性委托先声明一个`lazy`的值，在第一次调用时再从`lazy`中调用`findViewById`然后赋值给btn。(lazy是kotlin的一个委托方法类，类似的委托也可以自行实现)  
        注意：委托的实现方法实际上会在属性被第一次使用时调用，如果不符合条件，如btn在setContentView之前被使用，仍会报错，实际使用中，也要注意与context相关的委托调用的生命周期，也要注意线程相关  
        如果完全依照java的写法，其实应该是：
        ```kotlin
        lateinit var btn: Button 

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(...)
            btn = findViewById(R.id.btn)
        }
        ```

- 函数类型:
    - kotlin可以使用与函数签名相同的方式来当作类型，这种类型即函数类型
        ```kotlin
        val clickListener : (pos: Int)->Unit //参数名pos可以省略，但是建议保留用来表明参数的意义
        ```
        表示一个具有 接收一个Int参数，返回一个Unit即无返回 的函数签名的 函数类型，返回类型`Unit`不能省略
    - 函数类型实例化：
        - lambda表达式:
            ```kotlin
            val clickListener : (pos: Int) -> Unit = { pos ->
            }
            ```
            此时变量`clickListener`已被赋值，调用`clickListener`相当于调用被赋值给`clickListener`的方法     
            此时，依然可以使用类型推断，即：
            ```kotlin
            val clickListener = { pos: Int ->
            }
            ```
        - 匿名函数：
            ```kotlin
            val clickListener : (pos: Int) -> Unit = fun(pos:Int){ 
            }
            //或者
            val clickListener = fun(pos: Int){ 
            }
            ```

    - 调用: 可以像函数一样调用 `clickListener(1)`，也可以使用`clickListener.invoke(1)`

- 高阶函数:
    - 将函数类型当作参数或者返回值的函数
        ```kotlin
        fun updateIndex(index: Int, func: (pos: Int) -> Unit) { //func是自定义的函数名，类似于参数名称
            if (index > 10) {
                func.invoke(index) //此处会调用传入的函数
            }
        }
        
        //调用
        //直接将具有相同签名的函数类型传入
        updateIndex(1,clickListener)
        //调用时生成一个函数并传入
        updateIndex(1, { a->    // a是函数的参数名，可以自定义，跟java一样
        })
        //当kotlin最后一个参数是函数且调用的时候生成时，可以将{}写到参数()外，即
        updateIndex(1) { a-> 
        }
        ```
        高阶函数将函数当作参数传递，可以以很少代码实现回调或者监听代码，甚至不用声明回调接口 

    - 高阶函数理解上可以看作传入了一个带这个函数类型签名方法的接口类

    - `inline`关键字：因为java不支持函数类型，所以kotlin的函数类型和高阶函数实际上是生成了一个对象来实现的。如果在循环中大量调用高阶函数，则会由内存损耗，也有内存溢出的风险，此时可以使用`inline`关键字来修饰函数，即:
        ```kotlin
        inline fun updateIndex(index: Int, func: (pos: Int) -> Unit) { 
            if (index > 10) {
                func.invoke(index) //此处会调用传入的函数
            }
        }
        ```
        用`inline`修饰的方法会在编译时进行优化，即将内联函数的操作部分直接替换到调用处，来提升性能
        
    - `noinline`：内联函数内部，函数参数被其它非内联函数调用时，编译器会报错，为了解决这个问题，可以给函数参数加上`noinline`关键字

    - `inline`与`noinline`关键字的使用：高阶函数都可以加上`inline`，除非它报错      

- reified: 泛型具体化的类型参数，即泛型可以被当作具体的类型来使用
    ```kotlin
    fun <reified T: Activity> startActivity() {
        startActivity(Intent(this, T::class.java))
    }
    //调用
    startActivity<MainActivity>()
    ```
- 拓展函数：
    - koltin可以给一个已经存在的类拓展新的方法，而无需继承或者使用像装饰者这样的设计模式。

        ```kotlin
        //定义
        //out是一个类型限定，类似于java的Class<? extend Activity>
        fun Context.startActivity(clazz: Class<out Activity>) { 
            //Context即需要被拓展方法的类，startActivity是自定义的方法名
            //此方法可以被Context及其子类调用
            startActivity(Intent(this, clazz)) 
            //这里调用了Context里的startActivity(Intent)方法来实际实现
            //this即调用的Context的this
            //在方法体内，可以被看做在Context类里面，来调用其方法或者属性
        }
        //调用
        class MainActivity : BaseActivity(){

            companion object{

                fun startMainActivity(context:Context){
                    context.startActivity(MainActivity::class.java)
                    //class.java返回一个KClass，可以被当作java的class使用
                }
            }

            fun test(){
                //context子类可以直接调用
                startActivity(OtherActivity::class.java) 
            }
        }
        ```
        拓展方法可以写在类里，类范围可用，如果写在单独的kt文件中，则全局可用    
        实际上kotlin编译后是生成了一个工具类并将被拓展的类当作参数传入一个拓展的方法中，在调用代码处则是调用实际生成的工具类调用拓展方法   
        
- 内置函数：
    - `run`：在调用传入的函数后，返回函数的返回值，函数范围内直接调用调用者的方法，具体实现可以查看源码，常用来做非空判断
        ```koltin
        a?.let{ return this+1 } ?: retutn 2
        ```
    - `with`：在调用传入的函数后，返回调用者本身，函数范围内直接调用调用者的方法，常用作初始化
        ```koltin
        addView(ImageView(context).apply{
            setBackgroundColor(Color.RED)
        })
        ```
    - `takeIf`: 传入一个返回值为bool的函数，当函数返回true时返回调用者，否则返回空
        ```kotlin 
        val isTrue = intent?.getBooleanExtra(KEY,false).takeIf { it == true} ?: return
        ```
        当intent为空或者取出的值为false时都将return