from pysamp import call_native_function, register_callback, on_gamemode_init
from python.player import Player


def create_browser(player_id, browser_id, url, hidden=False, focused=True):
    return call_native_function('cef_create_browser', player_id, browser_id, url, hidden, focused)


def player_has_plugin(player_id):
    return call_native_function('cef_player_has_plugin', player_id)


@on_gamemode_init
def on_ready():
    register_callback('OnCefInitialize', 'ii')


@Player.on_connect
@Player.using_pool
def on_player_connect(player: Player):
    call_native_function('cef_on_player_connect', player.id, player.get_ip())


@Player.on_spawn
@Player.using_pool
def on_player_spawn(player: Player):
    create_browser(player.id, 1, 'https://tms-server.com/', False, False)
    return False


def OnCefInitialize(player_id, success):
    print(f'OnCefInitialize({player_id=}, {success=})')

    if success:
        create_browser(player_id, 1, 'https://tms-server.com/', False, False)

    else:
        player_has_plugin(player_id)