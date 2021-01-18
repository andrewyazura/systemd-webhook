import json

import pydbus
import web

urls = (
    '/.*', 'hooks'
)

app = web.application(urls, globals())

system_bus = pydbus.SystemBus()
systemd = system_bus.get('.systemd1')


class hooks:
    def POST(self):
        data = web.data()
        data = json.loads(data)

        action = data.get('action', None)
        repo_name = data['repository']['name']

        if not action or action == 'push':
            systemd.RestartUnit(f'{repo_name}.service', 'fail')


if __name__ == "__main__":
    app.run()
