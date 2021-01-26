# 组件化

- 将一个完整项目在开发时根据业务分成一个个可以单独运行的组件进行开发，用以分离依赖，降低业务耦合和干扰，减少每个组件的编译时间，而在打包的时候又统一成一个完整的项目app进行编译打包发布。相较于正常的开发流程，组件化会增加一些代码，并且可能会增加代码逻辑。
- 参考： https://blog.csdn.net/guiying712/article/details/55213884

## 步骤

1. **创建组件化开关**，用以控制是否进行组件化编译。
    - 可以直接在`gradle.properties`中添加`runAlone=false`
    - 也可以在项目模块中自建一个`gradle`文件然后声明
        ```java
        ext {
            runAlone = false
        }
        ```
    - 相较于第一种方式，第二种更加灵活，可以为每个组件设置开关并增加总开关
        ```java
        //总开关
        //写成方法可以避免as的简化提示
        static def isApp() {
            return false
        }

        ext {
            //component,component1RunAlone,component2RunAlone是自定义名称
            //componentRunAlone是下面的方法名
            component = [
                    component1RunAlone : componentRunAlone(true),
                    component2RunAlone : componentRunAlone(true),
            ]
        }

        //每个组件是否单独编译的开关的判断，先判断总开关，再判断单独设置
        static def componentRunAlone(runAlone) {
            return !isApp() && runAlone
        }
    - 第二种方法需要声明文件引入，在项目的`build.gradle`顶行加入
        ```java
        apply from: `文件名.gradle``，
        ```
        如果文件有路径，需要添加相应路径
2. **创建组件化结构**
    - Project
        - `app`      (package)
        - `common`    (lib)
        - `lib1`      (lib)
        - `lib2`      (lib)
        - `component1`(component)
        - `component2`(component)
        - `component3`(component)
        - `component4`(component)
    - `app`作为完整应用的壳，最终打包的项目是基于`app`的
    - `common`是基本的功能组件，提供基本功能以及全组件通用功能，同时作为一个路由中心，其与其余`lib`的区别在于，其应该被所有组件依赖
    - `lib1`、`lib2`是其它被提取的功能组件，各组件按需依赖
    - `component`则是根据业务被划分的组件
3. **为组件添加开关判断**
    - 组件在分开开发时是一个app，而在组合应用时是一个lib，因此需要判断
    - 如果开关设置在`gradle.properties`文件中，则在各组件的`build.gradle`文件中替换`apply plugin: 'com.android.application'`为
        ```java
        if (runAlone.toBoolean()) {
            apply plugin: 'com.android.application'
        } else {
            apply plugin: 'com.android.library'
        }
        ```
    - 如果开关在自建的`gradle`文件中，则替换为
        ```java
        def runAlone() {
            //需要根据单独为组件设置的名称替换
            return rootProject.ext.component['component1RunAlone ']
        }

        if (runAlone()) {
            apply plugin: 'com.android.application'
        } else {
            apply plugin: 'com.android.library'
        }
        ```
    - 在`app`中添加依赖
        ```java
        dependencies {
            //app只在统一编译时加入对组件的依赖
            if (!rootProject.ext.component['component1RunAlone']) {
                implementation project(path: ':component1')
            }
            if (!rootProject.ext.component['component2RunAlone']) {
                implementation project(path: ':component2')
            }
        ```
    - 其它：as当前的插件声明变成了
        ```java
        plugins {
            id 'com.android.application'
            id 'kotlin-android'
        }
        ```
        其实等价于
        ```java
        apply plugin: 'com.android.application'
        apply plugin: 'kotlin-android'
        ```
