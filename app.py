# -*- coding:UTF-8 -*-
from apps import creat_app
from flask_migrate import MigrateCommand
from flask_script import Manager
#必须导入，即使不使用
from apps.model.appinfo_maint import App_Info

app = creat_app()

#使用flask-script里面的manager进行命令得到管理和使用
manager = Manager(app=app)

#向manager中添加命令
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
