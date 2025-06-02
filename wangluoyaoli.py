import re
import jieba # For Chinese word segmentation
from collections import Counter # For frequency counting

# --- Word Segmentation Function using Jieba ---
def segment_chinese_title_jieba(title):
    if not title:
        return []
    # Use jieba for segmentation. lcut returns a list of words.
    # The 'cut_all=False' argument means precise mode.
    if '治疗' in title:
        title=title.split('治疗')[1]
    if '用药规律' in  title:
        title=title.split('用药规律')[0]
    if '研究' in title:
        title=title.split('研究')[1]
    if '探讨' in title:
        title=title.split('探讨')[1]
    if '探析' in title:
        title=title.split('探析')[1]
    if '分析' in title:
        title=title.split('分析')[1]
    if '探究' in title:
        title=title.split('探究')[1]
    if '对' in title:
        title=title.split('对')[1]
    if '药理学的' in title:
        title=title.split('药理学的')[1]
    if '治' in title:
        title=title.split('治')[1]
    if '规律' in title:
        title=title.split('规律')[0]
    if '挖掘' in title:
        title=title.split('挖掘')[1]
    if '防治' in title:
        title=title.split('防治')[0]
    if '预防' in title:
        title=title.split('预防')[0]
    if title.endswith('的'):
        title=title.split('的')[0]
    # seg_list = jieba.lcut(title, cut_all=False)
    seg_list=[title]
    return seg_list

# --- Main script ---
input_filename = "wangluoyaoli.txt"
data_from_file = ""

try:
    with open(input_filename, 'r', encoding='utf-8') as f:
        data_from_file = f.read()
    print(f"Successfully read data from '{input_filename}'")
except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found. Please create it in the same directory as the script and paste your data into it.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()

if not data_from_file:
    print("Error: The file is empty or could not be read properly.")
    exit()

# --- Parsing the text data read from the file ---
articles_data_list = []
lines = data_from_file.strip().split('\n')

for line_number, line_content in enumerate(lines):
    if "篇名" in line_content and "作者" in line_content:
        continue
    if not line_content.strip() or not line_content.strip()[0].isdigit():
        if "篇名" in line_content and "作者" in line_content:
             continue
        continue
    
    parts = line_content.split('\t')
    if len(parts) > 1:
        original_index_str = parts[0].strip()
        title_str = parts[1].strip()
        title_str = title_str.replace(" 网络首发", "").replace("（英文） OA", "").replace("（英文）OA", "").replace("（英文）", "").replace(" OA", "")
        articles_data_list.append({"index": original_index_str, "title": title_str})

# --- Deduplication, Segmentation, and Aggregating words for frequency counting ---
deduplicated_articles_with_segmentation = []
seen_titles = set()
all_segmented_words = [] # List to store all words from all titles for frequency counting
new_idx = 1

# Optional: Load a custom dictionary for Jieba if you have one
# jieba.load_userdict("path/to/your/custom_dict.txt")
# Add domain-specific terms to Jieba's dictionary dynamically
custom_terms = [
    "CiteSpace", "VOSviewer", "知识图谱", "可视化分析", "文献计量学",
    "中医药", "中医", "西医", "护理", "研究", "热点", "趋势", "现状",
    "糖尿病", "高血压", "冠心病", "脑卒中", "肺纤维化", "肿瘤", "癌症",
    "针灸", "推拿", "拔罐", "食疗", "养生", "教学", "治疗", "康复",
    "数据挖掘", "人工智能", "互联网", "一带一路", "临床研究", "基础研究",
    "作用机制", "信号通路", "分子生物学", "细胞焦亡", "细胞自噬",
    "随机对照试验", "Meta分析", "系统评价", "客观化", "标准化",
    "非药物干预", "外治法", "内治法", "辨证论治", "证候", "体质",
    "医院评价", "医疗服务", "健康管理", "人才培养", "课程思政",
    "文化传播", "国际化", "现代化", "发展趋势", "前沿",
    "偏瘫", "失眠", "抑郁症", "疼痛", "肥胖症", "荨麻疹", "青光眼",
    "视网膜病变", "骨质疏松症", "溃疡性结肠炎", "功能性便秘", "阿尔茨海默病",
    "帕金森病", "原发性痛经", "多囊卵巢综合征", "甲状腺功能亢进", "甲状腺结节",
    "消化不良", "胃食管反流病", "慢性肾脏病", "急性肺损伤", "心力衰竭",
    "心肌缺血", "再灌注损伤", "动脉粥样硬化", "血瘀证", "气虚证", "湿热证",
    "肾虚证", "肝郁气滞证", "PI3K/AKT/mTOR", "JAK/STAT", "Wnt信号通路", "Notch通路",
    "Th17/Treg", "OBE理念", "子午流注", "玄府学说", "三焦辨证", "“肾藏精”理论",
    "“治未病”", "“病证结合”", "“四联全生态”", "“互联网+”", "“肝肾同源”理论"
]
for term in custom_terms:
    jieba.add_word(term)


