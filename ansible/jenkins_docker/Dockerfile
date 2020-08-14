FROM jenkins/jenkins:lts

USER root
RUN mkdir /var/log/jenkins
RUN mkdir /var/cache/jenkins
RUN chown -R jenkins:jenkins /var/cache/jenkins
RUN chown -R jenkins:jenkins /var/log/jenkins
RUN apt-get update \
      && apt-get install -y sudo libltdl7 \
      && rm -rf /var/lib/apt/lists/*
RUN adduser jenkins sudo
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN sudo apt update -y
RUN apt install python3-pip -y 
RUN pip3 install requests jinja2 argparse urllib3 openpyxl

USER jenkins
ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS="--handlerCountMax=300 --logfile=/var/log/jenkins/jenkins.log --webroot=/var/cache/jenkins/war"
