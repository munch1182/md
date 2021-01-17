# 技术

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [ViewBinding](#viewbinding)
- [DataBinding](#databinding)
- [ViewPager2](#viewpager2)
- [Navigation](#navigation)
- [Paging](#paging)
- [Room](#room)
- [Hilt](#hilt)
- [AppStartup](#appstartup)
- [DataStore](#datastore)
- [ViewBinding使用](#viewbinding使用)
- [DataBinding使用](#databinding使用)
- [ViewPager2使用](#viewpager2使用)
- [Hilt的使用](#hilt的使用)
- [Startup使用](#startup使用)
- [DataStore使用](#datastore使用)
- [Paging3的使用](#paging3的使用)
- [Room的使用](#room的使用)

<!-- /code_chunk_output -->

## ViewBinding

- viewBinding用来查找布局文件中的控件，替代`findViewById()`和`ButterKnife`以及`kotlin-android-extensions`

- 官方文档：https://developer.android.google.cn/topic/libraries/view-binding?hl=zh_cn

- 使用：[ViewBinding使用](#Viewbinding使用)

- 优点
    - ViewBinding简单好用, as原生支持, 创建或者更改xml都会自动编译更改且无感知
- 缺点
    - 对应的类是生成的而且依赖文件名，如果更改xml文件名需要手动更改生成类的依赖

## DataBinding 

- `dataBinding`用来绑定数据与视图，`dataBinding`有`viewBinding`的功能，同时可以在布局文件中直接将控件与数据绑定，支持单向绑定和双向绑定

- 官方文档：https://developer.android.google.cn/topic/libraries/data-binding?hl=zh_cn

- 使用：[DataBinding使用](#DataBinding使用)

- 优点：
    - 带有`viewBinding`的功能，但必须要有`layout`标签
    - as原生支持，可与liveData配合使用
    - 绑定支持绑定表达式和自定义绑定适配器，也支持类的方法的使用，并不呆板，可以看作代码实现然后在xml进行调用
    - 使用dataBinding可以省略很多模板代码，特别是在`RecyclerView`的`item`中
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
    - 能正确处理当无缓存时的`fragment`的`onStart`和`onResume`及对应的生命周期(当缓存多个时被缓存的`fragment`的`onStart`方法仍会在创建时调用)
    - 基于`recyclerView`可以使用其特性，比如利用`LayoutManger`来做转场动画或者用`ItemDecoration`来绘制背景

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

- 官方文档：
    - https://developer.android.google.cn/topic/libraries/architecture/paging?hl=zh_cn
    - https://developer.android.google.cn/topic/libraries/architecture/paging/v3-overview
- 当前版本：2.1.2 / 3.0.0-alpha11
- paging有两个版本，paging2是目前的稳定版本，但paging3重写了paging2，更改了paging2的结构和api，但目前仍处于alpha版本中，其使用kotlin语言，使用flow

- 使用：[Paging3的使用](#paging3的使用)

- 优点：
    - 官方支持，自动加载更多而无需手动处理相关逻辑
    - 有了adapter的`refresh`、`retry`等api，处理刷新、重试逻辑异常简单
    - 与`room`的配合可以简化很多代码
    - 可以以比较少的代码实现带数据库缓存的分页，对于这类需求帮助很大
- 缺点：
    - 与其它官方的`alpha`版本相比，`paging3`当前并不稳定，部分api仍处于实验中
    - 如果要使用数据库缓存，而使用的数据库不支持`paging`的特性，则需要自行写代码去实现

## Room

- 官方基于SQLite的数据库

- 官方文档: https://developer.android.google.cn/topic/libraries/architecture/room
- 当前版本: 2.2.5

- 使用： [Room的使用](#room的使用)

- 优点：
    - 官方支持，基于sqlite，无需额外引入，打包不会增加额外的大小
    - 自行书写sql语句，可以书写诸如多表内联查询这种语句，更加自由灵活
    - as支持表名提示，字段提示，错误检查，也支持数据库直接查看和语句测试，比较方便
    - 与其它jetpack组件联系紧密，比如`paging`
- 缺点：
    - 需要手写sql语句，需要自行处理数据库关联，需要相关知识
    - 速度偏慢，虽然用户感知差异较小，但对比其它数据库速度仍有差距
    - 需要自行完成版本管理，进行升级和降级，特别是在sqlite没有删除列指令的情况下降级比较繁琐

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
    - 相较于`dagger2`，`hilt`难度很低，编写的样本代码很少
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

---

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
        //ActivityMainBinding即R.layout.activity_main的bind类
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
2. xml布局需要被`layout`标签包裹，同时使用`<data>`标签来声明要使用的类
(如果是在`dataBinding`中单纯使用`viewBinding`的功能需要去掉`<data>`标签)
(在as里，xml文件中选择xml文档声明行或者最外部标签，快捷键`alt+enter`选择`convert to binding layout`即可自动生成结构)
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto">
        <data>
            <!--声明的类，可以有多个，每一个都要这样声明-->
            <!--name是自定义别名-->
            <!--type指向实际的类，as支持路径提示-->
            <!--要实际支持双向绑定，要绑定的数据必须是一个可观察性质的数据，
            最实用的类型是livedata
            此处MainViewModel中的user即一个LivaData类型的变量-->
            <variable
                name="viewmodel"
                type="com.yunfeng.testlib.MainViewModel" />
        </data>
        <!--原本的视图结构-->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical">
            <!--除了单纯的调用数据，dataBinding还支持调用数据源中的方法，
            也支持一些绑定表达式，??即表示为空时的绑定表达式-->
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
2. 实现`FragmentStateAdapter`再将该adapter通过viewPager2的setAdapter设置即可

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
    //如果无需这些对象则无需这样实现
    //@InstallIn()表明作用域，即在该作用域下这些注解可以这样生成
    //SingletonComponent::class是hilt的类，表明类里的方法的作用域为全局单例
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
4. 注意点：
    - hilt库最主要要注意的就是作用域，不同的作用域会生成不同的对象
    - 如果一个类要使用hilt注入的变量，那么这个类必须可以被hilt依赖注入，否则应该使用构造传递
    - 在模块化中，hilt会在编译时生成注入方法，因此在壳包必须可以访问所有依赖注入对象

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
        //如果依赖其它初始任务，则返回其列表，startup会在依赖项目初始化之后再初始化本类
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
        <!--name需要更改为实现了Initializer的类-->
        <meta-data android:name="com.example.ExampleLoggerInitializer"
                tools:node="remove" />
    </provider>
    ```
4. 注意：此类先于application执行，因此只适合不依赖application的初始化

## DataStore使用
1. 启用:
    - datastore有两种版本，一种使用键值对，另一种使用`Proto`结构，这是一种诸如`xml`但与`xml`不同的结构，使用时需要定义架构而无法直接使用，此处只实验了第一种版本
    ```kotlin
    dependencies {
        implementation "androidx.datastore:datastore-preferences:1.0.0-alpha04"
    }
    ```
2. 创建
    ```kotlin 
    //这是一个kt的拓展函数
    val dataStore = context.createDataStore("datastore_name")
    //实际即
    PreferenceDataStoreFactory.create(
        corruptionHandler = null,
        migrations = listOf(),
        scope = CoroutineScope(Dispatchers.IO + SupervisorJob()) {
        File(context.filesDir, "datastore/datastore_name.preferences_pb")
    }

    ```
3. 写入
    - 写入方法是在协程中
    - 写入的线程由`DataStore`创建方法的`CoroutineScope`决定的，默认是在`IO`线程
    - 键值对的键是一个`Preferences.Key<T>`类型，可以用`preferencesKey(String)`方法生成
    - `preferencesKey(String)`方法只支持`Int`、`String`、`Boolean`、`Float`、`Long`、`Double`类型作为`Preferences.Key<T>`的泛型
    ```kotlin
    dataStore.edit {
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
5. 默认存储的文件路径为`file/datastore/自定义名.preference_pb`

## Paging3的使用
1. 启用
    ```kotlin
    dependencies {
        implementation "androidx.paging:paging-runtime:3.0.0-alpha11"
    }
    ```
2. 架构
    - 单一数据源，只从数据库或者只从服务器中获取数据，无缓存
    ![paging3 architecture1](https://developer.android.google.cn/topic/libraries/architecture/images/paging3-library-architecture.svg)
    - 将数据库作为单一数据源，远程数据先更新数据库，再通过数据库的数据刷新页面，数据库同时作为缓存存在
    ![paging3 architecture2](https://developer.android.google.cn/topic/libraries/architecture/images/paging3-layered-architecture.svg)
    - 单一数据源适合简单或者页面数据要求准确或者有时效性，而数据库作为缓存的架构适合展示类且变化不大的页面
3. 使用
    ```kotlin
    //1. 实现PagingDataAdapter,相较于RecyclerView.Adapter，
    //   PagingDataAdapter需要传入一个DiffUtil.ItemCallback用以比较数据
    //   其余需要实现的部分是一致的
    class RvAdapter :
        PagingDataAdapter<User, BindViewModel>(object : DiffUtil.ItemCallback<User>() {
            //用以判断两个参数是否一致
            //可以根据业务逻辑判断，也可以根据hash值判断
            override fun areItemsTheSame(oldItem: User, newItem: User): Boolean {
                return oldItem.id == newItem.id
            }
            //判断内容是否一致，用以刷新显示
            override fun areContentsTheSame(oldItem: User, newItem: User): Boolean {
                return oldItem.name == newItem.name
            }
        }) {
            ...
        }
    //2. 将PagingDataAdapter设置给rv
    rv.adapter = RvAdapter()
    //3. 获取一个PagingData类型的数据，然后传递给PagingDataAdapter
    //   getAllUser()返回的是一个Pager<Int, User>类型，见下文
    //   .flow是获取Pager内部维护的flow流，也是将Pager转为了flow，
    //   在flow中可以获取数据源传递的PagingData
    getAllUser()
        .flow
        .collect {
            //PagingDataAdapter接收数据
            rvAdapter.submitData(this.lifecycle, it)
        }
    //4. 构建Pager
    //a. 单一数据源，只从数据库或者只从服务器中获取数据
    fun getAllUser(): Pager<Int, User> {
        //自行构造一个Pager实例
        //pageSize是每页数量，initialKey是初始key值，即初始页码
        //PagingConfig主要用来设置页面相关，包括当滑动到倒数第几个就开始加载更多等属性
        return Pager(PagingConfig(pageSize = 20), initialKey = 0,
            //定义数据源
            pagingSourceFactory = {
                //PagingSource<Int, User>两个泛型，第一个泛型即分页key，作为分页判断的依据，
                //一般是int类型的页码，也可以是其它类型
                //第二个泛型是数据类型
                //这只是一种写法，事实上，room可以直接返回PagingSource类型的数据
                return@Pager object : PagingSource<Int, User>() {
                    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, User> {
                        //页面加载的分页判断
                        val page = params.key ?: 0
                        //模拟从数据库或者服务器中获取数据
                        val list = getListByPage(page)
                        val mockError = false
                        //模拟数据获取错误
                        if (mockError) {
                            return LoadResult.Error(Exception("获取数据失败"))
                        }
                        //获取到数据
                        return LoadResult.Page(list, null, page + 1)
                    }
                }
                //单一数据源，则无需设置此数据源
            }, remoteMediator = null)
    }
    //b. 双层数据源，pagingSourceFactory无效时才从remoteMediator中获取
    //remoteMediator仍是实验性api，需要显示声明
    @ExperimentalPagingApi
    fun getAllUser(): Pager<Int, User> {
        //自行构造一个Pager实例
        return Pager(PagingConfig(pageSize = 20), initialKey = 0,
            //room作为数据源
            //room支持返回DataSource.Factory<Int, ArticleDto>类型，
            //可以直接通过.asPagingSourceFactory()转换为pagingSourceFactory所需类型
            pagingSourceFactory = roomDao.queryAllUser().asPagingSourceFactory(),
            //定义分层数据源
            //官方推荐的架构是pagingSourceFactory用数据库作为唯一数据源，当pagingSourceFactory没有数据时，会调用remoteMediator，
            //此时remoteMediator获取服务器数据，然后写入数据库，再让pagingSourceFactory从数据库中读取
            //要实现这种架构，需要作为pagingSourceFactory的数据库能处理数据失效的情形，
            //自行简单构建的PagingSource是无法处理的，必须与数据库相关联
            //如果pagingSourceFactory不处于无效状态，remoteMediator就不会被调用
            //room可以自动处理，其它数据库可能需要参照实现去处理状态
            remoteMediator = object : RemoteMediator<Int, User>() {
                override suspend fun load(loadType: LoadType,state: PagingState<Int, User>): MediatorResult {
                    //模拟数据获取错误
                    val mockError = false
                    if (mockError) {
                        MediatorResult.Error(Exception("获取数据失败"))
                    }
                    //可以从参数中获取当前key
                    val key = getKey(loedType,state)
                    //从服务器中获取数据
                    val list = api.getAllUser(key)
                    //判断是否还有更多数据
                    val hasMore = judgeHasMore(key,list)
                    //判断并将数据更新到数据库
                    ...
                    //返回成功信号，让paging从数据库中去获取数据，
                    //endOfPaginationReached用以判断是否还有更多数据
                    return MediatorResult.Success(endOfPaginationReached = hasMore)
                }
            })
    }
    ```

## Room的使用
1. 启用
    ```kotlin
    kapt {
        arguments {
            //将room的sql结构存放到该地址
            //书写迁移语句时可以复制语句
            arg("room.schemaLocation", "$projectDir/schemas".toString())
        }
    }
    dependencies {
        def room_version = "2.2.5"
        implementation "androidx.room:room-runtime:$room_version"
        kapt "androidx.room:room-compiler:$room_version"
        // optional - Kotlin Extensions and Coroutines support for Room
        implementation "androidx.room:room-ktx:$room_version"
    }
    ```
2. 使用， 通过定义、注解的方式，`Room`可以自动生成相应的执行实现，以此来简化操作
    ```kotlin
    //1. 定义实体类，需要用@Entity注解
    //tableName 、ColumnInfo都是可选的
    //数据库不支持List类型，可以用两种方法解决
    //数据较为简单的可以使用@TypeConverters(class)来进行转换读写，比如用gson转为string进行读写
    //数据较为复杂的建议使用关系映射@Relation
    @Entity(tableName = "tb_user")
    data class User(
        @PrimaryKey val uid: Int,
        @ColumnInfo(name = "first_name") val firstName: String?,
        @ColumnInfo(name = "last_name") val lastName: String?
    ){
        //忽略的属性，不会被存进数据库
        @Ignore
        var str:String? = null
    }
    //2. 定义Dao，需要使用@Dao注解，用以调用sql语句
    @Dao
    interface UserDao {
        //查询语句，room支持多种返回值，也可以加拓展库去支持更多的返回值类型
        @Query("SELECT * FROM tb_user")
        fun getAll(): List<User>

        //带条件的查询，:userIds即可代表参数
        @Query("SELECT * FROM tb_user WHERE uid IN (:userIds)")
        fun loadAllByIds(userIds: IntArray): List<User>

        //带条件的查询并且限定返回
        //$TB_NAME_USER指向一个常量，等于tb_user
        //room也支持多表内联查询，相较于查询后组合的方式，这种方式更为简单高效
        @Query("SELECT * FROM $TB_NAME_USER WHERE first_name LIKE :first AND " +
               "last_name LIKE :last LIMIT 1")
        fun findByName(first: String, last: String): User

        //room也支持协程
        @Insert
        suspend fun insertAll(vararg users: User)

        //更新方法
        @Query("UPDATE $TB_NAME_USER SET `first_name` = :firstName WHERE `uid` = :uid")
        suspend fun updateFirstName(uid:Int, firstName:String)

        @Delete
        fun delete(user: User)

        //这种调用多个数据方法的方法需要@Transaction声明
        @Transaction
        suspend fun replace(user:User,newUser:User){
            delete(user)
            insertAll(newUser)
        }
    }
    //3. 定义数据库, entities即所有被@Entity声明的类，
    //version即数据库版本，当数据库结构发生变化时，该版本应该要变化，并提供相应的迁移方法，否则无法兼容
    @Database(entities = arrayOf(User::class), version = 1)
    abstract class AppDatabase : RoomDatabase() {
        //用以获取@Dao声明的对象
        abstract fun userDao(): UserDao
    }
    //4. 调用，db应该是单例的
    val db = Room.databaseBuilder(applicationContext,
                //数据库类和数据库名称
                AppDatabase::class.java, "database-name"
            )
            //添加版本迁移方法用以兼容，否则使用版本2数据库的应用打开版本1的数据时会报错
            .addMigrations(Migration1to2())
            .build()
    //调用查询语句
    val user : List<User> = db.userDao().getAll()
    ```
    