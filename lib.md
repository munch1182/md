# 技术

### dataBinding和viewBinding

- 用处：viewBinding可以用来替代`findViewById`和`ButterKnife`, 而`dataBinding`则是用来双向绑定数据与视图

- 官方文档：
    - [viewBinding](https://developer.android.google.cn/topic/libraries/view-binding?hl=zh_cn)
    - [dataBinding](https://developer.android.google.cn/topic/libraries/data-binding?hl=zh_cn)

- 使用：
    1. 启用
        ```kotlin
        android {
            buildFeatures {
                // viewBinding
                viewBinding true
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

            //如果控件多可以使用kotlin的run函数, 来避免多次使用binding
            binding.run {
                mainTv1.setTextColor(Color.BLACK)
                mainTv2.setTextColor(Color.BLACK)
                mainTv3.setTextColor(Color.BLACK)
            }
            ```
    3. 优点
        - ViewBinding简单好用, as原生支持, 创建或者更改都会自动编译, 点击类直接跳转xml文件, `ButterKnife`推荐
    4. 缺点
        - 所有类都需要编译后才能找到算是一个缺点
- hilt 依赖注入 需不需要
- paging 需不需要
- Rxjava / 协程flow
- objectbox / room
- viewpager2 - 解决fragment生命周期的问题