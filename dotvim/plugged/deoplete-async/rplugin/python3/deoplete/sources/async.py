from .base import Base

import re
RT_PATTERN = r'RT:?\w*$'
RX_RT = re.compile(RT_PATTERN, re.IGNORECASE)


def log(msg):
    with open('/tmp/async.log', 'a') as file_:
        file_.write('%s\n' % msg)


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.debug_enabled = True
        self.name = 'request_tracker'
        self.mark = '[RT]'

        self.is_volatile = True
        self.matchers = []
        self.sorters = []

        self.max_menu_width = 120
        self.max_abbr_width = 120
        self.input_pattern = RT_PATTERN

        self._cached_input = None
        self._counter = 10

    def get_complete_position(self, context):
        match = RX_RT.search(context['input'])
        return match.start() if match else -1

    def gather_candidates(self, context):
        if context['input'] != self._cached_input:
            log('RESET INPUT')
            self._cached_input = context['input']
            self._counter = 10

        if self._counter == 0:
            log('RESULT READY')
            context['is_async'] = False
            return ['RTfirst', 'RTsecond', 'RTthird']

        self._counter -= 1
        log('RESULT IS NOT READY: counter %s' % self._counter)
        context['is_async'] = True
        return []
