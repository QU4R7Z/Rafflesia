import glfw


def create_window(x, y, window_title, dev):
    try:
        window = glfw.create_window(x, y, window_title, None, None)
        if dev:
            print(f"{window_title} window 생성")

        if not window:
            glfw.terminate()

        glfw.make_context_current(window)

        while not glfw.window_should_close(window):
            glfw.poll_events()
            glfw.swap_buffers(window)

        glfw.terminate()
        if dev:
            print(f"{window_title} window 종료")

    except Exception as e:
        print(e)
