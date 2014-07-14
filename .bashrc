# Add vim as default editor
export EDITOR=vim
export TERMINAL=lxterminal
export BROWSER=firefox
export PATH=$HOME/bin:$PATH

# Gtk themes 
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# Alias 
alias ls='ls --color=auto'
alias l='ls -la'
alias la='ls -a'
alias ll='ls -l'
alias '..'='cd ..'
alias grep='grep --color=auto'
alias df='df -h'
alias du='du -c -h'
alias mkdir='mkdir -p -v'
alias more='less'
alias ping='ping -c 3'
alias dodo='systemctl halt'
alias hist='history | grep'
alias svim='sudo vim'
alias fork='$TERMINAL &' #open another terminal in the same repository. So fcking useful

# enable z
. ~/src/z/z.sh

# enable autoproxy UTC 
# (Goodbye compiegne)
#. ~/workspace/autoProxy/autoProxy.sh

# enable bash completion
if [ -f /etc/bash_completion ]; then
. /etc/bash_completion
fi

# Prompt
source ~/src/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '

# Arch logo display on start
[ ! "$UID" = "0" ] && archbey2
