# MasterProject
# Requirement:
   - python interpreter installed;
   - third-party PyQt5 package installed;
   - third-party Pandas package installed;

# User Guide:
   1. downloading these two folder 'core' and 'example';
   2. running the '16mainwindow' file of the 'example' folder.
   
   Alternatively, configuration can be done as below:
   1. downloading these three files '16mainwindow', 'saveMass_hobin' and 'compDPK_hobin'; 
   2. placing the 'saveMass_hobin' and 'compDPK_hobin' files in your 'core' folder; 
   3. plcaing the '16mainwindow' file in you 'example' folder;
   
# GUI Programming Guide:

   Basically, there are two ways to display your widgets. 
   - The first one is the automatic layout management by [Qt's layout engine](https://doc.qt.io/qt-5/layout.html). For instance , you can use these classes, such as QGridLayout, QHBoxLayout, QVBoxLayout, to arrange your widgets. These class will do some calculations automatically, such as the position and the size of widgets. When using the layout engine, you need to pay attention to the QSizePolicy, minimumSize and maximumSize of [QWidget](https://doc.qt.io/qt-5/qwidget.html). Actually, these attributes are used by the layout engine when resizing happens.
   - The second one is the manaul layout management. For instance, you need to provide a way to calculate the position and the size of widgets. If you want to place some widgets inside a specific widget, what you need to do is make this specific widget become the parent of these widget. To show up widgets, you just need to call the show() function of the specific widget. Keep in mind, if a widget becomes visible, its child widgets will become visible by default. 

