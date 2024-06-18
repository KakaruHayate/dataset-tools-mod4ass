# dataset-tools-mod4ass
A mod for dataset-tools(OpenVPI) for support .ass file(Advanced SubStation Alpha). 

## 2024/6/18
上传了`fix_ap.py`用于将音频的头尾0.1秒静音，需要`librosa`

配合`ds2mark`用于强化学习/模型蒸馏

## 依赖
`pip install wave`

~用来识别wave文件的采样率，这实际上是个防炒饭措施，在你正常处理音频文件的情况下是不需要check_wav的~

一般现代的python版本都能正常运行

## 使用
`python UI.py`
你也可以在命令行下直接使用对应脚本，`-h`命令查看帮助

## 需要注意的地方
 - 使用之前请使用Aegisub中的`字幕（S）→排序所有行→开始时间（S）`将字幕排序，之后将输入的原文行（你在MinLabel中Enter mandarin here…中输入的内容）的说话人标注`raw`，如果你已经标注了对应的label则应该输入`lab`
 - 不保证非Aegisub以及本程序以外程序生成的ASS文件可以由本程序解析转换

## 作用
本仓库程序作用为[Diffsinger(OpenVPI)][1]的[数据集制作工具][2]工作流加入[Aegisub][3]作为优化，从而解决以下问题

 - "AudioSlicer"通过算法判断音频静音部分进行分割，同时需要使用Adobe Audition™导入生成的"marks"进行调整，在实际使用过程中尤其是"静音阈值"和"最短长度"参数难以调节到理想效果。实际上对于各种语言的歌曲，互联网上广泛存在各种语言歌曲的包含时间戳的歌词文件，完全可以通过导入这些文件，在效率更高的编辑软件（如Aegisub）亦或是在AU中对其调整，甚至直接通过歌词从0构建切片时间戳，都是十分方便快捷的
 - "MinLabel"可以让你方便的输入与检查你的label标注，但美中不足的是音频的进度条不是很好用，对于一些你不熟悉的语言或者难以一遍过的语言，检查过程会非常折磨，对于音频的内容检查尤其是多语言对照检查，Aegisub都是经久不衰历经考验的，同时支持两种频谱的显示，你也可以非常方便的选区播放某一段音频

## 我是如何使用的
一般情况下我会直接编辑好.ASS格式的歌词，转化为.CSV格式的marks，导入AutoSlicer，之后导出.json使用MinLabel输出转换好的label，再回到Aegisub进行检查，最后输出.lab文件


[1]: https://github.com/openvpi/DiffSinger
[2]: https://github.com/openvpi/dataset-tools
[3]: https://aegi.vmoe.info/
