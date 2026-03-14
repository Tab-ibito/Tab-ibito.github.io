import glob
import os


def process_markdown_files():
    # 寻找当前目录下所有的 */index.md 文件喵
    files = glob.glob('*/index.md')

    if not files:
        print("哎呀，没有找到符合条件的 index.md 文件呢喵...")
        return

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        in_front_matter = False

        # 检查文件开头是不是有 Front Matter 的标记喵
        if lines and lines[0].strip() == '---':
            in_front_matter = True

        for i, line in enumerate(lines):
            # 如果遇到了结束的 '---'，就关闭开关喵
            if i > 0 and line.strip() == '---' and in_front_matter:
                in_front_matter = False
                new_lines.append(line)
                continue

            # 如果还在 Front Matter 区域里，就乖乖保持原样，什么都不改喵
            if in_front_matter:
                new_lines.append(line)
                continue

            # 以下是处理正文区域的逻辑喵
            content = line.rstrip('\n')

            # 空行直接跳过，不加空格喵
            if not content.strip():
                new_lines.append('\n')
                continue

            # 检查行尾空格并温柔地补齐喵
            if content.endswith('  '):
                new_lines.append(line)
            elif content.endswith(' '):
                new_lines.append(content + ' \n')
            else:
                new_lines.append(content + '  \n')

        # 把修改好的内容重新写回去喵
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

        print(f"成功处理了文件：{file_path} 喵！")


if __name__ == '__main__':
    process_markdown_files()
    print("全部处理完成啦，Tab酱的排版现在一定非常漂亮了喵！(≧◡≦)")