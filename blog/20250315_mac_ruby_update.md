---
id: notebook/blog/20250315_mac_ruby_update
title: 升级 Mac OS 自带的 Ruby 版本
subtitle: 开发 React Native 需要的 CocoaPods 要求更高版本的 Ruby
subject: 开发环境配置
category: 环境配置
tags: 开发环境
keywords: 
level: 200
cover: https://oscimg.oschina.net/oscnet/4d61b0d3264e651fde2e5a07d856381323d.jpg
authors: Chris Wei
created_when: 2025-03-15
updated_when: 2025-03-15
---

# 背景

根据`React Native`开发环境配置文档，需要安装`cocoapods`。安装过程出现报错，提示依赖包版本需要升级，而升级要求`Ruby`版本最低是`2.7`。而`Mac`自带的Ruby版本是`2.6`。

# 参考

https://dev.to/luizgadao/easy-way-to-change-ruby-version-in-mac-m1-m2-and-m3-16hl
https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/
https://jideije-emeka.medium.com/upgrade-your-default-ruby-version-and-install-cocoapods-newest-way-for-mac-2024-57c156b62226

# 步骤

1. install Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

1. run the following commands according to the instruction after installation

```
echo >> /Users/chris/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/chris/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

1. check

```
brew doctor
```

> You system is ready to brew.

1. install rbenv

```
brew install rbenv ruby-build
```

1. initialize rbenv

```
rbenv init
```

1. Check Your Current Ruby Version

```
ruby -v
```

> ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin24]

1. Install a Newer Ruby Version

```
rbenv install -l
```

> 3.1.6
> 3.2.7
> 3.3.7
> 3.4.2
> jruby-9.4.12.0
> mruby-3.3.0
> picoruby-3.0.0
> truffleruby-24.1.2
> truffleruby+graalvm-24.1.2

```
rbenv install 3.4.2
rbenv global 3.4.2
```

1. Verify Ruby Version

```
ruby -v           
```

> ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin23]

If it still shows the old version, don't worry. Here's a tip:

1. Update Your .zprofile

```
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init - zsh)"
```

Save the file. To apply the changes, either open a new terminal window or reload the profile with:

```
source .zprofile
```

1. Check ruby version

```
ruby -v
```

> ruby 3.4.2 (2025-02-15 revision d2930f8e7a) +PRISM [arm64-darwin24]


1. install cocoapods

```
sudo gem install cocoapods
```

> 

1. config XCode setting

> https://lonare.medium.com/exp-oxcode-must-be-fully-installed-before-you-can-continue-continue-to-the-app-store-65c8ff0d1496