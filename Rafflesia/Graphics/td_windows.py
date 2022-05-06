import glfw


def create_window(x, y, window_title, fullscreen, dev):
    try:
        if fullscreen:
            monitor = glfw.get_primary_monitor()
            vidmode = glfw.get_video_mode(monitor)
            window = glfw.create_window(vidmode.size.width, vidmode.size.height, window_title, monitor, None)
        else:
            window = glfw.create_window(x, y, window_title, None, None)
        if dev:
            print(f"Rafflesia Graphics / windows: {window_title} window 생성")

        return window

    except Exception as e:
        print(e)


def make_context_current(window, dev):
    try:
        if dev:
            print("Rafflesia Graphics / windows: make_content_current")
        glfw.make_context_current(window)
    except Exception as e:
        print(e)


def window_should_close(window, dev):
    try:
        return glfw.window_should_close(window)
    except Exception as e:
        print(e)


def swap_buffers(window, dev):
    try:
        glfw.swap_buffers(window)
    except Exception as e:
        print(e)


def poll_events(dev):
    try:
        glfw.poll_events()
    except Exception as e:
        print(e)


def terminate(dev):
    try:
        if dev:
            print("Rafflesia Graphics / windows: 윈도우 종료")

        glfw.terminate()
    except Exception as e:
        print(e)
