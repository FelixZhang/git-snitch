#!/usr/bin/env python3

import yaml
import os

def load(file):
    with open (file, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def cache_dir(cfg):
    return cfg.get('cache_dir')

def repos(cfg):
    cache_d = cache_dir(cfg)
    #cache_d = '/home/fezhang/bin/config/snitched'
    if os.access(cache_d, os.F_OK):
        return next(os.walk(cache_d))[1]
    else:
        return None

def default_keywords_regex(cfg):
    return cfg.get('defaults').get('keywords')['regex']

def default_keywords_word(cfg):
    return cfg.get('defaults').get('keywords')['word']

def default_mail_suffix(cfg):
    return cfg.get('defaults').get('mail_suffix')

def users(cfg):
    return cfg.get('users')

