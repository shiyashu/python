# SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
# 在使用SQLite前，我们先要搞清楚几个概念：
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
# 我们在Python交互式命令行实践一下：
# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)')
# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.execute('select * from user where id=?', '1')
# <sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
# 1
# 一次性获取一条数据
a = cursor.fetchone()
# 一次性获取所有数据
# a = cursor.fetchall()
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()