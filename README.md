# fastapi

## 预处理
- [安装虚拟环境](https://gitee.com/mathchan/zvision-work/blob/master/2020-11/python.md)
- install 模块使用类似于js中 package.json这种类型的配置文件

```shell
# 启动虚拟环境
# 在安装包的时候 使用如下 形式安装
pip install fastapi[all] 
pip freeze > requirements.txt
# 当 clone一个项目的时候 只需安装 配置文件中的包
pip install -r requirements.txt
```

- 运行
```shell
uvicorn main:app --reload
# 退出
ctrl+C
```
