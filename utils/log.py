import logging  # 日志模块
import datetime   # 时间模块
import os

# 设置日志存放路径
path = '.\\log\\'
if(not os.path.exists(path)):
    os.mkdir(path)

# 获取今天的日期
today_date = str(datetime.date.today())
# 创建logger记录器
logging.basicConfig(filename=path + today_date + '.log',level=logging.WARNING,filemode = 'a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test') # 用来分类
logger.setLevel(logging.WARNING)

# 创建一个控制台处理器，并将日志级别设置为debug

ch = logging.StreamHandler()

ch.setLevel(logging.WARNING)

# 创建formatter格式化器
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将formatter 添加到ch处理器
ch.setFormatter(formatter)

# 将ch添加到logger
logger.addHandler(ch)

# 清理上个月的日志
# def clean_log():
#     print('清理文件')
#     global path
#     global today_date
# 	# 遍历目录下的所有日志文件 i是文件名
# 	for i in os.listdir(path):       
#         file_path = path + i    # 生成日志文件的路径
		
# 		# 获取日志的年月，和今天的年月
# 	    today_m = int(today_date[5:7])   # 今天的月份
# 	    m = int(i[5:7])   # 日志的月份
# 	    today_y = int(today_date[0:4])   # 今天的年份
# 	    y = int(i[0:4])   # 日志的年份
	    
# 		# 对上个月的日志进行清理，即删除。
# 	    if(m < today_m):
# 	        if(os.path.exists(file_path)):   # 判断生成的路径对不对，防止报错
# 	            os.remove(file_path)   # 删除文件
# 	    elif(y < today_y):
# 	        if(os.path.exists(file_path)):
# 	            os.remove(file_path)

# if __name__ == '__main__':
#     clean_log()