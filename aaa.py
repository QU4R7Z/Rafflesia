from Rafflesia import UtilsManager

u = UtilsManager()
u.requirements_txt()
u.build("test.py", withconsole=True)
