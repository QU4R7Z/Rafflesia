import subprocess
import platform
import time


def package(main, company_name, product_version, deploy_dir_name, ico, withconsole, dev):
    try:
        system = platform.system()
        if dev:
            print(system)
        if system == 'Windows':
            if withconsole:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports --windows-icon-from-ico={ico} " \
                          f"--windows-company-name={company_name} --windows-product-version={product_version} " \
                          f"--output-dir={deploy_dir_name} " \
                          f"--include-module=OpenGL.platform " \
                          f"--include-module=OpenGL.arrays " \
                          f"{main}"
            else:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports --windows-disable-console " \
                          f"--windows-company-name={company_name} --windows-product-version={product_version} " \
                          f"--windows-icon-from-ico={ico} --output-dir={deploy_dir_name} " \
                          f"--include-module=OpenGL.platform " \
                          f"--include-module=OpenGL.arrays " \
                          f"{main}"
            if dev:
                print(command)

            start = time.time()
            subprocess.run(command.split(' '), shell=True)
            end = time.time()
            if dev:
                print(f"{end-start}s 사용됨")

        elif system == 'Linux':
            print(system)
        elif system == 'Darwin':
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)
