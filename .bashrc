function parse_git_branch {
    var=`git branch 2>/dev/null` 
    echo "($var)"| grep "*" #| cut -n 2 
}

PS1="\w \$(parse_git_branch)\$ "
# Add vim as default editor
export EDITOR=vim
export TERMINAL=lxterminal
export BROWSER=firefox
export PATH=$HOME/bin:$PATH

# Gtk themes 
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# Alias general
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

# Alias perso
alias dodo='sudo shutdown now'
alias utc='export http_proxy="proxyweb.utc.fr:3128"'
alias utcs='export https_proxy="proxyweb.utc.fr:3128"'
alias hist='history | grep'

# enable z
. ~/src/z/z.sh

# enable autoproxy UTC
. ~/workspace/autoProxy/autoProxy.sh

# Prompt
PS1='\[\e[1;32m\][\u@\h \W]$(parse_git_branch)\$\[\e[0m\]'
#PS1="$(parse_git_branch) "

# Arch logo display on start
[ ! "$UID" = "0" ] && archbey2
#[ ! "$UID" = "0" ] && fortune | ponysay
