[app]

# Nombre visible de la app en el telefono
title = OCUPAMOR

# Nombre del paquete (sin espacios ni acentos)
package.name = ocupamor
package.domain = org.ocupamor

source.dir = .

# Extensiones que SI se empaquetan dentro del APK
source.include_exts = py,png,jpg,jpeg,gif,atlas,kv,json,txt,ttf,otf,wav,mp3,ogg

# Carpetas que se incluyen completas
source.include_patterns = assets/*,assets/*/*,assets/*/*/*,assets/*/*/*/*

# Cosas que NO deben entrar al APK
source.exclude_dirs = tests,bin,.buildozer,__pycache__,.git,venv,.venv
source.exclude_exts = spec
source.exclude_patterns = .env,*.zip

version = 1.0

# Requisitos unificados sin versiones fijas para p4a
requirements = python3,kivy,pillow,android,pyjnius,certifi

orientation = portrait
fullscreen = 0

# ---------------------------- Android ----------------------------
android.permissions = INTERNET

# API 33 y NDK 25b para compatibilidad en GitHub Actions
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Arquitectura unica para agilizar la ejecucion
android.archs = arm64-v8a

android.accept_sdk_license = True
android.allow_backup = True

# ---------------------------- iOS ---------------------------------
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

[buildozer]
log_level = 2
warn_on_root = 0
