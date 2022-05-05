from Rafflesia.Utils import build
from Rafflesia.Utils import requirements_txt


class UtilsManager:
    def __init__(self, dev=True):
        self.dev = dev
        super(UtilsManager, self).__init__()

    def build(self, main, company_name="QU4R7Z", product_version=1.0, dirname="Rafflesia-deploy", withconsole=True):
        build.build(main, company_name, product_version, dirname, withconsole, self.dev)

    def requirements_txt(self):
        requirements_txt.run(self.dev)
