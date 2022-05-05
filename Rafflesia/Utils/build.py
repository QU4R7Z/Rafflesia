import subprocess
import platform


def package(main, company_name, product_version, deploy_dir_name, withconsole, dev):
    try:
        system = platform.system()
        if dev:
            print(system)
        if system == 'Windows':
            if withconsole:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports " \
                          f"--windows-disable-console --enable-plugin=numpy --windows-company-name={company_name} " \
                          f"--windows-product-version={product_version} --output-dir={deploy_dir_name} {main}"
            else:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports " \
                          f"--enable-plugin=numpy --windows-company-name={company_name} " \
                          f"--windows-product-version={product_version} --output-dir={deploy_dir_name} {main}"
            if dev:
                print(command)
            subprocess.run(command.split(' '), shell=True)

        elif system == 'Linux':
            print(system)
        elif system == 'Darwin':
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)
