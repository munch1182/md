# VSCODE配置 

- 可以基本满足多语言开发，适合入门学习、简单开发和查看代码

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [win下一些默认快捷键](#win下一些默认快捷键)
- [Markdown](#markdown)

<!-- /code_chunk_output -->

## win下一些默认快捷键 

- 折叠全部：`ctrl+k, ctrl+0`
- 展开全部：`ctrl+k, ctrl+j`
- 复制当前行到下一行：`ctrl c + v`
- 格式化：`shoft+alt+f`     //需要安装当前文件类型formatter插件

- 快捷键表：`ctrl+k, ctrl+s`
- 打开设置：`ctrl+,`
- 打开终端：```ctrl+` ```
- 打开插件：`ctrl+shift+x`
- 工作目录：`ctrl+shift+e`

>>>

## Markdown 

- 插件：Markdown Preview Enhanced
    - 支持代码块运行
        - 需要电脑环境支持，且代码被电脑执行，在开放环境下是不安全的
        - 需要手动开启设置 Markdown-preview-enhanced:Enable Script Execution
        - 需要指定语言并添加`{cmd=true}`或者指定环境`{cmd=指定路径}`：
        - 添加`hide`即`{cmd=true hide}`则可以省略代码直接显示结果
        ```java {.line-numbers,highlight=[1-2]} //.line-numbers添加代码行数,highlight=[1-2]指定行添加高亮
        public static void main(String[] args){
            System.out.print(-9 % 4);
        }
        ```
        ```kotlin
        fun main(args:Array<String>){
            System.out.print(-9 % 4)
        }
        ```
        ```python {cmd=true}
        if __name__ == '__main__':
            print('%d%%%d=%d,%d%%%d=%d' % (-9, 4, -9 % 4, 9, -4, 9 % -4))
        ```
    - 画图
        ```mermaid
        graph LR
        A(下载) --> B[安装]
        B --> C{界面是否顺心}
        C --> | 顺心 | D[试用]
        C --> |不顺心| E[卸载]
        E --> F{寻找下一个}
        D --> G{好不好用}
        G -->  |好用| H[使用]
        G -->  |不好用| E
        H --> I{长期使用顺不顺心}
        I --> |顺心| H
        I --> |不顺心| E
        F --> |找不到| J(自己开发)
        F --> |找到| A
        ```

        ```flow
        startID=>start: 开始框
        inputoutputID=>inputoutput: 输入输出框
        operationID=>operation: 操作框
        conditionID=>condition: 条件框
        subroutineID=>subroutine: 子流程
        endID=>end: 结束框

        startID->inputoutputID->operationID->conditionID
        conditionID(no)->subroutineID
        conditionID(yes)->endID
        ```
        
    - 自带生成目录，需要书写时有结构
        ```
        <!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->
        ```
        也可以直接使用`[TOC]`
    - 导出
        - 导出pdf效果最好的仍然是`Chrome`，因为其保留了代码块效果
        - pandoc可以转换多种格式，但是在没有模板的情况下效果并不好
    - 参考
        - [在 VSCode 下用 Markdown Preview Enhanced 愉快地写文档](https://zhuanlan.zhihu.com/p/56699805)
        - [vscode markdown preview enhance 插件 pdf 导出](https://blog.csdn.net/m0_37639589/article/details/91349425)

- 一些markdown语法:
    - 上标 2^3^=8 `2^3^=8`
    - 注脚 注脚会被自动移到文章末尾[^1]
    [^1]: 注脚会被自动移到文章末尾
    - 删除线 ~~123~~ `~~123~~`
    - 下缩 ~456~ `~456~`
    - 表格  
            
        | item1 | item2 | item3 | item4 |
        | :---: | :--- | ---: | --- |
        | item1item1 | item2 | item3item3 | item4 |
        | item1 | item2item2 | item3 | item4item4 |
