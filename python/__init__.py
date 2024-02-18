import samp
from pysamp import *
from python import cef
from python.cef import *
from python.player import Player


samp.config(encoding='cp1251')


@on_gamemode_init
def on_gamemode_init():
    set_game_mode_text('PyCEF Demo')
    cef_register_callbacks([
        ['login_event', 'is']
    ])


@Player.on_connect
@Player.using_pool
def on_player_connect(player: Player):
    cef_on_player_connect(
        player_id=player.get_id(),
        player_ip=player.get_ip()
    )


def login_event(player_id: int, args: str):
    login, password = args.split()
    player: Player = Player.from_pool(player_id)
    player.send_client_message(-1, f'[Auth] Login: {login}, Password: {password}')


@Player.on_disconnect
@Player.using_pool
def on_player_disconnect(player: Player, reason: int):
    Player.remove_from_pool(player)
