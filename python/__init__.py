import samp
from pysamp import *
from pysamp.commands import cmd
from pysamp.timer import set_timer
from python.player import Player
from python import pycef
from python.pycef import *


samp.config(encoding='cp1251')


@on_gamemode_init
def on_gamemode_init():
    set_game_mode_text('I Love 664')
    add_player_class(0, -2623.6630, 1408.8757, 7.1015, 195.1507, -1, -1, -1, -1, -1, -1)
    show_player_markers(1)
    show_name_tags(True)
    set_name_tag_draw_distance(40)
    enable_stunt_bonus_for_all(False)
    disable_interior_enter_exits()
    set_weather(0)


@cmd
@Player.using_pool
def cef(player: Player):
    # player.send_client_message(-1, f'{pycef.player_has_plugin(player.id)}')
    pycef.create_browser(player.id, 123, "https://www.youtube.com/embed/78CcMEIOP2A?autoplay=1&controls=0", False, False)


@Player.on_connect
@Player.using_pool
def on_player_connect(player: Player):
    ...


@Player.on_disconnect
@Player.using_pool
def on_player_disconnect(player: Player, reason: int):
    Player.remove_from_pool(player)
