# MasterProject
相比cheshi_v1：cheshi_v2多了QFileDialog的设置；
相比run_v1:run_v2需要传递一个cfg文件的路径，又需要一个结果保存的路径
cheshi_v3相比cheshi_v2少了选择结果保存路径一步
cheshi_v4相比cheshi_v3完善了Compartment Setup功能，并且删除了“用DockWidget显示”的五组参数
cheshi_v5重要更改：新建工程不需要选择文件夹！而是建立一个QTreeWidgetItem的显示而已，数据的保存放在ProjectItem类的saveProject方法中。

