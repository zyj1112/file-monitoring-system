# 为大创项目chickenglass写的一个文件状态监视系统
***
## 内容介绍
watching.py是一个文件状态监视的程序，主要是把文件变化的日志打印出来

watching_refreshing.py是一个文件状态监视（把文件变化的日志打印出来）+文件变化时刷新浏览器的程序
***
## 主要功能
老师的[HackMD博客](https://hackmd.io/LoFPSapEQhWjBfCFVfytVQ)中对文件状态监视描述是：

文件状态监视（可以用livereload）：
* 输入文件监视+meta rebuild：有改变就跑build系统。build系统并且会更新新的meta data。
* 输出文件监视+live preview：输出改变之后自动刷新浏览器live preview。自己写一大堆东西再手动刷新的世界告一段落。（可以用livereloadx）

从我的角度来看，我需要完成的工作主要是以下两个：
* 监视html文件是否发生改变：在使用编辑模式时我们直接改变html文件，而我们需要设计程序监视html文件的改变
* html文件改变后，刷新浏览器：这样我们就不需要手动刷新浏览器了，~~虽然我觉得手动刷新也不是很麻烦（bushi）~~
