# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021 The MVT Project Authors.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

from .cache_files import CacheFiles
from .filesystem import Filesystem
from .net_netusage import Netusage
from .safari_favicon import SafariFavicon
from .version_history import IOSVersionHistory
from .webkit_indexeddb import WebkitIndexedDB
from .webkit_localstorage import WebkitLocalStorage
from .webkit_safariviewservice import WebkitSafariViewService

FS_MODULES = [CacheFiles, Filesystem, Netusage, SafariFavicon, IOSVersionHistory,
              WebkitIndexedDB, WebkitLocalStorage, WebkitSafariViewService,]
