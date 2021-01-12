# 技术

- 简单用法见最后

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [viewBinding](#viewbinding)
- [DataBinding](#databinding)
- [viewpager2](#viewpager2)
- [Navigation](#navigation)
- [paging](#paging)
- [hilt](#hilt)
- [未完成](#未完成)
- [viewBinding使用](#viewbinding使用)
- [databinding使用](#databinding使用)
- [viewPager2使用](#viewpager2使用)

<!-- /code_chunk_output -->

## viewBinding

- 用处：viewBinding用来查找布局文件中的控件，替代`findViewById()`和`ButterKnife`以及`kotlin-android-extensions`

- 官方文档：https://developer.android.google.cn/topic/libraries/view-binding?hl=zh_cn

- 使用：[viewBinding使用](#viewbinding使用)

- 优点
    - ViewBinding简单好用, as原生支持, 创建或者更改xml都会自动编译更改且无感知, 点击类直接跳转xml文件
- 缺点
    - 所有类都需要编译后才能找到算是一个缺点

## DataBinding 

- 用处：`dataBinding`用来绑定数据与视图，`dataBinding`有`viewBinding`的功能，同时可以在布局文件中直接将控件与数据绑定，支持单向绑定和双向绑定

- 官方文档：https://developer.android.google.cn/topic/libraries/data-binding?hl=zh_cn

- 使用：[databinding使用](#databinding使用)

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

## viewpager2

- 用处：viewpager的升级版本，`viewpager2`基于`RecyclerView`

- 官方文档：https://developer.android.google.cn/guide/navigation/navigation-swipe-view-2

- 当前版本：1.0.0

- 使用：[viewPager2使用](#viewpager2使用)

- 优点：
    - 默认无缓存，且只创建当前`Fragment`
    - 能正确处理当`offscreenPageLimit`为1时的`fragment`的`onStart`和`onResume`的生命周期
    - 可以使用`RecyclerView`的`LayoutManger`来做转场动画

##  Navigation

- 用处：用于`Fragment`间页面跳转，可以用来替代`FragmentTransaction`相关的api，适合一个activity多个fragment组成的情形
- 可以理解为对fragment的事务进行了升级，并完善了动画以及图形化支持

- 官方文档：https://developer.android.google.cn/guide/navigation

- 当前版本：2.3.2

- 优点：
    - as原生支持，且支持视图式编程，跳转结构清晰明了
    - 一个activity多个fragment使得编程形式十分统一
- 缺点：
    - 所有的页面使用fragment完成，但其还是在acivity上，与android的交互如`StatusBar`之类的还是要经过activity
    - 基本支持activity的过场动画，但是需要设置，不如activity简便

## paging

- 用处：官方分页库

- 官方文档：https://developer.android.google.cn/topic/libraries/architecture/paging?hl=zh_cn

- 当前版本：2.1.2 / 3.0.0-alpha11
- paging有两个版本，paging2是目前的稳定版本，但paging3重写了paging2，更改了paging2的结构和api，但目前仍处于alpha版本中，其使用kotlin语言，使用flow

## hilt

- 用处：官方的依赖注入库，用于注入对象解耦，是`dagger2`的android场景化
- 官方文档：
    - https://developer.android.google.cn/training/dependency-injection/hilt-android?hl=zh_cn     
    - https://dagger.dev/hilt/gradle-setup
- 当前版本：2.30-alpha
- 优点：
    - 解耦合
    - 相较于`dagger2`，`hilt`难度大大降低，编写的样本代码也很少
- 缺点：
    - 需要理解注入体系，有一点的门槛

## 未完成
- Rxjava / 协程flow
- objectbox / room

## viewBinding使用

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
## databinding使用
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

## viewPager2使用
1. 启用
    ```kotlin
    dependencies {
        implementation "androidx.viewpager2:viewpager2:1.0.0"
    }
    ```
2. 继承`FragmentStateAdapter`并实现`createFragment()`和`getItemCount`再将该adapter通过viewPager2的setAdapter设置即可
