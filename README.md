# -基于Python Opencv4的装甲板识别 基于视觉与串口通信的自动瞄准
作者：11 巩布g7人 张智行

1.本视觉代码可在树莓派Linux系统和Windows系统上运行<br>

2.Linux系统：在树莓派中刷入官方镜像，打开其中的Thonny Python IDE，将工程文件上传至IDE上，安装python-opencv: pip install opencv-python，安装numpy: pip install numpy，安装serial：pip install pyserial,安装后接入摄像头即可在树莓派上运行程序

3.Windows系统：*编译器介绍：PyCharm是一种Python IDE（Integrated Development Environment，集成开发环境），带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、项目管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发<br>
               *安装方式:https//www.jetbrains.com/pycharm/download/ 单击官网首页右侧Community下的Download按钮，即可下载免费社区版<br>
               *安装python-opencv、numpy、serial模块即可运行程序

4.视觉原理说明：https://github.com/Curry50/Vision/blob/4387468009c31854a03fa33305ea33f53d5242fd/%E8%A7%86%E8%A7%89%E5%8E%9F%E7%90%86%E8%AF%B4%E6%98%8E.docx

5.通信原理补充：除了视觉原理说明文档中的四个模块外，为了将打击点坐标信息传递给stm32主控板，新增了SerialCommunication模块。该模块主要是对视觉得到的坐标信息进行数据处理，转换成16进制字符串，便于stm32主控板读取坐标信息
