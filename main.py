import json

import dbus
import web

urls = (
    '/.*', 'hooks'
)

app = web.application(urls, globals())
bus = dbus.SystemBus()

systemd = bus.get_object(
    'org.freedesktop.systemd1',
    '/org/freedesktop/systemd1'
)

manager = dbus.Interface(
    systemd,
    'org.freedesktop.systemd1.Manager'
)


class hooks:
    def POST(self):
        data = web.data()
        data = json.loads(data)

        action = web.ctx.env.get('X-GitHub-Event', None)
        repo_name = data['repository']['name']

        if action == 'push':
            manager.RestartUnit(f'{repo_name}.service', 'fail')


if __name__ == "__main__":
    app.run()
