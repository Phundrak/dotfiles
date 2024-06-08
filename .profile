#!/bin/sh
# shellcheck source=/dev/null
. "$HOME"/.profile.private

export EMAIL=lucien@phundrak.com
export NAME="Lucien Cartier-Tilet"

export XDG_CACHE_HOME="$HOME"/.cache
export XDG_CONFIG_HOME="$HOME"/.config
export XDG_DATA_HOME="$HOME"/.local/share
export XDG_STATE_HOME="$HOME"/.local/state

SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
export SSH_AUTH_SOCK
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH":/usr/local/lib
export LSP_USE_PLISTS=true
export DIFFPROG=ediff
export SUDO_ASKPASS="$HOME"/.local/bin/askpass
export MANPAGER=less

export DART_SDK=/opt/dart-sdk/bin
export ANDROID_HOME="$HOME"/Android/Sdk
export CHROME_EXECUTABLE=/usr/bin/chromium

LESS_TERMCAP_mb=$(printf '\e[1;32m')
export LESS_TERMCAP_mb
LESS_TERMCAP_md=$(printf '\e[1;32m')
export LESS_TERMCAP_md
LESS_TERMCAP_me=$(printf '\e[0m')
export LESS_TERMCAP_me
LESS_TERMCAP_se=$(printf '\e[0m')
export LESS_TERMCAP_se
LESS_TERMCAP_so=$(printf '\e[01;33m')
export LESS_TERMCAP_so
LESS_TERMCAP_ue=$(printf '\e[0m')
export LESS_TERMCAP_ue
LESS_TERMCAP_us=$(printf '\e[1;4;31m')
export LESS_TERMCAP_us

export BROWSER=firefox

export EDITOR="emacsclient -c"
export VISUAL="emacsclient -c"

export GTK_THEME=Nordic
export GTK_ICON_THEME="Flat-Remix-Dark"

export __GL_SHADER_DISK_CACHE_PATH="$XDG_CACHE_HOME"/nv
export _JAVA_OPTIONS="-Djava.util.prefs.userRoot=${XDG_CONFIG_HOME}/java -Djavafx.cachedir=${XDG_CACHE_HOME}/openjfx"
export _Z_DATA="$XDG_DATA_HOME"/z
export BUNDLE_USER_CACHE="$XDG_CACHE_HOME"/bundle
export BUNDLE_USER_CONFIG="$XDG_CONFIG_HOME"/bundle
export BUNDLE_USER_PLUGIN="$XDG_DATA_HOME"/bundle
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export CUDA_CACHE_PATH="$XDG_CACHE_HOME"/nv
export DENO_DIR="$HOME"/.config/deno
export DENO_INSTALL_ROOT="$HOME"/.local/bin/deno
export DOCKER_CONFIG="$XDG_CONFIG_HOME"/docker
export GEM_HOME="$XDG_DATA_HOME"/gem
export GEM_SPEC_CACHE="$XDG_CACHE_HOME"/gem
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export GOPATH="$XDG_DATA_HOME"/go
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export HISTFILE="$XDG_STATE_HOME/bash/history"
export ICEAUTHORITY="$XDG_CACHE_HOME"/ICEauthority
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export MBSYNCRC="$XDG_CONFIG_HOME"/isync/mbsyncrc
export MPLAYER_HOME="$XDG_CONFIG_HOME"/mplayer
export MYPY_CACHE_DIR="$XDG_CACHE_HOME"/mypy
export NPM_CONFIG_USERCONFIG="$XDG_CONFIG_HOME"/npm/npmrc
export NUGET_PACKAGES="$XDG_CACHE_HOME"/NuGetPackages
export NVM_DIR="$XDG_DATA_HOME"/nvm
export PARALLEL_HOME="$XDG_CONFIG_HOME"/parallel
export PASSWORD_STORE_DIR="$XDG_DATA_HOME"/pass
export PKG_CACHE_PATH="$XDG_CACHE_HOME"/pkg-cache
export PSQL_HISTORY="$XDG_DATA_HOME/psql_history"
export PYENV_ROOT="$XDG_DATA_HOME"/pyenv
export PYLINTHOME="$XDG_CACHE_HOME"/pylint
export PYTHONSTARTUP="$HOME"/python/pythonrc
export RUSTUP_HOME="$XDG_DATA_HOME"/rustup
export SQLITE_HISTORY="$XDG_CACHE_HOME"/sqlite_history
export TERMINFO="$XDG_DATA_HOME"/terminfo
export TERMINFO_DIRS="$XDG_DATA_HOME"/terminfo:/usr/share/terminfo
export TEXMFVAR="$XDG_CACHE_HOME"/texlive/texmf-var
export W3M_DIR="$XDG_DATA_HOME"/w3m
export WINEPREFIX="$XDG_DATA_HOME"/wine
export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority
export XCOMPOSEFILE="$XDG_CONFIG_HOME"/X11/xcompose
export XCURSOR_PATH=/usr/share/icons:$XDG_DATA_HOME/icons
export GRADLE_USER_HOME="$XDG_DATA_HOME"/gradle
export DOTNET_CLI_HOME="$XDG_DATA_HOME"/dotnet
export CUDA_CACHE_PATH="$XDG_CACHE_HOME"/nv
export ANDROID_USER_HOME="$XDG_DATA_HOME"/android

PATH="/usr/lib/xfce-polkit/:$PATH"
PATH="$HOME/.cabal/bin:$PATH"
PATH="$GEM_HOME/ruby/2.6.0/bin:$PATH"
PATH="$GEM_HOME/ruby/3.0.0/bin:$PATH"
PATH="$GOPATH/bin:$PATH"
PATH="${CARGO_HOME}/bin:$PATH"
PATH="$HOME/Android/Sdk/tools/bin:$PATH"
PATH="$HOME/.local/bin:$PATH"
PATH="$HOME/.config/plover/plugins/linux/bin:$PATH"
PATH="$HOME/.nix-profile/bin:$PATH"
export PATH
