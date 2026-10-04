[app]
<<<<<<< HEAD
title = Mini Engine Step 1
package.name = miniengine1
package.domain = org.mizan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
=======
title = MI System SuperPower
package.name = misystem
package.domain = com.mi.superpower
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,html
version = 3.0.0

requirements = python3==3.11.0,kivy,flask,requests,urllib3,jinja2,markupsafe,itsdangerous,click,workzeug

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE

[buildozer]
log_level = 2
warn_on_root = 1
>>>>>>> f84fdfb3ac60f5c64261c72131c9791ed71b9076
