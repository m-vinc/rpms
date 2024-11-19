
# My Personal RPM Packages

This repository contains all the RPM spec files I’ve written and will write in the future. Feel free to use them, open Issues, or submit Pull Requests.

---

## Why?  

I’m learning how to package software — that’s the main goal.  

I’m tired of everything being "packaged" using Docker and Dockerfiles. I used to be one of those people who relied on Docker for "packaging" services in my homelab. But lately, I’ve started migrating some services from Podman/Docker to Proxmox containers (LXC), where I need to install services using something revolutionary: the operating system’s package manager.  

Do I enjoy it? Probably. The more I do it, the more I appreciate it — and the more I grow frustrated with the typical new project on Git{Hub,GitLab} that lacks proper packaging. Instead, there’s usually just a Dockerfile containing the entire earth (and if you’re lucky, some multi-stage build with nested images dependencies).  

Let’s be honest: many people create Docker images by installing packages via a package manager *inside* the image. So why not package the software first and then build a Docker image from it?  

---

## No Hate, Just Learning  

There’s no real hate behind this. I’m just using it as an excuse to learn something new! 😄  