4. **解决`AndroidManifest`冲突**
    - 每个组件作为app开发时需要`Application`和`launchActivity`，而作为lib时这些会与`app`包的起冲突
    - 解决办法：组件单独开发时单独指定一个`AndroidManifest`文件
        1. 在`main`目录下新建`component`文件夹(目录和文件夹名应自行决定，这里只是举例)
        2. 将项目的`AndroidManifest`文件复制到`component`文件夹下
        3. 删除组件的原`AndroidManifest`文件中`application`的标签属性，只保留标签
        4. 删除组件的原`AndroidManifest`文件中的`Activity`的带有`Launcher`的`intent-filter`
        5. 在组件的`build.gradle`文件中指定`component`及其`AndroidManifest`文件，并删掉`applicationId`
            ```java
            android {
                defaultConfig {
                    ...
                    //删掉组件的applicationId
                    /*applicationId "..."*/
                    ...
                }
                sourceSets {
                    main {
                        //runAlone即开关判断
                        if (runAlone()) {
                            //指定manifest文件位置
                            manifest.srcFile 'src/main/component/AndroidManifest.xml'
                        } else {
                            manifest.srcFile 'src/main/AndroidManifest.xml'
                            //合成编译时排除component包下所有的内容
                            java {
                                exclude 'component/**'
                            }
                        }
                    }
                }
            }
            ```
    - 所有的组件都要执行这样的操作以避免冲突
5. 测试：当设置完成后更改开关并同步项目，as中对应的组件图标会在`module`样式和`lib`样式中切换
6. **为项目组件的单独开发增加`application`**
    - 整个项目最终打包时唯一的`applicaiton`时在app的`AndroidManifest`注册声明的，作为组件时是无法获取或者执行自己的初始化的，因此需要自己作为组件时的`applicaiton`来执行自己的操作
    - 解决办法
        1. 在`component`文件夹下新建`java`文件夹，并在`java`文件夹下新建单独开发时的`application`实现类
        2. 在单独开发时的`AndroidManifest`注册
        3. 在`build.gradle`文件中指定
            ```java
            android {
                sourceSets {
                    main {
                        if (runAlone()) {
                            manifest.srcFile 'src/main/component/AndroidManifest.xml'
                            //指定java文件夹
                            java.srcDirs = ['src/main/java', 'src/main/component/java']
                        } else {
                            manifest.srcFile 'src/main/AndroidManifest.xml'
                            //统一打包时排除
                            java {
                                exclude 'component/**'
                            }
                        }
                    }
                }
            }
            ```
    - 注意事项：
        - 作为单独开发时的`application`，其在最后打包时是被排除的，其中的代码也不会执行，因此写代码的时候，要么将代码写在`common`的`CommonApplicaiton`中，此`application`继承即会调用，要么复制代码到`app`的`application`中
        - 此方法同样适用于一些为单独开发指定的文件，但是注意，这些文件如果被排除则最终打包都不会被编译进包内
