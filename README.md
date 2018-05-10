# conan-box2d

![conan-box2d image](/images/conan-box2d.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/box2d%3Aconan/images/download.svg?version=2.3.1%3Astable)](https://bintray.com/conan-community/conan/box2d%3Aconan/2.3.1%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-box2d.svg?branch=stable%2F2.3.1)](https://travis-ci.org/conan-community/conan-box2d)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/2.3.1?svg=true)](https://ci.appveyor.com/project/<appveyor_user>/conan-box2d/branch/stable/2.3.1)

[Conan.io](https://conan.io) package for [box2d](http://box2d.org/) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/box2d%3Aconan).

## Basic setup

    $ conan install box2d/2.3.1@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    box2d/2.3.1@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)