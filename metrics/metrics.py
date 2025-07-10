import psutil
import json
from datetime import datetime

def get_metrics():
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent
    }
    return json.dumps(data)

if __name__ == "__main__":
    print(get_metrics())

