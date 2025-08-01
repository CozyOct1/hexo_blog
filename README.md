# Hexo Blog

这是一个用于存放 Obsidian 笔记并自动化部署到 GitHub Pages 的 Hexo 博客项目。

## 项目目的

- 将 Obsidian 笔记转换为 Hexo 博客文章。
- 自动化部署 Hexo 博客到 GitHub Pages，实现持续集成和持续部署。

## 使用方法

1.  **克隆仓库**：
    ```bash
    git clone https://github.com/your-username/hexo_blog.git
    cd hexo_blog
    ```
2.  **安装依赖**：
    ```bash
    pip install -r requirements.txt
    npm install -g hexo-cli
    npm install
    ```
3.  **编写文章**：
    将您的 Obsidian Markdown 笔记放置在 `source/_posts/` 目录下。
4.  **本地预览**：
    ```bash
    hexo clean
    hexo generate
    hexo server
    ```
    访问 `http://localhost:4000` 预览您的博客。
5.  **部署到 GitHub Pages**：
    运行 `main.py` 脚本，它将自动化执行 Hexo 的生成和部署过程。
    ```bash
    python main.py
    ```

## 自动化部署流程

`main.py` 脚本负责以下自动化任务：

1.  清理 Hexo 生成的旧文件。
2.  生成最新的 Hexo 静态文件。
3.  将生成的静态文件部署到 GitHub Pages。

确保您已在 Hexo 的 `_config.yml` 文件中配置了正确的部署信息。