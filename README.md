# 考研英语一训练档案

静态网站，无需构建。将本目录文件置于 GitHub 仓库根目录，在仓库 Settings → Pages 中选择 **Deploy from a branch**、main 分支和根目录即可发布。站点使用相对路径，项目 Pages 地址也可正常打开。

新增一组时，在 `build_entries.py` 中按组 ID 增加完整三题及来源；把大作文图片复制到 `assets/`，核对文字、数据与图片，再运行 `python3 build_entries.py` 更新 `entries.json`。同时更新 `archive/出题记录.md`；权威版本始终是 ChatGPT Library 中同名出题记录。

2026年9月9日至15日的七组在 `historic_reconstructions.json` 中。待译句与大作文原始题图已经恢复；翻译背景段落、小作文题面和大作文 Directions 根据历史记录重建，可用于练习，但不是当日发布内容的逐字重印。检索到原文后应替换对应重建文本并改动来源标记。

仓库只收录公开模拟题面和配图。不要提交 GitHub 令牌、作答记录、讲评或个人资料。
