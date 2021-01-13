# 技术

- 简单用法见最后

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [ViewBinding](#viewbinding)
- [DataBinding](#databinding)
- [ViewPager2](#viewpager2)
- [Navigation](#navigation)
- [Paging](#paging)
- [Hilt](#hilt)
- [AppStartup](#appstartup)
- [DataStore](#datastore)
- [未完成](#未完成)
- [ViewBinding使用](#viewbinding使用)
- [DataBinding使用](#databinding使用)
- [ViewPager2使用](#viewpager2使用)
- [Hilt的使用](#hilt的使用)
- [Startup使用](#startup使用)
- [DataStore使用](#datastore使用)

<!-- /code_chunk_output -->

## ViewBinding

- viewBinding用来查找布局文件中的控件，替代`findViewById()`和`ButterKnife`以及`kotlin-android-extensions`

- 官方文档：https://developer.android.google.cn/topic/libraries/view-binding?hl=zh_cn

- 使用：[ViewBinding使用](#Viewbinding使用)

- 优点
    - ViewBinding简单好用, as原生支持, 创建或者更改xml都会自动编译更改且无感知, 点击类直接跳转xml文件
- 缺点
    - 所有类都需要编译后才能找到算是一个缺点

## DataBinding 

- `dataBinding`用来绑定数据与视图，`dataBinding`有`viewBinding`的功能，同时可以在布局文件中直接将控件与数据绑定，支持单向绑定和双向绑定

- 官方文档：https://developer.android.google.cn/topic/libraries/data-binding?hl=zh_cn

- 使用：[DataBinding使用](#DataBinding使用)

- 优点：
    - 带有`viewBinding`的功能，但必须要有`layout`标签
    - as原生支持，可与liveData配合使用
    - 绑定支持绑定表达式和自定义绑定适配器，也支持类的方法的使用，并不呆板，可以看作代码实现然后在xml进行调用
    - 使用dataBinding可以省略很多模板代码
    - dataBinding比较灵活，可以简单使用单向绑定，也可以使用双向绑定，并不强制
- 缺点：
    - 使用dataBinding会导致内容分离，即将数据显示视图的过程中一部分方法在activity中一部分在xml中，需要熟悉否则会对代码阅读产生障碍
    - dataBinding完全使用有一定门槛
    - dataBinding写在xml中，当前版本虽然支持对错误的提示但是并不及代码中的错误提示智能
    - dataBinding布局必须要有layout标签，因此如果页面由多个布局在代码中拼接，则对页面的绑定需要自行判断调用，对`include`之类在xml中完成布局的无影响，带有databinding的`include`也可正常使用

## ViewPager2

- viewpager的升级版本，`viewpager2`基于`RecyclerView`

- 官方文档：https://developer.android.google.cn/guide/navigation/navigation-swipe-view-2

- 当前版本：1.0.0

- 使用：[ViewPager2使用](#ViewPager2使用)

- 优点：
    - 默认无缓存，且只创建当前`Fragment`
    - 能正确处理当`offscreenPageLimit`为1时的`fragment`的`onStart`和`onResume`的生命周期
    - 可以使用`RecyclerView`的`LayoutManger`来做转场动画

##  Navigation

- 用于`Fragment`间页面跳转，可以用来替代`FragmentTransaction`相关的api，适合一个activity多个fragment组成的情形
- 可以理解为对fragment的事务进行了升级，并完善了动画以及图形化支持

- 官方文档：https://developer.android.google.cn/guide/navigation

- 当前版本：2.3.2

- 优点：
    - as原生支持，且支持视图式编程，跳转结构清晰明了
    - 一个activity多个fragment使得编程形式十分统一
- 缺点：
    - 所有的页面使用fragment完成，但其还是在acivity上，与android的交互如`StatusBar`之类的还是要经过activity
    - 基本支持activity的过场动画，但是需要设置，不如activity简便

## Paging

- 官方分页库

- 官方文档：https://developer.android.google.cn/topic/libraries/architecture/paging?hl=zh_cn

- 当前版本：2.1.2 / 3.0.0-alpha11
- paging有两个版本，paging2是目前的稳定版本，但paging3重写了paging2，更改了paging2的结构和api，但目前仍处于alpha版本中，其使用kotlin语言，使用flow


## Hilt

- 官方的依赖注入库，用于注入对象解耦，是`dagger2`的android场景化

- 官方文档：
    - https://developer.android.google.cn/training/dependency-injection/hilt-android?hl=zh_cn     
    - https://dagger.dev/hilt/gradle-setup
- 参考: https://blog.csdn.net/guolin_blog/article/details/109787732

- 当前版本：2.30-alpha

- 使用：[Hilt的使用](#Hilt的使用)

- 优点：
    - 解耦合
    - 相较于`dagger2`，`hilt`难度不高，编写的样本代码很少
    - as支持注入跳转
- 缺点：
    - 需要理解注入体系
    - 会生成很多的代理类，因此偶尔错误不会指向自己的代码而指向代理类中

## AppStartup

- 用于初始化任务，许多第三方库利用`ContentProvider`可以在xml文件中注册并先于`Application`执行来进行无感知初始化并获取context，但过多的库使用多个`ContentProvider`会增加启动时间，所以就出了这个库来统一初始化任务

- 官方文档： https://developer.android.google.cn/topic/libraries/app-startup
- 参考： https://guolin.blog.csdn.net/article/details/108026357

- 当前版本: 1.0.0

- 使用： [Startup使用](#Startup使用)

## DataStore

- 用于替代`SharedPreferences`，使用flow实现异步返回，避免阻塞主线程

- 官方文档: https://developer.android.google.cn/topic/libraries/architecture/datastore#preferences-datastore

- 当前版本：1.0.0-alpha04

- 使用： [DataStore使用](#DataStore使用)

- 优点：
    - 避免了`SharedPreferences`的漏洞，诸如阻塞线程，有造成anr的风险等问题
- 缺点：
    - 需要熟悉协程，因为它的写入是在协程中进行
    - 需要熟悉`flow`，因为其返回值是一个`flow`对象

## 未完成
- Rxjava / 协程flow
- objectbox / room

## ViewBinding使用

1. 启用: 在`build.gradle`文件中设置
    ```kotlin
    android {
        buildFeatures {
            // dataBinding
            dataBinding true
        }
    }
    ```
2. 使用
    - ViewBinding会在创建`layout`文件后编译一个以文件名开头，以Binding结尾的类，使用该类即可调用所有有id的控件
        ```kotlin
        //ActivityMainBinding即R.layout.activity_main的bing类
        //因为ActivityMainBinding是根据layout文件生成的，因此无需声明xml路径
        val binding = ActivityMainBinding.inflate(LayoutInflater.from(this))
        //binding.root即inflate的view对象
        setContentView(binding.root)
        //直接根据R.id.main_tv生成的字段调用控件, 下划线会变成驼峰格式
        binding.mainTv.setTextColor(Color.BLACK)

        //如果控件多可以使用run函数, 可以少写binding
        binding.run {
            mainTv1.setTextColor(Color.BLACK)
            mainTv2.setTextColor(Color.BLACK)
            mainTv3.setTextColor(Color.BLACK)
        }
        ```
    - 如果不需要生成Binging类，则需要在xml文件中最外层的标签内添加`tools:viewBindingIgnore="true"`
## DataBinding使用
1. 启用: 在`build.gradle`文件中设置
    ```kotlin
    android {
        buildFeatures {
            // dataBinding
            dataBinding true
        }
    }
    ```
2. xml布局需要被`layout`标签包裹，同时使用`<data>`标签来声明数据源  
(在as里，xml文件中选择xml文档声明行或者最外部标签，快捷键`alt+enter`选择`convert to binding layout`即可自动生成结构)
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto">
        <data>
            <!--声明的数据源，可以有多个，每一个都要这样声明-->
            <!--name是自定义别名-->
            <!--type指向实际的类，as支持路径提示-->
            <!--要实际支持双向绑定，要绑定的数据必须是一个可观察性质的数据，
            最实用的类型是livedata
            此处MainViewModel中的user即一个LivaData类型的变量-->
            <variable
                name="viewmodel"
                type="com.yunfeng.testlib.MainViewModel" />
        </data>
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical">
            <!--除了单纯的调用数据，dataBinding还支持调用数据源中的方法，
            也支持一些绑定表达式，??即绑定表达式-->
            <TextView
                android:id="@+id/main_tv"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@{viewmodel.user.name ?? @string/app_name}" />
            <!--app:avatar是自定义的绑定适配器，
            可以看作将实现方法在xml中以这种方式调用，
            as支持自定义方法提示，支持点击跳转到方法源码-->
            <ImageView
                android:layout_width="80dp"
                android:layout_height="80dp"
                app:avatar="@{viewmodel.user.avatar}" />
            <!--@={}即双向绑定，当EditText的text值发生变化时，
            viewmodel.user.address的值也会发生变化，反之亦然-->
            <EditText
                android:id="@+id/main_et"
                android:layout_width="300dp"
                android:layout_height="wrap_content"
                android:text="@={viewmodel.user.address}" />
        </LinearLayout>
    </layout>
    ```     
    自定义绑定适配器，可以写在一个文件中，as会自动编译并调用
    ```kotlin
    //两个参数分别是调用的控件和绑定的数据类型
    @BindingAdapter("avatar")
    fun loadAvatar(imageView: ImageView, any: Any?) {
        Glide.with(imageView)
            .load(any)
            .placeholder(R.mipmap.ic_launcher)
            .into(imageView)
    }
    ```
3. 界面中使用
    ```kotlin
    private val model by lazy { ViewModelProvider(this).get(MainViewModel::class.java) }

    override fun onCreate(savedInstanceState: Bundle?) {
        //此处也可以按照viewBinding的写法
        val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.run {
            //绑定生命周期
            lifecycleOwner = this@MainActivity
            //绑定声明的数据源即可将数据显示到页面中
            //更改model中的user即可自动更改页面显示
            viewmodel = model
        }
    }

    class MainViewModel : ViewModel() {
        val user = MutableLiveData(User(name = "name123", avatar = "avatar://www", address = null))
    }
    ```

## ViewPager2使用
1. 启用
    ```kotlin
    dependencies {
        implementation "androidx.viewpager2:viewpager2:1.0.0"
    }
    ```
2. 继承`FragmentStateAdapter`并实现`createFragment()`和`getItemCount`再将该adapter通过viewPager2的setAdapter设置即可

## Hilt的使用
1. 启用
    ```kotlin
    buildscript {
        dependencies {
            classpath 'com.google.dagger:hilt-android-gradle-plugin:2.30-alpha'
        }
    }
    //-------------------------------------------------//
    //需要使用kapt
    apply plugin: 'kotlin-kapt'
    apply plugin: 'dagger.hilt.android.plugin'

    android {
        //需要使用java8的特性
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
    }
    dependencies {
        implementation "com.google.dagger:hilt-android:2.30-alpha"
        kapt "com.google.dagger:hilt-android-compiler:2.30-alpha"
        //hilt对viewModel的优化库
        implementation 'androidx.hilt:hilt-lifecycle-viewmodel:1.0.0-alpha02'
        kapt 'androidx.hilt:hilt-compiler:1.0.0-alpha02'
    }
    ```
2. 入口：自定义app类添加注解`@HiltAndroidApp`并在xml中声明app类，这一步是必须的，这是hilt的入口
3. 使用：
    ```kotlin
    //SingletonModule是一个自定义类
    //用于提供一些注解对象的生成，主要是第三方的对象，需要使用@Module
    //@InstallIn()表明作用域，即在该作用域下这些注解可以这样生成
    //SingletonComponent::class是hilt的类，表明作用域为全局单例
    @Module
    @InstallIn(SingletonComponent::class)
    object SingletonModule {

        //当在该作用域下使用一个Retrofit的依赖注入对象时，hilt会从此处生成一个Retrofit对象
        //当然如果是单例的只会生成一次
        //提供注解对象需要使用@Provides
        //此方法为自定义方法，返回值即表明提供的注解对象，此处为Retrofit
        //参数是所需要的参数，如果该注解需要参数，那么该参数也必须可以依赖注入生成，见provideOkHttpClient方法
        @Provides
        fun provideRetrofit(client: OkHttpClient): Retrofit {
            return Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create(Gson()))
                .client(client)
                .build()
        }

        @Provides
        fun provideOkHttpClient(): OkHttpClient {
            return OkHttpClient.Builder().build()
        }

        @Provides
        fun provideApi(retrofit: Retrofit): Api = retrofit.create(Api::class.java)
    }
    //@Inject注解构造即告诉hilt当需要一个新的TestRepository对象时需要怎样生成
    //类似于@Provides但是被简化了，也可以以类似 @Provides的方式提供
    //同样的，如果有参数，则参数也必须可以提供依赖注入对象
    class TestRepository @Inject constructor() : BaseRepository() {

        //通过依赖注入直接生成一个Api对象
        //对于使用者来说，无需关心api是怎样生成的，也无需依赖api生成所依赖的类，这就是依赖注入的作用
        //诸如工厂方法、静态方法生成之类的，不是在调用处创建对象的都是依赖注入的概念
        //因为要依赖注入赋值，变量不能是val声明并且不能私有，构造函数同理
        @Inject
        lateinit var api: Api

        //依赖注入是根据对象类型生成的
        //如果一个类的依赖注入的作用域非单例的(非全局单例或者作用域里非单例)
        //那么注入一次，即会调用注入方法(构造函数或者@Provides)一次
        //此处因为Api是单例注入的，所以api和api2是相同对象，否则，会是两个不同对象
        @Inject
        lateinit var api2: Api

        fun test(){
            //api可以直接使用
            //此时hilt会根据作用域层层搜索一个Api对象，找到SingletonModule类中的provideApi方法
            //然后将返回值赋给api
            api.search()
        }
    }

    //ViewModelInject是hilt-lifecycle-viewmodel库的注解
    //如果不引入这个库则需要使用@ActivityRetainedScoped注明在activity生命周期内保持单一，并使用@Inject提供构造
    class TestJetpackViewModel @ViewModelInject constructor(
        private val repository: ArticleRepository) :ViewModel() {

    }

    //如果要在Activity中使用依赖注入则@AndroidEntryPoint是必须的声明，这是hilt的入口之一
    @AndroidEntryPoint
    class TestJetpackActivity : AppCompatActivity() {

        //因为ViewModelInject注解，所以viewModel可以以原来的方式生成
        private val viewModel by { ViewModelProvider(this).get(TestJetpackViewModel::class.java) }

    }
    ```
4. 注意点：hilt库最主要要注意的就是作用域，不同的作用域会生成不同的对象

## Startup使用
1. 启用
    ```kotlin
    dependencies {
        implementation "androidx.startup:startup-runtime:1.0.0"
    }
    ```
2. 实现
    ```kotlin
    class MyInitializer : Initializer<Unit> {
        override fun create(context: Context) {
            //进行初始化
        }
        //如果依赖其它初始任务，则返回其列表，startup会在依赖项目初始化只会再初始化本类
        override fun dependencies(): MutableList<Class<out Initializer<*>>> {
            return mutableListOf()
        }
    }
    ```
3. 注册
    ```xml
    <provider
        android:name="androidx.startup.InitializationProvider"
        android:authorities="${applicationId}.androidx-startup"
        android:exported="false"
        tools:node="merge">
        <!--name需要更改为实现了Initializer的类，其余内容诸如authorities不可更改-->
        <meta-data android:name="com.example.ExampleLoggerInitializer"
                tools:node="remove" />
    </provider>
    ```
4. 注意：此类先于application执行，因此只适合不依赖application的初始化

## DataStore使用
1. 启用:
    - datastore有两种版本，一种使用键值对，另一种使用`Proto`结构，这是一种诸如`xml`但与`xml`不同的结构，此处只实验了第一种版本
    ```kotlin
    dependencies {
        implementation "androidx.datastore:datastore-preferences:1.0.0-alpha04"
    }
    ```
2. 创建
    ```kotlin 
    //这是一个kt的拓展函数
    val dataStore = context.createDataStore("datastore_name")
    ```
3. 写入
    - 写入是在子线程，且是在协程中
    - 键值对的键是一个`Preferences.Key<T>`类型，可以用`preferencesKey(String)`方法生成
    - `preferencesKey(String)`方法只支持`Int`、`String`、`Boolean`、`Float`、`Long`、`Double`类型
    ```kotlin
    dataStore.edit {
        //子线程
        it[preferencesKey<Boolean>("isset")] = true
    }
    ```
4. 读取：读取返回的是一个`flow`对象，而非直接返回结果
    ```kotlin
    val isSetFlow: Flow<Boolean> = dataStore.data.map {
        it[preferencesKey("isset")] ?: false
    }
    isSetFlow.collect {
        //获取到结果it
    }
    ```