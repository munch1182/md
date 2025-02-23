# Android Compose

`Android Compose`是一个声明式的`Android UI`开发框架，用以简化并加快`Android`界面开发。

## 1. 什么是声明式

`Compose`的声明式与`React/Vue`、`Fultter`、`SwiftUI`等框架类似，采用可组合的函数描述`UI`和其结构，并使用数据来驱动`UI`，更改数据值即会自动同步更改`UI`。
与之相对应的，是`Android`传统的命令式`UI`开发方式，其采用`XML`或者`Java/Kotlin`语法来构建`UI`和其结构，并在获取到`UI`控件后，调用其方法进行`UI`更改。

`xml`写法：

```XML
<LinearLayout
    orientation="vertical">
    <TextView
        android:id="@+id/textView"
        android:text="Hello World!" />
    <Button
        android:id="@+id/button"
        android:text="Change Text" />
</LinearLayout>
```

```java
val button = findViewById<Button>(R.id.button)
val textView = findViewById<TextView>(R.id.textView)

button.setOnClickListener {
    // 调用该TextView控件的setText方法，更改其文本内容
    // 触发view的invalidate方法，重新绘制UI
    textView.text = "Hello Compose!"
}
```

或者

```java
val textview = TextView(this).apply { text = "Hello World" }
val button = Button(this).apply { text = "Change Text" }
val ll = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }

ll.addView(textview)
ll.addView(button)

button.setOnClickListener {
    textview.text = "Hello Compose"
}
```

`compose`写法：

```java
@Composable
fun Greeting() {
    var str by remember { mutableStateOf("hello world") }
    Column {
        Text(str)
        Button(
            // 更改text值，Compose会自动同步更改所有显示该值的UI显示
            // text值的变化会自动触发Compose的重组, 以更改UI显示
            onClick = { str = "hello compose" }) {
            Text("Change Text")
        }
    }
}
```

对比下写法上的区别：

1. `Compose`是采用组合的方式来显示`UI`，而`View`是采用继承的方式来显示`UI`。如`Button`在`View`中是对`TextView`的功能拓展，其继承自`TextView`，所以自身是一个单独的控件，可以直接设置显示的文字。而在`Compose`中`Button`只实现了名为`Button`（按压效果、点击回调等）的功能，不包括其内的显示，所以还需要再组合`Text`来实现文字显示。
   _组合与继承的优劣并不在于其本身，而是要与绘制方法相关联。_
2. `Compose`的`UI`更改是通过更改数据来实现的，而`View`的`UI`更改是通过调用控件的方法来实现的。所以`View`的`UI`更改需要先获取到控件对象，再调用其方法。而`Compose`的`UI`更改只需要更改数据，不需要也不能获取到对应的控件对象，对数据的更改会被`Compose`自动同步到所有显示该值的`UI`上。

## 2. 为什么要用`Compose`

`Compose`并不是对`View`的语法糖或者写法简化，而是对`View`的替代。`Compose`的`UI`基本上并不依赖`View`，而是直接在`Canvas`上绘制。
而之所以要使用`Compose`，主要有三个原因：

1. 引入数据驱动思想。这种思想已经在其他语言中被广泛验证与运用，已被证实其高效简洁。
2. 提升效率。不依赖`XML`声明`UI`即减少了界面布局的解析时间，`Compose`新的测量方式也解决了`View`的测量时间会随着层级增加而指数级增加的问题。
3. 摆脱历史包袱。直观来说，`android.view.View`是所有`View`的父类，而其现在有 3W+ 行代码。

## 3. `Compose`的写法结构

完善前面的例子：

```java
class MainActivity : ComponentActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // 不再需要setContentView函数设置UI界面
        // setContentView(..)
        setContent {
            Greeting("Android")
        }

    }

    @Composable
    fun Greeting() {
        var str by remember { mutableStateOf("hello world") }
        Column {
            Text(str)
            Button(
                // 更改text值，Compose会自动同步更改所有显示该值的UI显示
                // text值的变化会自动触发Compose的重组, 以更改UI显示
                onClick = { str = "hello compose" }) {
                Text("Change Text")
            }
        }
    }
}
```
