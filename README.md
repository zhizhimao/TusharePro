# TusharePro
Tushare金融大数据开放社区
https://tushare.pro/

安装
pip install tushare

版本升级
pip install tushare --upgrade

查看当前版本的方法：
import tushare as ts
print(ts.__version__)

设置token
ts.set_token('8438434b5690c99aae1dd2a1d8367e6606f4c98c105f9c4aa693d846')
以上方法只需要在第一次或者token失效后调用，完成调取tushare数据凭证的设置，正常情况下不需要重复设置。也可以忽略此步骤，直接用pro_api('your token')完成初始化
