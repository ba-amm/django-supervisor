
import time

from watchdog.events import PatternMatchingEventHandler

class ThrottledModifiedHandler(PatternMatchingEventHandler):
    """
    A pattern matching event handler that calls the provided
    callback when a file is modified.
    """
    def __init__(self, *args, **kwargs):
        self.event_count = 0
        super(ThrottledModifiedHandler, self).__init__(*args, **kwargs)

    def on_modified(self, event):
        super(ThrottledModifiedHandler, self).on_modified(event)
        if not event.is_directory:
            self.event_count += 1

    def reset_counter(self):
        self.event_count = 0
