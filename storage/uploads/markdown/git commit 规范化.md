# 项目年终总结导致实施git commit规范化



git commit 之前瞎几把写，写得到是快，但是最后统计项目的时候，就搞死人了。



## Part 1

目前打算使用的方法为：

1. git commit 写规范点
2. 用 standard-version 工具自动生成 change log



规范化标准参考 [https://keepachangelog.com/zh-CN/1.0.0/](https://keepachangelog.com/zh-CN/1.0.0/)

![](http://35.201.166.242:8080/images/2020/01/09/chrome_ckGEv9rqcT.png)

注：例子样式见附录一

- 动作基本分为3类，Added、Changed、Removed

- 每次分割以版本号为区间

- commit 内容有描述、引用作者

大致看下来很清楚，但是我没法一个去手动维护，肯定有自动化的工具。



## Part 2

寻找工具过程中，有几种比较星高的，肯定是经过了大家的检验。

最好评的是一个从github的issue和pull request中提取change logs的项目，当然一个issue通常能解决一个bug或者一个新的特性。

但是对于我们这种开发人较少的，至少目前没有人写issue，change logs的来源只能是来自git commit了啊。选到最后选择了`standard-version`工具，当然很有可能会换，比较大佬选择了另一款，还可以给pycharm装插件，看情况吧。

所以，目前最主要的是定义好 git commit的格式，其他交给工具了。



1. 变动类型，参考 `keepachangelog`

   ![](http://35.201.166.242:8080/images/2020/01/09/chrome_L7j7cphPKo.png)

   推荐有 6 种类型，噗

   我印象中还会用Fixed、Feat等，总之这个东西不统一。

2. [语义化版本格式](https://semver.org/)

   教你怎么定义版本号..（以后研究，暂时tag版本号由工具自动生成好了）

## Part 3

参考资料差不多了，以下是自己以后怎么干。



例子：

```shell
git commit -m 'fix(blog): fix upload cant work bug'
or
git commit -m 'feat(blog): 增加markdown文件上传文章功能'
```

以上对应了`修复`、`新特性`，如果是`优化`用 perf（默认是隐藏）

格式为 `action` + `(module or function)` + `: desc`

此处中间部分甚至可以忽略，看自己心情了。这里也没有用 git cz 啥子来校验，全凭自己干 ^_^

而 standard-version 的其他参数，等下次详细研究再补上。





---

**附录一**

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2017-06-20
### Added
- New visual identity by [@tylerfortune8](https://github.com/tylerfortune8).
- Version navigation.
- Links to latest released version in previous versions.
- "Why keep a changelog?" section.
- "Who needs a changelog?" section.
- "How do I make a changelog?" section.
- "Frequently Asked Questions" section.
- New "Guiding Principles" sub-section to "How do I make a changelog?".
- Simplified and Traditional Chinese translations from [@tianshuo](https://github.com/tianshuo).
- German translation from [@mpbzh](https://github.com/mpbzh) & [@Art4](https://github.com/Art4).
- Italian translation from [@azkidenz](https://github.com/azkidenz).
- Swedish translation from [@magol](https://github.com/magol).
- Turkish translation from [@karalamalar](https://github.com/karalamalar).
- French translation from [@zapashcanon](https://github.com/zapashcanon).
- Brazilian Portugese translation from [@Webysther](https://github.com/Webysther).
- Polish translation from [@amielucha](https://github.com/amielucha) & [@m-aciek](https://github.com/m-aciek).
- Russian translation from [@aishek](https://github.com/aishek).
- Czech translation from [@h4vry](https://github.com/h4vry).
- Slovak translation from [@jkostolansky](https://github.com/jkostolansky).
- Korean translation from [@pierceh89](https://github.com/pierceh89).
- Croatian translation from [@porx](https://github.com/porx).
- Persian translation from [@Hameds](https://github.com/Hameds).
- Ukrainian translation from [@osadchyi-s](https://github.com/osadchyi-s).

### Changed
- Start using "changelog" over "change log" since it's the common usage.
- Start versioning based on the current English version at 0.3.0 to help
translation authors keep things up-to-date.
- Rewrite "What makes unicorns cry?" section.
- Rewrite "Ignoring Deprecations" sub-section to clarify the ideal
  scenario.
- Improve "Commit log diffs" sub-section to further argument against
  them.
- Merge "Why can’t people just use a git log diff?" with "Commit log
  diffs"
- Fix typos in Simplified Chinese and Traditional Chinese translations.
- Fix typos in Brazilian Portuguese translation.
- Fix typos in Turkish translation.
- Fix typos in Czech translation.
- Fix typos in Swedish translation.
- Improve phrasing in French translation.
- Fix phrasing and spelling in German translation.

### Removed
- Section about "changelog" vs "CHANGELOG".

## [0.3.0] - 2015-12-03
### Added
- RU translation from [@aishek](https://github.com/aishek).
- pt-BR translation from [@tallesl](https://github.com/tallesl).
- es-ES translation from [@ZeliosAriex](https://github.com/ZeliosAriex).

## [0.2.0] - 2015-10-06
### Changed
- Remove exclusionary mentions of "open source" since this project can
benefit both "open" and "closed" source projects equally.

## [0.1.0] - 2015-10-06
### Added
- Answer "Should you ever rewrite a change log?".

### Changed
- Improve argument against commit logs.
- Start following [SemVer](https://semver.org) properly.

## [0.0.8] - 2015-02-17
### Changed
- Update year to match in every README example.
- Reluctantly stop making fun of Brits only, since most of the world
  writes dates in a strange way.

### Fixed
- Fix typos in recent README changes.
- Update outdated unreleased diff link.

## [0.0.7] - 2015-02-16
### Added
- Link, and make it obvious that date format is ISO 8601.

### Changed
- Clarified the section on "Is there a standard change log format?".

### Fixed
- Fix Markdown links to tag comparison URL with footnote-style links.

## [0.0.6] - 2014-12-12
### Added
- README section on "yanked" releases.

## [0.0.5] - 2014-08-09
### Added
- Markdown links to version tags on release headings.
- Unreleased section to gather unreleased changes and encourage note
keeping prior to releases.

## [0.0.4] - 2014-08-09
### Added
- Better explanation of the difference between the file ("CHANGELOG")
and its function "the change log".

### Changed
- Refer to a "change log" instead of a "CHANGELOG" throughout the site
to differentiate between the file and the purpose of the file — the
logging of changes.

### Removed
- Remove empty sections from CHANGELOG, they occupy too much space and
create too much noise in the file. People will have to assume that the
missing sections were intentionally left out because they contained no
notable changes.

## [0.0.3] - 2014-08-09
### Added
- "Why should I care?" section mentioning The Changelog podcast.

## [0.0.2] - 2014-07-10
### Added
- Explanation of the recommended reverse chronological release ordering.

## [0.0.1] - 2014-05-31
### Added
- This CHANGELOG file to hopefully serve as an evolving example of a
  standardized open source project CHANGELOG.
- CNAME file to enable GitHub Pages custom domain
- README now contains answers to common questions about CHANGELOGs
- Good examples and basic guidelines, including proper date formatting.
- Counter-examples: "What makes unicorns cry?"

[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.8...v0.1.0
[0.0.8]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.0.1



