from pysamp import (
    call_native_function,
    register_callback
)


class Browser:
    def __init__(
            self,
            player_id: int,
            browser_id: int,
            url: str,
            is_hidden: bool,
            is_focused: bool
    ) -> None:
        self.player_id: int = player_id
        self.browser_id: int = browser_id
        self.url: str = url
        self.is_hidden: bool = is_hidden
        self.is_focused: bool = is_focused

        call_native_function(
            'cef_create_browser',
            self.player_id,
            self.browser_id,
            self.url,
            self.is_hidden,
            self.is_focused
        )

    @classmethod
    def create(
        cls, player_id: int,
        browser_id: int,
        url: str,
        is_hidden: bool = False,
        is_focused: bool = False
    ):
        return cls(
            player_id,
            browser_id,
            url,
            is_hidden,
            is_focused
        )

    def destroy(self):
        return call_native_function(
            'cef_destroy_browser',
            self.player_id,
            self.browser_id
        )

    def hide(self, is_hidden: bool):
        self.is_hidden = is_hidden

        return call_native_function(
            'cef_hide_browser',
            self.player_id,
            self.browser_id,
            self.is_hidden
        )

    def emit_event(self, event_name: str, *args):
        return call_native_function(
            'cef_emit_event',
            self.player_id,
            event_name,
            *args
        )

    def subscribe_event(self, event_name: str, callback):
        return call_native_function(
            'cef_subscribe',
            event_name,
            callback
        )

    def focus(self, is_focused: bool):
        self.is_focused = is_focused

        return call_native_function(
            'cef_focus_browser',
            self.player_id,
            self.browser_id,
            self.is_focused
        )

    def load_url(self, url: str):
        self.url = url

        return call_native_function(
            'cef_load_url',
            self.player_id,
            self.browser_id,
            self.url
        )


def OnCefInitialize(player_id: int, status: int):
    print('[CEF] Initialize...')

    if status:
        print('[CEF] Successful Initialize.')
        browser = Browser.create(
            player_id=player_id,
            browser_id=1,
            url='http://localhost/',
            is_focused=True
        )
        browser.subscribe_event('login:submit', 'login_event')

    else:
        print(f'[CEF] Failed initialize. (player_id: {player_id})')


def cef_register_callbacks(callbacks: list[str] = []):
    register_callback('OnCefInitialize', 'ii')

    for callback in callbacks:
        register_callback(*callback)


def cef_on_player_connect(player_id: int, player_ip: str):
    call_native_function('cef_on_player_connect', player_id, player_ip)
