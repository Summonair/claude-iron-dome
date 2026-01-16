#!/usr/bin/env python3
import json
import sys
import re

def main():
    try:
        data = json.load(sys.stdin)
        
        tool_input = data.get('tool_input', {})
        cmd = tool_input.get('command', '')

        patterns = [
            r'rm\s+-rf',
            r'sudo',
            r'terraform\s+destroy',
            r'cdk\s+(destroy|synth)',
            r'git\s+push\s+--force',
            r'git\s+reset\s+--hard',
            r'kubectl\s+delete',
            r'docker\s+(system\s+prune|rmi|stop|kill)',
            r'aws\s+s3\s+rb',
            r'gcloud\s+projects\s+delete',
            r'mkfs',
            r'dd\s+if=',
            r'chmod\s+-R\s+777',
            r'chown\s+-R',
            r'gh\s+repo\s+delete',
            r'npm\s+publish'
        ]

        for pattern in patterns:
            if re.search(pattern, cmd):
                print(f"Iron Dome Intercepted: Dangerous command pattern detected: '{pattern}'", file=sys.stderr)
                sys.exit(1)

        sys.exit(0)

    except Exception as e:
        print(f"Iron Dome Error: {e}", file=sys.stderr)
        sys.exit(0) 

if __name__ == "__main__":
    main()
