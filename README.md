# MasterProject
#8mainwindow:1，打算采用5个QTableWidget,通过QStackedLayout来实现显示,2，数据结构定位pd.DataFrame,3，通过“自定义信号的发射”来实现“读取cfg文件后的数据显示”；
#9mainwindow:在8的基础上修改了：用QLineEdit()作为数据输入，而不是QTableWidgetItem()；显示的时候输入框自动延伸到右边界处；使用一个Button来commit另一个button来 reset。（意外地完成了修改数据，原因是Python中b=a;对b的内容修改也会对a造成影响）
#10mainwindow:数据成功地保存到文件。解决了1，写入不该写入的行；2，COMPARTMENT_SETUP一定要在最前面，然后轮到COMP；3，层数的表达转换；往后修改要注意的点是：1,load了数据之后，None可能变成字符串也可能还是None；2，如果初始化时pd.Series(None,dtype='str')那么在QLineEdit那里键入了东西并且保存了，即使以后将输入框清空也使None变成空字符串（数据类型质变）。后面我直接抛弃None而初始化为空字符串；
#11mainwinodw:增加了VE,DE,HF,BD的显示。
#12mainwindow：增加了matplotlib的画布和工具栏
#13mainwindow:将closeProject函数从SurreyWindow处移动到ProjectViwer处
#14mainwindow:相比13mainwindow，修改中文注释为英文