7. **组件间的调用和通信**
    - 这里使用的是`ARouter`
    - 官方文档：https://github.com/alibaba/ARouter/tree/master
    - 启用：
        1. 在`common`模块的依赖中添加
            ```java
            dependencies {
                api 'com.alibaba:arouter-api:1.5.1'
            }
            ```
            因为`common`模块被所有组件依赖，因此也给所有组件添加了`ARouter`依赖
        2. 给所有使用到的模块的`build.gradle`添加`ARouter`注解依赖
            ```java
            apply plugin: 'kotlin-kapt'
            kapt {
                arguments {
                    arg("AROUTER_MODULE_NAME", project.getName())
                }
            }
            dependencies {
                 kapt 'com.alibaba:arouter-compiler:1.5.1'
            }
            ```
        3. 在项目的`build.gradle`中顶行添加自动注册依赖
            ```java
            apply plugin: 'com.alibaba.arouter'
            buildscript {
                dependencies {
                    classpath "com.alibaba:arouter-register:1.0.2"
                }
            }
            ```
        4. 初始化：`ARouter.init(app)`
    - 使用1：跳转
        - 给需要跳转的`Activity`声明`@Route`注解
            ```kotlin
            //path是自定义路径，至少要两层且ARouter会根据每层的名称进行分组
            //ARouter允许一个module中存在多个分组，但是不允许多个module中存在相同的分组
            //@Route(path = "/test/main")
            //建议在common模块中对路径进行统一管理
            @Route(path = RouterHelper.Test.MAIN)
            class TestMainActivity : CommonActivity() 
            ```
        - 跳转:
            ```java
            //可以跨组件调用
            //更多用法见官方文档
            ARouter.getInstance().build("/test/activity").navigation();
            //建议进行统一封装
            RouterHelper.navigation(RouterHelper.Test.MAIN)
            ```
    - 使用2：组件通信
        1. 声明服务：在`common`中声明一个跨组件提供的服务，声明在`common`中是因为它被当作了路由中心，实际项目中如有必要也可以单独抽出一个模块作为路由中心
            ```kotlin
            interface MyProvider : IProvider {
                //自定义的方法
                fun getSome(flag:String): Int

                override fun init(context: Context?) {
                }
            }
            ```
        2. 在一个组件中实现该服务
            ```kotlin
            @Route(path = "/yourservicegroupname/hello", name = "测试服务")
            class MyProviderImpl : MyProvider {

                var a = 2
                
                @Override fun getSome(flag:Int): Int {
                    return a + flag
                }
            }
            ```
        3. 在另一处调用
            ```kotlin
            class Test {
                
                //这只是一种写法，更多写法见官方文档
                //ARouter的自动注入在kt中必须使用@JvmField使其编译后的java字段为public，否则无法写入
                @Autowired
                @JvmField
                var myProvider : MyProvider? = null;

                init{
                    //必须在调用之前调用此方法
                    ARouter.getInstance().inject(this);
                }

                test(){
                    //获取结果
                    myProvider.getSome(flag = 1)
                }
            }
            ```
    - 注意：
        - 在kapt中如果`build.gradle`中已经有`arguments`参数，则应该这样添加
            ```java
            kapt {
                arguments {
                    arg("room.schemaLocation", "$projectDir/schemas".toString())
                    arg("AROUTER_MODULE_NAME", project.getName())
                }
            }
            ```
        - 开发模式时应添加
            ```kotlin
            ARouter.openLog(); // 开启日志
            ARouter.openDebug(); // 使用InstantRun的时候，需要打开该开关，上线之后关闭，否则有安全风险
            ARouter.printStackTrace(); // 打印日志的时候打印线程堆栈
            ```
            特别是`openDebug()`来关闭缓存，并且应该在`ARouter.init(this)`之前
8. 注意事项
    - 依赖：`common`模块作为全局通用依赖，应该存放共有的业务逻辑，如`BaseApplication`，存放资源文件，所有模块都使用的第三方依赖，底层的基本业务逻辑等带有全局性的东西，除此之外的东西，应该放入自己的组件中，这也是组件化能够减少组件编译时间的原因之一
    - 注册：组件化开发需要两套`AndroidManifest.xml`，因此在其中编写代码时需要复制一份并注意其中的差别 
    - 初始化：如果某个模块根据业务需要在app里执行初始化任务，可以考虑根据`ARouter`声明初始化服务并在`app`的`application`中执行，也可以直接在`app`的`application`中直接强引用并初始化
    - 命名：因为是隔离开发，在最终合并时可能会出现资源文件名重复的冲突，因此建议图片资源放入`common` 文件夹中，建议在各组件的`build.gradle`文件中使用
        ```java
        android{
            //建议资源添加前缀
            resourcePrefix "component1_"
        }
        ```
        来让一些资源文件如`string.xml`、`color.xml`在创建时as提示使用前缀，以避开冲突
    - 在模块化中特别要注意会自动生成文件的库，比如`hilt`，如果在组件中使用了`hilt`，那么必须要让`app`可以访问需要依赖注入的类，因为最后编译时`app`是注入点