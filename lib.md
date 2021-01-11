# 技术

### viewBinding

- 用处：viewBinding用来查找布局文件中的控件，替代`findViewById`和`ButterKnife`以及`kotlin-android-extensions`

- 官方文档：https://developer.android.google.cn/topic/libraries/view-binding?hl=zh_cn

- 使用：
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
    3. 优点
        - ViewBinding简单好用, as原生支持, 创建或者更改都会自动编译, 点击类直接跳转xml文件
    4. 缺点
        - 所有类都需要编译后才能找到算是一个缺点

## DataBinding 

- 用处：`dataBinding`则是用来双向绑定数据与视图，`dataBinding`有`viewBinding`的功能，同时可以在布局文件中直接将控件与数据绑定，当数据或者控件发生改变时，另一方会根据设置自动相应变化
- 官方文档：https://developer.android.google.cn/topic/libraries/data-binding?hl=zh_cn
- 使用：
    1. 启用: 在`build.gradle`文件中设置
        ```kotlin
        android {
            buildFeatures {
                // dataBinding
                dataBinding true
            }
        }
        ```
    2. xml布局需要被`layout`标签包裹，同时使用`<data>`标签来声明数据源(在as里，xml文件中选择xml文档声明行即第一行，快捷键`alt+enter`选择`convert to binding layout`即可自动生成结构)
        ```xml
        <?xml version="1.0" encoding="utf-8"?>
        <layout xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:app="http://schemas.android.com/apk/res-auto">

            <data>
                <!--声明的数据源，可以有多个，每一个都要这样声明-->
                <!--name是自定义别名-->
                <!--type指向实际的数据类,支持路径提示-->
                <variable
                    name="user"
                    type="com.project.app.UserBean" />
            </data>

            <!--原有的布局文件-->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content">

                <!--@{user.name}即绑定数据，user是自定义的别名，name是UserBean的属性，支持代码提示，支持错误检查-->
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="@{user.name}"/>
            </LinearLayout>
        </layout>
        ```
- hilt 依赖注入 需不需要
- paging 需不需要
- Rxjava / 协程flow
- objectbox / room
- viewpager2 - 解决fragment生命周期的问题