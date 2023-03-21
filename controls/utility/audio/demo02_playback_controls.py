import flet as flt
from flet import *


url = 'https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true'


def main(page: Page):
    def volume_down(event):
        audio_mp3.volume -= 0.1
        audio_mp3.update()
    
    def volume_up(event):
        audio_mp3.volume += 0.1
        audio_mp3.update()
    
    def balance_left(event):
        audio_mp3.balance -= 0.1
        audio_mp3.update()
    
    def balance_right(event):
        audio_mp3.balance += 0.1
        audio_mp3.update()
    
    audio_mp3 = Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )

    page.overlay.append(audio_mp3)

    page.add(
        ElevatedButton('Play', on_click=lambda _: audio_mp3.play()),
        ElevatedButton('Pause', on_click=lambda _: audio_mp3.pause()),
        ElevatedButton('Resume', on_click=lambda _: audio_mp3.resume()),
        ElevatedButton('Release', on_click=lambda _: audio_mp3.release()),
        ElevatedButton("Seek 2s", on_click=lambda _: audio_mp3.seek(2000)),
        Row(
            [
                ElevatedButton("Volume down", on_click=volume_down),
                ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        Row(
            [
                ElevatedButton("Balance left", on_click=balance_left),
                ElevatedButton("Balance right", on_click=balance_right),
            ]
        ),
        ElevatedButton('Get duration', on_click=lambda _: print("Duration:", audio_mp3.get_duration())),
        ElevatedButton('Get position', on_click=lambda _: print("Current position:", audio_mp3.get_duration())),
    )


if __name__ == '__main__':
    flt.app(target=main)