for article_entry in articles_data_list:
    title_val = article_entry["title"]
    if title_val not in seen_titles:
        seen_titles.add(title_val)
        # Use Jieba for segmentation
        segmented_title_list = segment_chinese_title_jieba(title_val)
        
        deduplicated_articles_with_segmentation.append({
            "new_index": new_idx,
            "original_index": article_entry["index"],
            "title": title_val,
            "segmented_title_list": segmented_title_list, # Store as list for processing
            "segmented_title_str": ", ".join(segmented_title_list) 
        })
        # Add words to the global list for frequency counting
        # Optional: Filter out single-character words or punctuation if needed
        for word in segmented_title_list:
            # Simple filter: ignore single character words unless they are English letters/numbers
            # and ignore common punctuation if not handled by jieba (jieba usually handles them well)
            # Also, convert to lowercase for case-insensitive counting of English words.
            word_cleaned = word.strip().lower()
            if len(word_cleaned) > 1 or word_cleaned.isalnum(): # Keep words longer than 1 char, or single alphanumeric chars
                if word_cleaned not in ['的', '与', '及', '和', '对', '中', '基于', '分析', '研究', '可视化', '趋势', '现状', '热点', '及', '（', '）', '(', ')', '近', '年', '我国', '国内', '相关', '进展', '应用', '探索', '探讨', '比较', '领域', '展望', '回顾', '前沿', '动态', '作用', '机制', '效果', '评价', '构建', '体系', '模式', '规律']: # Example stop words
                    all_segmented_words.append(word_cleaned)
        new_idx += 1

# --- Word Frequency Counting ---
word_counts = Counter(all_segmented_words)
# Sort by frequency in descending order
sorted_word_counts = word_counts.most_common()

# --- Outputting the table of articles (first 50 and last 10) ---
output_md_content = "| 序号 (新) | 序号 (原) | 篇名 | 篇名分词 (Jieba) |\n"
output_md_content += "|---|---|---|---|\n"

for i, entry_item in enumerate(deduplicated_articles_with_segmentation):
    if i < 50:
        output_md_content += f"| {entry_item['new_index']} | {entry_item['original_index']} | {entry_item['title']} | {entry_item['segmented_title_str']} |\n"

if len(deduplicated_articles_with_segmentation) > 60:
    output_md_content += "| ... | ... | ... | ... |\n"
    for i in range(max(50, len(deduplicated_articles_with_segmentation) - 10), len(deduplicated_articles_with_segmentation)):
        entry_item = deduplicated_articles_with_segmentation[i]
        output_md_content += f"| {entry_item['new_index']} | {entry_item['original_index']} | {entry_item['title']} | {entry_item['segmented_title_str']} |\n"
elif len(deduplicated_articles_with_segmentation) > 50 :
    for i in range(50, len(deduplicated_articles_with_segmentation)):
        entry_item = deduplicated_articles_with_segmentation[i]
        output_md_content += f"| {entry_item['new_index']} | {entry_item['original_index']} | {entry_item['title']} | {entry_item['segmented_title_str']} |\n"

print(f"\nTotal unique articles found and processed: {len(deduplicated_articles_with_segmentation)}")
print("\n--- Output Markdown Table (First 50 and Last 10) ---")
print(output_md_content)

# --- Saving the full processed article list to a Markdown file ---
output_filename_md = "processed_articles_jieba_output-网络药理.md"
try:
    with open(output_filename_md, 'w', encoding='utf-8') as f_out:
        f_out.write(f"Total unique articles found and processed: {len(deduplicated_articles_with_segmentation)}\n\n")
        f_out.write("| 序号 (新) | 序号 (原) | 篇名 | 篇名分词 (Jieba) |\n")
        f_out.write("|---|---|---|---|\n")
        for entry_item in deduplicated_articles_with_segmentation:
            f_out.write(f"| {entry_item['new_index']} | {entry_item['original_index']} | {entry_item['title']} | {entry_item['segmented_title_str']} |\n")
    print(f"\nFull processed article list saved to '{output_filename_md}'")
except Exception as e:
    print(f"An error occurred while writing the article output file: {e}")

# --- Saving Word Frequency Statistics to a file ---
word_freq_filename = "word_frequencies-网络药理.txt"
try:
    with open(word_freq_filename, 'w', encoding='utf-8') as f_freq:
        f_freq.write("词语\t频率\n") # Header for the frequency file
        for word, freq in sorted_word_counts:
            f_freq.write(f"{word}\t{freq}\n")
    print(f"Word frequency statistics saved to '{word_freq_filename}'")
except Exception as e:
    print(f"An error occurred while writing the word frequency file: {e}")
