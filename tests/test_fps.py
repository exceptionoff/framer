
import pytest


import frame_functions


@pytest.mark.what_fps
@pytest.mark.parametrize("n_frames", [10, 50, 100])
class TestFps:


    def test_n_frames_pyautogui_screenshot(self, tmp_dir, n_frames):
        for i in range(n_frames):
            frame_functions.screenshot(f'{tmp_dir}/pyautogui{n_frames}frame{i}.png')

    def test_n_frames_mss_mss_shot(self, tmp_dir, n_frames):
        sct = frame_functions.mss()
        for i in range(n_frames):
            sct.shot(output=f'{tmp_dir}/mss{n_frames}frame{i}.png')

    def test_n_frames_grab_screen_shot(self, tmp_dir, n_frames):
        for i in range(n_frames):
            frame_functions.grab_screen(output=f'{tmp_dir}/grab_screen{n_frames}frame{i}.png')