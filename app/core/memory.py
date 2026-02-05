# from collections import defaultdict, deque
#
# MAX_HISTORY = 6
# _sessions = defaultdict(lambda: deque(maxlen=MAX_HISTORY))
#
# def add_message(session_id: str, role: str, content: str):
#     _sessions[session_id].append({
#         "role": role,
#         "content": content
#     })
#
# def get_history(session_id: str):
#     return list(_sessions[session_id])

from collections import defaultdict, deque
from datetime import datetime

MAX_HISTORY = 6
_sessions = defaultdict(lambda: deque(maxlen=MAX_HISTORY))

def add_message(session_id: str, role: str, content: str):
    _sessions[session_id].append({
        "role": role,
        "content": content,
        "time": datetime.utcnow().isoformat()
    })

def get_history(session_id: str):
    return list(_sessions[session_id])
