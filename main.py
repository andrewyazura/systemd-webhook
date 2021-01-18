import json
import os
import web

urls = (
    '/.*', 'hooks'
)

app = web.application(urls, globals())


class hooks:
    def POST(self):
        data = web.data()
        data = json.loads(data)

        action = data.get('action', None)
        repo_name = data['repository']['name']

        if not action or action == 'push':
            os.system(f'sudo systemctl restart {repo_name}.service')


if __name__ == "__main__":
    app.run()
