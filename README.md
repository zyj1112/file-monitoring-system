# A file status monitoring system written for Innovation Project for College Students chickenglass
***
## Introduction
watching.py is a file status monitoring program, the main function is to print out the log of file changes

watching_refreshing.py is a file status monitoring (print out the log of file changes) + program to refresh the browser when the file changes
***
## Main function:
Mentor's blog:[HackMD blog](https://hackmd.io/LoFPSapEQhWjBfCFVfytVQ)The description in the blog is：

File status monitoring (can use livereload):
* Input file monitoring + meta rebuild: run the build system if there is a change. Build the system and update the new meta data.
* Output file monitoring + live preview: Automatically refresh the browser live preview after the output changes. The world of writing a lot of things by yourself and refreshing manually has come to an end. (you can use livereloadx)

From my point of view, what I need to accomplish is mainly the following two:
* Monitor whether the html file changes: we directly change the html file when using the edit mode, and we need to design a program to monitor the change of the html file
* After the html file is changed, refresh the browser: so that we don't need to manually refresh the browser,~~Although I think manual refresh is not very troublesome~~
