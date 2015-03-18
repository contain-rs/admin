#!/usr/bin/env python3

import toml
import sys

def err(msg, *args):
    print('error:', msg % args, file = sys.stderr)

def enforce_key_not_in_configs(dict, key, type, action):
    if key in dict:
        err('%s %s should not %s in configs.toml',
            type, key, action)
        sys.exit(1)

def main():
    secrets = toml.load('secrets.toml')

    configs = toml.load('configs.toml')

    for setting in ['github', 'web']:
        enforce_key_not_in_configs(configs, setting,
                                   'setting', 'exist')
        configs[setting] = secrets[setting]

    for name in configs['repo']:
        d = configs['repo'][name]
        # set the default names
        if 'owner' not in d:
            d['owner'] = 'contain-rs'
        if 'name' not in d:
            d['name'] = name
        # set the per-repo secrets.
        for (service, settings) in secrets['per-repo'].items():
            enforce_key_not_in_configs(d, service,
                                       'service',
                                       'be registered for repository %s' % name)
            d[service] = settings

    print(toml.dumps(configs))

if __name__ == '__main__':
    main()
