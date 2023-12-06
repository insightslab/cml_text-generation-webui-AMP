import mitmproxy
from modules import shared
class ConditionalRerouter:
    def request(self, flow):
        flow.request.host = 'localhost'
        if flow.request.path.startswith('/api'):
            flow.request.port = shared.args.api_blocking_port
        else:
            flow.request.port = shared.args.listen_port

addons = [ConditionalRerouter()]