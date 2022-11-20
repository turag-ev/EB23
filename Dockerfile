FROM ros:foxy-ros-base
ARG gid
ARG uid
ARG user=dev

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS="yes"

RUN apt-get update && apt-get install -y \
    sudo \
    iputils-ping \
    net-tools \
    clang-format \
    gdb \
    curl \
    nano \
    git \
    zsh \
    wget \
    ros-foxy-ament-cmake-clang-format \
    python3-pip \
    python3-vcstool \
    libqt5svg5 \
    python3-tk 

RUN groupadd -g $gid -o $user && \
    useradd -m -u $uid -g $gid -o -s /bin/bash $user && \
    echo "$user:x:"$uid":$gid:$user,,,:/home/$user:/bin/bash" >> /etc/passwd && \
    echo "$user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$user && \
    chmod 0440 /etc/sudoers.d/$user
USER $user
RUN sudo python3 -m pip install --upgrade pip && \  
    rosdep update && \
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN echo "PATH=$HOME/.local/bin:$PATH" >> ~/.zshrc && \
    echo "source /opt/ros/foxy/setup.zsh" >> ~/.zshrc && \
    echo "source /home/$user/workspace/install/setup.zsh" >> ~/.zshrc && \
    echo "cd /home/$user/workspace" >> ~/.zshrc && \
    echo 'eval "$(register-python-argcomplete3 ros2)"' >> ~/.zshrc && \
    echo 'eval "$(register-python-argcomplete3 colcon)"' >> ~/.zshrc && \
    echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc && \
    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc && \
    echo "source /home/$user/workspace/install/setup.bash" >> ~/.bashrc && \
    echo "cd /home/$user/workspace" >> ~/.bashrc

WORKDIR /home/$user/
COPY ./workspace ./workspace/
COPY ./resources ./resources/
RUN sudo chown -R $user:$user /home/$user/ && \
    sudo chsh -s ~/.zshrc 
RUN python3 ./resources/install_requirements.py && \
    rosdep install --from-paths ./workspace/ros_packages/src --ignore-src --rosdistro $ROS_DISTRO -y
RUN cd ./workspace && . "/opt/ros/foxy/setup.sh" && colcon build --symlink-install
RUN rm -r ./resources && \
    cd ./workspace/ && ls . | grep -v "build\|install\|log" | xargs rm -r 
ENTRYPOINT [ "zsh" ] 