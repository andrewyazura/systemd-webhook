import json
import web

try:
    import dbus

    bus = dbus.SystemBus()
    systemd = bus.get_object(
        'org.freedesktop.systemd1',
        '/org/freedesktop/systemd1'
    )
    manager = dbus.Interface(
        systemd,
        'org.freedesktop.systemd1.Manager'
    )
    debug_mode = False

except ModuleNotFoundError:
    debug_mode = True


urls = (
    '/github-webhook', 'hooks'
)

app = web.application(urls, globals())


class hooks:
    def POST(self):
        data = web.data()
        data = json.loads(data)

        action = web.ctx.env.get('X-GitHub-Event', None)
        repo_name = data['repository']['name']

        if action == 'push':
            if debug_mode:
                print(action, repo_name)
                return

            manager.RestartUnit(f'{repo_name}.service', 'fail')


if __name__ == "__main__":
    app.run()
