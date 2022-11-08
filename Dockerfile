FROM osrf/ros:foxy-desktop

ARG gid
ARG uid
ARG user=dev

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS="yes"

RUN apt-get update && apt-get install -y \
    sudo \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    iputils-ping \
    net-tools \
    clang-format \
    clang \
    gdb \
    nano \
    git-all \
    python3-pip \
    wget \
    intel-gpu-tools \
    ros-foxy-ament-cmake-clang-format \
    python3-vcstool 

RUN groupadd -g $gid -o $user && \
    useradd -m -u $uid -g $gid -o -s /bin/bash $user
RUN echo "$user:x:"$uid":$gid:$user,,,:/home/$user:/bin/bash" >> /etc/passwd && \
    echo "$user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$user && \
    chmod 0440 /etc/sudoers.d/$user
USER $user
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.3/zsh-in-docker.sh)" -- \
    -p git -p sudo -p git-prompt -p 'history-substring-search'
RUN rosdep update
RUN echo "PATH=$HOME/dev/.local/bin:$PATH" >> ~/.zshrc && \
    echo "source /opt/ros/foxy/setup.zsh" >> ~/.zshrc && \
    echo "source /home/$user/workspace/install/setup.zsh" >> ~/.zshrc && \
    echo "cd /home/$user/workspace" >> ~/.zshrc && \
    echo 'eval "$(register-python-argcomplete3 ros2)"' >> ~/.zshrc && \
    echo 'eval "$(register-python-argcomplete3 colcon)"' >> ~/.zshrc

RUN echo "PATH=$HOME/dev/.local/bin:$PATH" >> ~/.bashrc && \
    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc && \
    echo "source /home/$user/workspace/install/setup.bash" >> ~/.bashrc && \
    echo "cd /home/$user/workspace" >> ~/.bashrc

RUN sudo python3 -m pip install --upgrade pip
RUN mkdir -p /home/$user/workspace/
WORKDIR /home/$user/
COPY ./workspace ./workspace
COPY ./resources ./resources
RUN sudo chown -R $user:$user /home/$user/
RUN sudo usermod -a -G video $user && \
    sudo chsh -s ~/.zshrc 
WORKDIR /home/$user/resources/
RUN python3 install_requirements.py
WORKDIR /home/$user/workspace/
RUN rosdep install --from-paths ./ros_packages/src --ignore-src --rosdistro $ROS_DISTRO -y
RUN colcon build --symlink-install
RUN ls . | grep -v "build\|install\|log" | xargs rm -r
RUN rm -r ../resources

ENTRYPOINT /bin/zsh