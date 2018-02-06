FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install --yes software-properties-common python-software-properties git python3-pip
RUN add-apt-repository --yes --update ppa:neovim-ppa/stable
RUN apt-get update
RUN apt-get install --yes neovim
RUN pip3 install neovim

COPY dotvim /root/.vim
COPY vimrc /root/.config/nvim/init.vim
COPY dotvim/autoload/plug.vim /root/.local/share/nvim/site/autoload/plug.vim

RUN nvim +PlugInstall +qall

