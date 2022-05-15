from Rafflesia import UtilsManager

u = UtilsManager(dev=True)
u.requirements_txt()
u.build("test.py", withconsole=False)
