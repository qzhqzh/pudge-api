# 固定版本
From ubuntu:20.04
# 维护者
MAINTAINER 28630707@qq.com
# 默认 POSIX 语言不支持中文，C.UTF-8 才支持
ENV LANG C.UTF-8
# 基础包
RUN apt-get update && apt-get install -y python3 \
    python3-pip \
    apache2 \
    libapache2-mod-wsgi-py3 \
    libcurl4-openssl-dev \
    libssl-dev \
    supervisor
# 依赖资源
COPY install_required/ /tmp/install_required/
RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r /tmp/install_required/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 配置文件
RUN /bin/bash /tmp/install_required/apache2.grandbox-sge.sh /home/site/html/dist /home/site/api/storage/logs/apache2 /home/site/api > /etc/apache2/sites-available/grandbox-sge.conf \
    && sed -i 's:export lang=c:export lang=c.utf-8:g' /etc/apache2/envvars \
    && echo "listen 9003" >> /etc/apache2/ports.conf \
    && echo "listen 9004" >> /etc/apache2/ports.conf \
    && a2enmod rewrite \
# 移除资源文件
RUN rm -rf /tmp/install_required/
# 让 apache2 在前台运行，不至于使 docker 自动退出
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

