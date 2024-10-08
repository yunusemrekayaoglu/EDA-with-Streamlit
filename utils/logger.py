# utils/logger.py

import datetime
import os
import pandas as pd

class OperationLogger:
    def __init__(self, log_file='utils/operation_logs.csv'):
        self.log_file = log_file
        self.logs = []
        self.ensure_log_file_exists()

    def ensure_log_file_exists(self):
        if not os.path.isfile(self.log_file):
            df = pd.DataFrame(columns=['Timestamp', 'User', 'Operation', 'Columns'])
            df.to_csv(self.log_file, index=False)

    def log_operation(self, user, operation, columns=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        columns_str = ', '.join(columns) if columns else 'N/A'
        self.logs.append((timestamp, user, operation, columns_str))
        self.append_logs_to_csv()

    def append_logs_to_csv(self):
        df = pd.DataFrame(self.logs, columns=['Timestamp', 'User', 'Operation', 'Columns'])
        df.to_csv(self.log_file, mode='a', header=False, index=False)
        self.logs = []

    def show_logs(self):
        if os.path.isfile(self.log_file):
            df = pd.read_csv(self.log_file)
            return df.to_records(index=False).tolist()
        return []
