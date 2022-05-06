import os

from Rafflesia.Utils import build
from Rafflesia.Utils import requirements_txt


class UtilsManager:
    def __init__(self, dev=True):
        self.dev = dev
        super(UtilsManager, self).__init__()

    def build(self, main, company_name="QU4R7Z", product_version=1.0, dirname="Rafflesia-deploy",
              ico=os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources/rafflesia.ico"),
              withconsole=True):
        build.package(main, company_name, product_version, dirname, ico, withconsole, self.dev)

    def requirements_txt(self):
        requirements_txt.run(self.dev)
