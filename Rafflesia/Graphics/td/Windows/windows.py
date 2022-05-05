import glfw
from OpenGL.GL import *


def create_window(x, y, window_title, fullscreen, drawer, dev):
    try:
        if fullscreen:
            monitor = glfw.get_primary_monitor()
            vidmode = glfw.get_video_mode(monitor)
            window = glfw.create_window(vidmode.size.width, vidmode.size.height, window_title, monitor, None)
        else:
            window = glfw.create_window(x, y, window_title, None, None)
        if dev:
            print(f"{window_title} window 생성")

        if not window:
            glfw.terminate()

        glfw.make_context_current(window)

        while not glfw.window_should_close(window):
            glfw.poll_events()
            for i in drawer:
                glDrawArrays(i)
            glfw.swap_buffers(window)

        glfw.terminate()
        if dev:
            print(f"{window_title} window 종료")

    except Exception as e:
        print(e)
