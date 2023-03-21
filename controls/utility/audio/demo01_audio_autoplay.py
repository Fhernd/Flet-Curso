import flet as flt
from flet import *


def main(page: Page):
    audio_mp3 = Audio(
        src='https://luan.xyz/files/audio/ambient_c_motion.mp3',
        autoplay=True,
    )

    page.overlay.append(audio_mp3)

    page.add(
        Text('this is an app with backgroun audio.'),
        ElevatedButton('Stop playing', on_click=lambda _: audio_mp3.pause()
                       ),
    )


if __name__ == '__main__':
    flt.app(target=main)
