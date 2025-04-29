import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, filename='events.log'):
        self.filename = filename
        
    def log_event(self, event_type: str, metadata: dict):
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'type': event_type,
            'metadata': metadata
        }
        with open(self.filename, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    def audit_trail(self, address: str):
        with open(self.filename, 'r') as f:
            return [json.loads(line) for line in f if address in line]
